import telebot
def start_handler(message, bot, main_keyboard):
    user_mention = message.from_user.first_name
    start1 = f"🖐 Привет, *{user_mention}*!\n"
    start2 = "Учишься на IT специальности, но нет времени и сил, чтобы написать приложение для очередной курсовой? Не беда!\n"
    start3 = "Я бот студии *«CTRL C + CTRL V»*, с моей помощью ты сможешь создать заказ на разработку любого программного продукта: *сайта*, *desktop приложения* *и др.*"
    start_message = start1 + start2 + start3
    bot.send_message(message.chat.id, start_message, parse_mode="Markdown", reply_markup=main_keyboard)
