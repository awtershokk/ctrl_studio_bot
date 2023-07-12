from telebot import types
from unicodedata import category

def select_order_category(message, bot):
    select_category_keyboard = types.InlineKeyboardMarkup()

    diplom_button = types.InlineKeyboardButton('Дипломная работа', callback_data='diplom')
    kurs_button = types.InlineKeyboardButton('Курсовая работа', callback_data='kursovaya')
    practika_button = types.InlineKeyboardButton('Практика(УП/ПП)', callback_data='practika')
    lab_button = types.InlineKeyboardButton('Лабораторная работа', callback_data='laborator')
    another_button = types.InlineKeyboardButton('Другое', callback_data='another')

    select_category_keyboard.add(diplom_button)
    select_category_keyboard.add(kurs_button)
    select_category_keyboard.add(practika_button)
    select_category_keyboard.add(lab_button)
    select_category_keyboard.add(another_button)

    bot.send_message(message.chat.id, '⏳ Выберите категорию работы:', reply_markup=select_category_keyboard)
def select_order_type(message, bot):
    select_order_type_keyboard = types.InlineKeyboardMarkup()

    site_button = types.InlineKeyboardButton('Сайт', callback_data='site')
    desktop_button = types.InlineKeyboardButton('Desktop приложение', callback_data='desktop')
    tgbot_button = types.InlineKeyboardButton('Telegram бот', callback_data='tgbot')
    console_button = types.InlineKeyboardButton('Консольное приложение', callback_data='console')

    select_order_type_keyboard.add(site_button)
    select_order_type_keyboard.add(desktop_button)
    select_order_type_keyboard.add(tgbot_button)
    select_order_type_keyboard.add(console_button)

    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='⏳ Выберите тип работы:', reply_markup=select_order_type_keyboard)

def select_order_deadline(message, bot):
    select_order_deadline_keyboard = types.InlineKeyboardMarkup()

    min_1week_button = types.InlineKeyboardButton("Меньше 1 недели", callback_data='min1week')
    odna_dve_week_button = types.InlineKeyboardButton("1-2 недели", callback_data='odna_dve_week')
    two_week_month_button = types.InlineKeyboardButton("2 недели - 1 месяц", callback_data='two_week_month')
    month_button = types.InlineKeyboardButton("1-2 месяца", callback_data='month-twomonth')
    two_month_more_button = types.InlineKeyboardButton("2 месяца и более" , callback_data='two-month_more')

    select_order_deadline_keyboard.add(min_1week_button)
    select_order_deadline_keyboard.add(odna_dve_week_button)
    select_order_deadline_keyboard.add(two_week_month_button)
    select_order_deadline_keyboard.add(month_button)
    select_order_deadline_keyboard.add(two_month_more_button)

    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='⏳ Выберите сроки выполнения работы:', reply_markup=select_order_deadline_keyboard)

