def feedback(message, bot):
    chat_id = message.chat.id
    text = 'Для решения любых вопросов, связанных с использованием бота, мы рекомендуем обратиться к команде /info, где вы сможете получить всю нужную информацию.\nЕсли у вас возникли другие вопросы или требуется дополнительное консультирование, не стесняйтесь обратиться в [службу поддержки](https://t.me/ctrlstudio_admin).'
    bot.send_message(chat_id, text, parse_mode="Markdown", disable_web_page_preview = True)