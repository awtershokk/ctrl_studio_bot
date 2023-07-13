import telebot
import os
from dotenv import load_dotenv
from handlers.start_handler import start_handler
from handlers.info_handler import help_handler
from keyboards.main_reply_keyboard import create_reply_keyboard
from keyboards.order_inline_keyboards import select_order_category, select_order_type, select_order_deadline, edit_order
from handlers.сreate_order_handler import choise_order_category,  choise_order_type, choise_order_deadline, last_create_order_message
from handlers.total_order_handler import working_with_order_creation

load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    main_keyboard = create_reply_keyboard()
    start_handler(message, bot, main_keyboard)

@bot.message_handler(commands=['info'])
def handle_help(message):
    help_handler(message, bot)

@bot.message_handler(func=lambda message: message.text == "🛠 Создать заказ")
def handle_create_order(message):
    select_order_category(message, bot)

@bot.callback_query_handler(func=lambda call: call.data in ['diplom', 'kursovaya', 'practika', 'laborator', 'another'])
def handle_select_type(call):
    choise_order_category(call, bot)
    select_order_type(call.message, bot)

@bot.callback_query_handler(func=lambda call: call.data in ['desktop', 'site', 'tgbot', 'console'])
def handle_select_deadline(call):
    choise_order_type(call, bot)
    select_order_deadline(call.message, bot)

@bot.callback_query_handler(func=lambda call: call.data in ['min1week','odna_dve_week','two_week_month','month-twomonth','two-month_more'])
def handle_create_totalmessage(call):
    choise_order_deadline(call, bot)
    last_create_order_message(call, bot)

@bot.callback_query_handler(func=lambda call: call.data == 'create_order')
def handle_create_order(call):
    working_with_order_creation(call, bot)
@bot.callback_query_handler(func=lambda call: call.data == 'edit_order')
def handle_edit_order(call):
    edit_order(call, bot)

bot.polling()
