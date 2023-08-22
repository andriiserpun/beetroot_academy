import random
import requests
import traceback
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters

TOKEN = '6373644159:AAEFSE-zwOATnv1wpt-lgiM4bMNnNnpr6qE'

API_KEY = 'C08P9JY-2D640QB-G550J3G-79REZR8'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я могу показать тебе случайный фильм.')

def random_movie(update: Update, context: CallbackContext) -> None:
    response = requests.get(f'https://kinopoisk.dev/documentation?api_key={API_KEY}')
    data = response.json()
    movies = data['results']
    random_movie = random.choice(movies)

    title = random_movie['title']
    overview = random_movie['overview']
    release_date = random_movie['release_date']

    message = f"Название: {title}\nОписание: {overview}\nДата выхода: {release_date}"
    update.message.reply_text(message)

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Я понимаю только команды /start и /random_movie.")


def main():
    try:
        updater = Updater(token=TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("random_movie", random_movie))
        dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        traceback.print_exc()

if __name__ == '__main__':
    main()

# TOKEN = '6373644159:AAEFSE-zwOATnv1wpt-lgiM4bMNnNnpr6qE'
#

# API_KEY = 'C08P9JY-2D640QB-G550J3G-79REZR8'

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#
#
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')
#
#
# app = ApplicationBuilder().token("6373644159:AAEFSE-zwOATnv1wpt-lgiM4bMNnNnpr6qE").build()
#
# app.add_handler(CommandHandler("hello", hello))
#
# app.run_polling()