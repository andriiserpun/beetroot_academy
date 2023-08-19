from telegram import Bot
from telegram.ext import Updater, CommandHandler
import os


TELEGRAM_BOT_TOKEN = os.environ.get('6553723256:AAFX1vByEhelImArItiF_NXiWEYXeW9azGs')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
updater = Updater(bot=bot, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Django bot.")

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()