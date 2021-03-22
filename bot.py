import telebot
import config_firstBot

bot = telebot.TeleBot(config_firstBot.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)