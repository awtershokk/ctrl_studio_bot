def feedback(message, bot):
    chat_id = message.chat_id
    text = 'Если у вас возникли какие-либо вопросы по использованию бота можете использовать команду /info \nЕсли у вас остаются какие-то другие вопросы напишите нашему администратору @ctrlstudio_admin'
    bot.send_message(chat_id, text)