import telebot

bot = telebot.TeleBot('5158474439:AAFARrFsPG5g6ZKN62lLtrDGMZJUDRIY0iI')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я еще маленький бот и только учусь! Вы можете взять сноуборд (комплект) в прокат сутки - 400Р, выходные -600Р, месяц - 1500Р.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Бот в стадии разработки. Вы можете взять сноуборд (комплект) в прокат сутки - 400Р, выходные -600Р, месяц - 1500Р.")
    else:
        bot.send_message(message.from_user.id, "Мы разарабатываем наш бот: сейчас для заказа комплекта можно написать в @powder_boardrent или прочитать в канале @boardrent_powder. Вы можете взять сноуборд (комплект) в прокат сутки - 400Р, выходные -600Р, месяц - 1500Р.")

bot.polling(none_stop=True, interval=0)