def rev_handler(message, bot):
    revmsg = 'Все отзывы о нашей работе находятся [здесь](https://t.me/ctrlstudio_reviews).'
    bot.send_message(message.chat.id, revmsg, parse_mode="Markdown", disable_web_page_preview = True)