import telebot

bot = telebot.TeleBot("7532474924:AAHsGMNEDhwD0uEMq8FW9Zo2LUbVoYn3EFE", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Zafar janob, sizmi bratan: {message.from_user.username}")

@bot.message_handler(commands=['salom'])
def send_eee(message):
    bot.reply_to(message, "salam palalam!!!")



bot.infinity_polling()
