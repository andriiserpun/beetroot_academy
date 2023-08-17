# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext
#
# # Токен вашего бота (замените на полученный от @BotFather)
# TOKEN = "6553723256:AAFX1vByEhelImArItiF_NXiWEYXeW9azGs"
#
# def main():
#     updater = Updater(token=TOKEN, use_context=True)
#     dispatcher = updater.dispatcher
#
#     # Обработчик команды /start
#     def start(update: Update, context: CallbackContext):
#         update.message.reply_text("Привет! Я бот для фильмов. Используй /add для добавления фильма и /random для получения случайного фильма.")
#
#     start_handler = CommandHandler("start", start)
#     dispatcher.add_handler(start_handler)
#
#     # Обработчик команды /add
#     def add_movie(update: Update, context: CallbackContext):
#         update.message.reply_text("Отправьте мне название фильма:")
#         return "name"
#
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler('add', add_movie)],
#         states={
#             "name": [MessageHandler(Filters.text, get_name)],
#             "year": [MessageHandler(Filters.text, get_year)],
#             "country": [MessageHandler(Filters.text, get_country)],
#             "comment": [MessageHandler(Filters.text, get_comment)],
#         },
#         fallbacks=[],
#     )
#
#     dispatcher.add_handler(conv_handler)
#
#     # ... (ваш ConversationHandler)
#
#     # Обработчик команды /random
#     def random_movie(update: Update, context: CallbackContext):
#         random_movie = get_random_movie()
#
#         if random_movie:
#             message = f"Случайный фильм:\nНазвание: {random_movie.name}\nГод выпуска: {random_movie.year}\nСтрана: {random_movie.country}\nКомментарий: {random_movie.comment}"
#         else:
#             message = "Список фильмов пуст."
#
#         update.message.reply_text(message)
#
#     random_handler = CommandHandler("random", random_movie)
#     dispatcher.add_handler(random_handler)
#
#     # Обработчик для всех текстовых сообщений
#     def handle_text_message(update: Update, context: CallbackContext):
#         text = update.message.text
#         update.message.reply_text(f"Вы сказали: {text}")
#
#     text_handler = MessageHandler(Filters.text, handle_text_message)
#     dispatcher.add_handler(text_handler)
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == "__main__":
#     main()













