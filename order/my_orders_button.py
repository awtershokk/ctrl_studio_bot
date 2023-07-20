from database.db_functions import select_client_orders, create_connection
conn = create_connection()

status_on_ru ={
    'Created':'Создан',
    'At_work':'В разработке',
    'Completed':'Выполнен'
}

def clients_order(message, bot):
    global status_on_ru
    global conn

    client_id = message.from_user.id
    rows = select_client_orders(conn, client_id)

    if not rows:
        bot.send_message(chat_id=message.chat.id, text="На данный момент у вас нет заказов.")
    else:
        for row in rows:
            ttl1 = '*Ваш заказ:*\n'
            ttl2 = f'*№ заказа* - #{row[0]}\n'
            ttl3 = f"*Категория работы* - {row[4]}\n"
            ttl4 = f"*Тип работы* - {row[5]}\n"
            ttl5 = f"*Сроки* - {row[6]}\n"
            ttl6 = f"*Расчетная стоимость* - {row[7]}\n"
            ttl7 = f'*Начало работы* - {row[9]}\n'
            ttl8 = f'*Статус* - {status_on_ru[row[8]]}\n'
            total_message = ttl1 + ttl2 + ttl3 + ttl4 + ttl5 + ttl6 + ttl7 + ttl8
            bot.send_message(chat_id=message.chat.id, text=total_message, parse_mode="Markdown")


