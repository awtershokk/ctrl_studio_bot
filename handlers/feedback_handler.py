def feedback(message, bot):
    chat_id = message.chat.id
    f1 = 'Для решения любых вопросов, связанных с использованием бота, мы рекомендуем обратиться к команде /info, где вы сможете получить всю нужную информацию.\n'
    f2 = 'Если у вас возникли другие вопросы или требуется дополнительное консультирование, не стесняйтесь обратиться в [службу поддержки](https://t.me/ctrlstudio_admin).'
    f = f1 + f2
    bot.send_message(chat_id, f, parse_mode="Markdown", disable_web_page_preview = True)