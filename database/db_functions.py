import datetime
import os
import sqlite3
from dotenv import load_dotenv

DATABASE_NAME = 'orders.db'
admin1 = os.getenv('ADMIN1')
admin2 = os.getenv('ADMIN2')
admins = [admin1, admin2]
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
    except sqlite3.Error as e:
        print(e)
    return conn

def insert_order(conn, client_username, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status, order_start='-'):
    query = '''
        INSERT INTO orders (client_username, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status, order_start)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    try:
        conn.execute(query, (client_username, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status, order_start))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def select_client_orders(conn, client_id):
    query = '''
        SELECT * FROM orders
        WHERE client_id = ? AND order_status != 'draft'
    '''
    try:
        cursor = conn.execute(query, (client_id,))
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
def select_client_username(conn, client_id):
    query = '''
        SELECT client_username FROM clients
        WHERE client_id = ?
    '''
    try:
        cursor = conn.execute(query, (client_id,))
        result = cursor.fetchone()
        if result:
            client_username = f"@{result[0]}"
            return client_username
        else:
            return None
    except sqlite3.Error as e:
        print(e)
def selecct_client_draft_orders(conn, client_id):
    query = '''
        SELECT * FROM orders
        WHERE client_id =? AND order_status = 'draft'
    '''
    try:
        cursor = conn.execute(query, (client_id,))
        rows = cursor.fetchall()
        return rows
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








def confirm_order(conn, order_id, total_cost):
    global  admins
    query = '''
        UPDATE orders
        SET order_status = ?
        SET order_start = ?
        SET order_price = ?
        WHERE order_id = ?
    '''
    order_status = 'at_work'
    order_start = datetime.now()

    try:
        conn.execute(query, (total_cost, order_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
