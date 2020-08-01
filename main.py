import telebot
import emoji
import config
import re  
import requests  
import json  
from telebot import types
import db
URL = 'https://krot.info/uploads/posts/2019-06/1559743235_sexy-model-woman-ass-gorgeous-pov-from-behind.jpg'
Bot_Token = '1196864922:AAE8M7uLGI9nnyrVg4WG4rQ9qPkvpHROqzk'
bot = telebot.TeleBot(Bot_Token)
Rate = False
@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, "Привет! Этот бот создан для того , чтобы получать различные картинки и обмениваться ими между разными пользователями." + "\U0001F60A")
	button = types.KeyboardButton(text = 'Новый мем' )
	keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard = False, resize_keyboard = True)
	keyboard.add(button)
	bot.send_message(message.from_user.id, 'Мемасик' + '\U0001F3DE' ,reply_markup = keyboard)
	
@bot.message_handler(content_types = ['text'])
def send_photo(message):
	global Rate
	global URL
	if message.text == 'Новый мем':
		#Buttons----------------------------------
		LikeButton = types.InlineKeyboardButton(text = '\U0001F44D', callback_data = 'like')
		DislikeButton = types.InlineKeyboardButton(text = '\U0001F44E', callback_data = 'dislike')
		textButton = types.InlineKeyboardButton(text = 'Оцени мемасик', callback_data = 'None')
		#KeyBoard_init----------------------------
		LikeBoard = types.InlineKeyboardMarkup()
		LikeBoard.add(LikeButton, DislikeButton)
		#LikeBoard.add(textButton)
		bot.send_chat_action(message.chat.id, 'upload_photo')
		URL = config.get_image()
		bot.send_photo(message.chat.id, URL, reply_markup = LikeBoard)
		Rate = True
		db.get_URL(URL)
	
@bot.callback_query_handler(func=lambda call: True)
def choose(call):
	global Rate
	if call.data == 'like' and Rate:
		bot.answer_callback_query(callback_query_id=call.id, text='Не мем, а КАЕФ')
		Rate = False
		db.get_rate(True, URL)
		db.show_DataBase()
	elif call.data == 'dislike' and Rate:
		bot.answer_callback_query(callback_query_id=call.id, text='*звуки баяна*')
		Rate = False
		db.get_rate(False, URL)
		db.show_DataBase()

bot.polling(none_stop = True, interval = 0)
