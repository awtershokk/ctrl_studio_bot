#(conn, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status)
from handlers.сreate_order import info_product
from database.db_functions import create_connection
from database.db_functions import insert_order
conn = create_connection()

def working_with_order_creation(call, bot):
    global conn
    client_id = call.message.from_user.id
    client_name = call.message.from_user.first_name
    order_category = info_product['Категория работы']
    order_type = info_product['Тип работы']
    order_deadline = info_product['Сроки']
    order_price = info_product['Расчетная стоимость']
    order_status = info_product['Статус']
    insert_order(conn, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status)




