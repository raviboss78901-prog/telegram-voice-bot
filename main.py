from gtts import gTTS
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def tts(message):
    text = message.text
    tts = gTTS(text=text, lang='hi')
    tts.save("voice.mp3")
    audio = open("voice.mp3", "rb")
    bot.send_voice(message.chat.id, audio)
    audio.close()

bot.infinity_polling()
