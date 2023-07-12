#(conn, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status)
from handlers.сreate_order import info_product
from database.db_functions import create_connection
from database.db_functions import insert_order
from dotenv import load_dotenv
import os
admin = os.getenv('ADMIN_ID')
conn = create_connection()

def working_with_order_creation(call, bot):
    global conn
    client_username = call.from_user.username
    client_name = call.from_user.first_name
    order_category = info_product['Категория работы']
    order_type = info_product['Тип работы']
    order_deadline = info_product['Сроки']
    order_price = info_product['Расчетная стоимость']
    order_status = info_product['Статус']
    insert_order(conn, client_username, client_name, order_category, order_type, order_deadline, order_price, order_status)
    message_for_admin = f"Категория работы: {info_product['Категория работы']}\nТип работы: {info_product['Тип работы']}\nСроки: {info_product['Сроки']}\nРасчетная стоимость: {info_product['Расчетная стоимость']}\nСтатус: {info_product['Статус']}"

    for id in admin:
        bot.send_message(chat_id=id, text=message_for_admin)




