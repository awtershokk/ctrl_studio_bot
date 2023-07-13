import telebot
def help_handler(message, bot):
    bot.send_message(message.chat.id, "Помощь", parse_mode="Markdown")