from telebot import types
from database.db_functions import selecct_client_draft_orders, select_client_orders ,create_connection
conn = create_connection()
def clients_order(call, bot):
    global conn
    client_id = call.message.from_user.id
    rows = select_client_orders(conn, client_id)
    for row in rows:
        ttl1 = '*Ваш заказ:*\n'
        ttl2 = '*№ заказа* - #1\n'
        ttl3 = f"*Категория работы* - {row[4]}\n"
        ttl4 = f"*Тип работы* - {row[5]}\n"
        ttl5 = f"*Сроки* - {row[6]}\n"
        ttl6 = f"*Расчетная стоимость* - {row[7]}\n"
        ttl7 = f'Начало работы: {row[9]}\n'
        ttl8 = f'Статус: {row[8]}\n'
        total_message = ttl1 + ttl2 + ttl3 + ttl4 + ttl5 + ttl6 + ttl7 + ttl8
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=total_message, parse_mode="Markdown")

# client_username, client_id, client_name, order_category, order_type, order_deadline, order_price, order_status):