from telebot import types
from database.db_functions import select_client_username, selecct_client_draft_orders, select_client_orders,create_connection
conn = create_connection()
def send_message_client_order(message, bot):
    global conn
    client_id = message.from_user.id
    first_message_my_order = types.InlineKeyboardMarkup()
    client_username = select_client_username(conn, client_id)
    client_order_quantity = len(select_client_orders(conn, client_id))

    order_button = types.InlineKeyboardButton('Заказы', callback_data='order')
    draft_button = types.InlineKeyboardButton('Черновики', callback_data='draft')

    first_message_my_order.add(order_button)
    first_message_my_order.add(draft_button)

    my_orders_message = f'Имя: {client_username}\nКоличество заказов: {client_order_quantity}'

    bot.send_message(message.chat.id, my_orders_message, reply_markup=first_message_my_order)
