import sqlite3

continuing = "y"
con = sqlite3.connect(":memory:")   # Stores database in ram
con.isolation_level = None
cur = con.cursor()

cur.execute('''CREATE TABLE stock (id integer, model text, name text, qty integer, price real)''')  # Defines the qualities of the database

stock_items = [(1, 'Road', 'Allez', 2, 999.99),
              (2, 'Road', 'Diverge E5', 1, 1299.99),
              (3, 'Mountain', 'Rockhopper', 2, 699.99),
              (4, 'Mountain', 'Chisel', 3, 1599.99),
              (5, 'Kids', 'Hotwalk', 2, 224.99),
              (6, 'Kids', 'Jett 24', 4, 599.99),
              (7, 'Kids', 'Riprock Coaster 20', 1, 324.99),
              (8, 'Fitness', 'Sirrus 4.0', 2, 1499.99),
              (9, 'Fitness', 'Turbo Vado 3.0', 1, 3249.99),
              (10, 'Fitness', 'Sirrus 1.0', 4, 649.99),
              (11, 'Road', 'Allez Sport', 0, 1199.99)]
cur.executemany('INSERT INTO stock VALUES (?, ?, ?, ?, ?)', stock_items)    # Fills in the database with new data

con.commit()    # Saves changes

while continuing.lower() == "y":
    print()

    function = input("What action do you wish to perform (insert, modify, delete, query): ").lower()

    if function == "modify" or function == "delete" or function == "query":    # Gets the WHERE statement if it is not an insert statement
        filter_data = input("Are there any qualifiers on what you would like to look at/edit (ex: qty = 2 or name = 'Allez') Leave blank to ignore: ")

    if function == "insert":
        insert_id = input("What is the id of the new item: ")
        insert_model = input("What is the model of the new item (Road, Kids, Mountain, Fitness): ")
        insert_name = input("What is the name of the new item: ")                                       # Getting all parts for the insert statement
        insert_qty = input("What is the quantity of the new item: ")
        insert_price = input("What is the price of the new item: ")
        cur.execute(f"INSERT INTO stock VALUES ('{int(insert_id)}','{insert_model}','{insert_name}','{int(insert_qty)}','{float(insert_price)}')")
        con.commit()

    elif function == "modify":  # Modifies an existing item. Used to change the qualities of an item.
        data_modify = input("What do you want to change (id, model, name, qty, price): ")
        data_modify_value = input("What is the new value: ")
        if filter_data != "":
            cur.execute(f'UPDATE stock SET {data_modify} = {data_modify_value} WHERE {filter_data}')
        else:
            cur.execute(f'UPDATE stock SET {data_modify} = {data_modify_value}')
        con.commit()

    elif function == "delete":  # Delete/closes out an item in the store
        if filter_data != "":
            cur.execute(f'DELETE FROM stock WHERE {filter_data}')
        else:
            cur.execute(f'DELETE FROM stock')
        con.commit()

    elif function == "query":   # Prints out the stock of the store
        print()
        if filter_data != "":
            for row in cur.execute(f'SELECT * FROM stock WHERE {filter_data}'):
                if row[3] == 1:
                    print("We have " + str(row[3]) + " " + row[2] + " " + row[1] + " bike. It costs " + str(row[4]) + "." )
                elif row[3] > 1:
                    print("We have " + str(row[3]) + " " + row[2] + " " + row[1] + " bikes. They cost " + str(row[4]) + " each." )
                elif row[3] == 0:
                    print("We are out of the " + row[2] + " " + row[1] + " bike. They cost " + str(row[4]) + " if you would like to wait for them to come back in stock." )
        else:
            for row in cur.execute('SELECT * FROM stock'):
                if row[3] == 1:
                    print("We have " + str(row[3]) + " " + row[2] + " " + row[1] + " bike. It costs " + str(row[4]) + "." )
                elif row[3] > 1:
                    print("We have " + str(row[3]) + " " + row[2] + " " + row[1] + " bikes. They cost " + str(row[4]) + " each." )
                elif row[3] == 0:
                    print("We are out of the " + row[2] + " " + row[1] + " bike. They cost " + str(row[4]) + " if you would like to wait for them to come back in stock." )
    continuing = input("Would you like to continue viewing/editing the database [y/n]: ")