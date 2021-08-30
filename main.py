import telebot
import config
import action
import connect
import time, datetime
import threading
from telebot import util, types
from telebot import types

TELEGRAM_TOKEN = config.token

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# chat_id = '-1001533838311'
numbers = ['89805471561', '232525']
# Функция для инсерта нового пула номеров
# result = action.insertNewNums(connection=connect.getConnection(), numbers=numbers)
# Функция для получения номера
# result = action.getNum(connection=connect.getConnection())
# print(result)
#
# @bot.message_handler(commands=['me'])
# def send_user_data(message):
#     user = message.from_user
#     text = 'User:\n<code>{0}</code>'.format(user)
#     # if the command has sent in a group get and display status and other information
#     # about the command sender
#     if message.chat.id < 0:
#         chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
#         text += '\n\nChat member:\n<code>{0}</code>'.format(chat_member)
#     bot.send_message(message.chat.id, text, parse_mode='HTML')
#
#
# # Get and display information about the bot
# @bot.message_handler(commands=['bot'])
# def send_getme(message):
#     me = bot.get_me()
#     text = '<code>' + str(me) + '</code>'
#     bot.send_message(message.chat.id, text, parse_mode='HTML')
#
#
# @bot.message_handler(commands=["id"])  # Получить ID чата при отправке сообщения /id
# def chat_id(message):
#     my_chat_id = int(message.chat.id)
#     bot.send_message(message.chat.id, my_chat_id)
#
#
# # get and display information about the chat
# # @bot.message_handler(commands=['chat'])
# # def send_chat_data(message):
# #     chat = message.chat
# #     text = '<code>' + str(chat) + '</code>'
# #     bot.send_message(message.chat.id, text, parse_mode='HTML')
# #
# #
# #
# #
# # def tic_tac():
# #     i = 0
# #
# #     while True:
# #
# #         this_moment = datetime.datetime.now()
# #
# #         # Executes each 60 secondss
# #         if ((i % 60) == 0):
# #             if chat_id:
# #                 bot.send_message(chat_id, "Hello! How are you?")
# #
# #         # Check if it is 12:00:00; if it is true sends the message
# #         if this_moment.hour == 12 and this_moment.minute == 0 and this_moment.second == 0:
# #             if chat_id:
# #                 bot.send_message(chat_id, "It is the noon!")
# #
# #         i += 1
# #         time.sleep(1)
#
#
# # Needs to be started to know the chat id to send messages
# @bot.message_handler(content_types=['text'])
# def save_chat_id(message):
#     # global chat_id
#     # chat_id = message.chat.id
#     chat_id = int(985596404)
#     bot.send_message(chat_id, message.text)
#
#
# @bot.message_handler(commands=['setTitle'])
# def preSetTitle(message):
#     global chat_id
#     bot.send_message(chat_id, 'На какой сменим?')
#     # bot.register_next_step_handler(message, setTitle)
#     print(bot.register_next_step_handler(message, setTitle))
#
#
# def setTitle(text):
#     bot.set_chat_title(chat_id, text.text)
#
#
# # timThr = threading.Thread(target=tic_tac)
# # timThr.start()
# bot.polling(none_stop=True)
