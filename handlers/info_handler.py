import telebot
def help_handler(message, bot):
    infomsg = 'Со всеми правилами и условиями для создания заказа вы можете ознакомиться [здесь](https://telegra.ph/Pravila-i-usloviya-zakaza-07-13).'
    bot.send_message(message.chat.id, infomsg, parse_mode="Markdown", disable_web_page_preview = True)