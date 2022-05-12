import telebot
from nlgu import NLU
from nlgu import text
from nlgu import illustrachiya
API_TOKEN = ''  # TODO: Вставьте сюда API_TOKEN вашего бота
answer =[]
bot = telebot.TeleBot(API_TOKEN)
controller = {}
il = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Здравствуйте! Дайте мне две темы, а я сделаю вам историю!
Или вы можете дать мне две характеристики вашего персонажа.
Лучше всего, если будет имя. Пример: ролики Папа.
Для начала напишите “Хочу историю”''')
    id = message.from_user.id
    controller[id] = 'start'
    il[id] = 0

@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start')
    first = NLU()
    if(user_state == 'start'):
        if(first.right(user_choice,user_state) != 1):
            bot.send_message(message.chat.id, "Напишите 'Хочу историю' ")
        else:
            controller[user_id] = 'vibor'
            bot.send_message(message.chat.id, "Вы хотите иллюстрацию к своей истории?")
    if(user_state == 'start_t'):
        if(user_choice == 'Да'):
            controller[user_id] = 'start'
        else:
            bot.send_message(message.chat.id, "Ну пока! Если что, то напишите 'Хочу историю'")
            controller[user_id] = 'start'
    if (user_state == 'vibor'):
        if (first.right(user_choice, user_state) == 'Error'):
            bot.send_message(message.chat.id, "Ответьте нормально на вопрос")
        elif (first.right(user_choice, user_state) == 1):
            il[user_id] = 1
            controller[user_id] = 'tema'
            bot.send_message(message.chat.id, "Введите темы")
        else:
            controller[user_id] = 'tema'
            bot.send_message(message.chat.id, "Введите темы")
    if(user_state == 'tema'):
        textix = first.right(user_choice, user_state)
        history = text(textix)
        bot.send_message(message.chat.id, history)
        if (il[user_id] == 1):
            bot.send_photo(message.chat.id, illustrachiya(textix[0]))
        bot.send_message(message.chat.id, "Хотите еще историю?")
        controller[user_id] = 'start_t'
        il[user_id] = 0
    else:
        pass
@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Красиво конечно, но давайте по делу''')

@bot.message_handler(content_types=['video'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Красиво конечно, но давайте по делу''')

@bot.message_handler(content_types=['photo'])
def start_message(message):
    bot.send_message(message.chat.id,
'''.....''')
    bot.send_message(message.chat.id, "Вы меня не любите(((ТТ(((")
bot.polling()

@bot.message_handler(content_types=['document'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Не игнорирую МЕНЯ!!!!''')

@bot.message_handler(content_types=['audio'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Не игнорирую МЕНЯ!!!!''')

bot.polling()