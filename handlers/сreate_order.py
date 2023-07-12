from keyboards.order_inline_keyboards import select_order_type, select_order_deadline

info_product = {
    'Категория работы': None,
    'Тип работы': None,
    'Сроки': None,
    'Расчетная стоимость': None
}
category_texts= {
    'diplom': ['Дипломная работа', 9000],
    'kursovaya': ['Курсовая работа', 4000],
    'practika': ['Практика(УП/ПП)', 2000],
    'laborator': ['Лабораторная работа', 500],
    'another': ['Другое', 3000]
}
type_texts= {
    'site': 'Сайт',
    'desktop': 'Desktop приложение',
    'tgbot': 'Telegram бот',
    'console': 'Консольное приложение',

}
deadline_text = {
    'min1week': ['Меньше 1 недели', 2],
    'odna_dve_week': ['1-2 недели', 1.5],
    'two_week_month': ['2 недели - 1 месяц', 1.2],
    'month-twomonth': ['1-2 месяца', 1],
    'two-month_more': ['2 месяца и более', 0.9]
}

def choise_order_category(call, bot):
    global info_product
    global category_texts
    category = call.data
    info_product['Категория работы'] = category_texts[category][0]
    info_product['Расчетная стоимость'] = category_texts[category][1]


def choise_order_type(call, bot):
    global info_product
    global type_texts
    types = call.data
    info_product['Тип работы'] = type_texts[types]


def choise_order_deadline(call, bot):
    global info_product
    global deadline_text
    category = call.data
    info_product['Сроки'] = deadline_text[category][0]
    info_product['Расчетная стоимость'] *= deadline_text[category][1]

def last_create_order_message(call, bot):
    global info_product

    ttl1 = '*Ваш заказ:*\n'
    ttl2 = '*№ заказа* - #1\n'
    ttl3 = f"*Категория работы* - {info_product['Категория работы']}\n"
    ttl4 = f"*Тип работы* - {info_product['Тип работы']}\n"
    ttl5 = f"*Сроки* - {info_product['Сроки']}\n"
    ttl6 = f"*Расчетная стоимость* - {info_product['Расчетная стоимость']}\n"
    ttl7 = '*(Окончательная стоимость зависит от сложности работы, и может отличаться от расчетной)*'
    total_message = ttl1 + ttl2 + ttl3 + ttl4 + ttl5 + ttl6 + ttl7

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=total_message, parse_mode="Markdown")





