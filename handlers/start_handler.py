import telebot
import sqlite3

def start_handler(message, bot, main_keyboard):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    client_username = message.from_user.username
    client_id = message.from_user.id
    client_name = message.from_user.first_name

    cursor.execute("SELECT * FROM clients WHERE client_id = ?", (client_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()

        bot.send_message(message.chat.id, "You are already registered.")
    else:

        cursor.execute("INSERT INTO clients (client_username, client_id, client_name) VALUES (?, ?, ?)",
                       (client_username, client_id, client_name))
        conn.commit()
        conn.close()

        start1 = f"🖐 Привет, *{client_name}*!\n"
        start2 = "Учишься на IT специальности, но нет времени и сил, чтобы написать приложение для очередной курсовой? Не беда!\n"
        start3 = "Я бот студии *«CTRL C + CTRL V»*, с моей помощью ты сможешь создать заказ на разработку любого программного продукта: *сайта*, *desktop приложения* *и др.*"
        start_message = start1 + start2 + start3
        bot.send_message(message.chat.id, start_message, parse_mode="Markdown", reply_markup=main_keyboard)


