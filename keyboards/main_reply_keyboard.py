from telebot import types
def create_reply_keyboard():
    main_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    create_order_button = "🛠 Создать заказ"
    my_orders_button = "👤 Мои заказы"
    feedback_button = "📞 Обратная связь"
    reviews_button = "📝 Отзывы"

    main_keyboard.add(create_order_button, my_orders_button)
    main_keyboard.add(feedback_button, reviews_button)

    return main_keyboard