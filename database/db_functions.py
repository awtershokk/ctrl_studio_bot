import sqlite3

DATABASE_NAME = 'orders.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except sqlite3.Error as e:
        print(e)
    return conn

def insert_order(conn, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status):
    query = '''
        INSERT INTO orders (client_id, client_name, order_category, order_type, order_deadline, order_price, order_status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    try:
        conn.execute(query, (client_id, client_name, order_category, order_type, order_deadline, order_price, order_status))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def get_all_orders(conn):
    query = '''
        SELECT * FROM orders
    '''
    try:
        cursor = conn.execute(query)
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(e)

def update_order_status(conn, order_id, new_status):
    query = '''
        UPDATE orders
        SET order_status = ?
        WHERE order_id = ?
    '''
    try:
        conn.execute(query, (new_status, order_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

