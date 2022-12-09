import telebot
from telebot import types
from game import WordGame
from tb_token import get_token

user_game = {}  # создание словаря с пользователями и персональными играми к ним

token = get_token()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    game_btn = types.KeyboardButton('Игра в слова')
    new_game_btn = types.KeyboardButton('Новая игра')
    markup.add(game_btn, new_game_btn)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}', reply_markup=markup)


# @bot.message_handler(commands=['game'])
# def start_game(message):
#     bot.send_message(message.chat.id, 'Введите слово')
#
#
# @bot.message_handler(commands=['new_game'])
# def start_game(message):
#     game.new_game()
#     bot.send_message(message.chat.id, 'Введите слово')
#

@bot.message_handler(content_types=['text'])
def user_word(message):
    if message.text == 'Игра в слова':
        user_game[message.from_user.id] = WordGame() # добавление пользователя в словарь
        bot.send_message(message.chat.id, 'Введите слово')
    elif message.text == 'Новая игра':
        user_game[message.from_user.id] = WordGame() # добавление пользователя в словарь, если он не нажал кнопку "игра в слова"
        user_game[message.from_user.id].new_game() #новая игра
        bot.send_message(message.chat.id, 'Введите слово')
    else:
        answer = user_game[message.from_user.id].progress(message.text)
        bot.send_message(message.chat.id, answer)


bot.infinity_polling()
