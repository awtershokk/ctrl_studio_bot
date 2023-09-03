from telebot import types

def feedback(message, bot):
    chat_id = message.chat.id

    feed_keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='📝 Правила и условия заказа', url='https://telegra.ph/Pravila-i-usloviya-zakaza-07-13')
    url_button2 = types.InlineKeyboardButton(text='☎️ Служба поддержки', url='https://t.me/ctrlstudio_admin')
    url_button3 = types.InlineKeyboardButton(text='📋 Отзывы', url='https://t.me/ctrlstudio_reviews')
    feed_keyboard.add(url_button)
    feed_keyboard.add(url_button2)
    feed_keyboard.add(url_button3)

    f = '⚙️ Навигатор по боту'

    bot.send_message(chat_id, f, parse_mode="Markdown", disable_web_page_preview = True, reply_markup=feed_keyboard)