from telebot import types

def feedback(message, bot):
    chat_id = message.chat.id

    feed_keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='☎️ Служба поддержки', url='https://t.me/ctrlstudio_admin')
    feed_keyboard.add(url_button)

    f1 = 'Для решения любых вопросов, связанных с использованием бота, мы рекомендуем обратиться к команде /info.\n'
    f2 = 'Если у вас возникли другие вопросы или требуется дополнительное консультирование, не стесняйтесь обратиться в службу поддержки.'

    f = f1 + f2
    bot.send_message(chat_id, f, parse_mode="Markdown", disable_web_page_preview = True, reply_markup=feed_keyboard)