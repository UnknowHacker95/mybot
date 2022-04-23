import telebot
from nlgu import NLU
API_TOKEN = ''  # TODO: Вставьте сюда API_TOKEN вашего бота
answer =[]
bot = telebot.TeleBot(API_TOKEN)
controller = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Здравствуйте! Дайте мне две темы, а я сделаю вам историю!
Или вы можете дать мне две характеристики вашего персонажа.
Лучше всего, если будет имя. Пример: ролики Папа.
Для начала напишите “Хочу историю”''')
    id = message.from_user.id
    controller[id] = 'start'

@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start')
    first = NLU()
    first.right(user_choice, user_state)
bot.polling()