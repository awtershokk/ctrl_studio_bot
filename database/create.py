import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        client_id INTEGER,
        client_name TEXT    ,
        order_category TEXT,
        order_type TEXT,
        order_deadline TEXT,
        order_price REAL,
        order_status TEXT
    )
''')

cursor.close()
conn.close()