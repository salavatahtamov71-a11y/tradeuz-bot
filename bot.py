import os
import telebot
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("💰 Прибыль / убыток")
    keyboard.add("🛑 Stop Loss", "🎯 Take Profit")
    keyboard.add("⚖️ Risk / Reward")
    keyboard.add("📊 Размер позиции")

    bot.send_message(
        message.chat.id,
        "📈 Добро пожаловать в TradeUZCalcBot!\n\n"
        "Выберите нужный инструмент:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: message.text == "💰 Прибыль / убыток")
def profit(message):
    bot.send_message(
        message.chat.id,
        "💰 Калькулятор прибыли/убытка\n\n"
        "Пока это первая версия бота. "
        "Следующим шагом добавим расчёт."
    )

@bot.message_handler(func=lambda message: True)
def other(message):
    bot.send_message(
        message.chat.id,
        "Выберите инструмент из меню 👇"
    )

bot.infinity_polling()
