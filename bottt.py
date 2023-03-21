import telebot
from telebot import types


bot = telebot.TeleBot()

state = {}
questions = {
    "question1": "Вопрос1",
    "question2": "Вопрос1",
    "question3": "Вопрос1",
    "question4": "Вопрос1",
    "question5": "Вопрос1",
    "question6": "Вопрос1"
    }

answer = '********'
secret_answer = 54.72559
user_answered = {}
users_answers = {}
user_states = {}


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет. Готов найти свой подарок? \nТебе нужно ответить на все вопросы викторины и получить ответ из 8 символов. Если запутаешься пиши /help'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("Да, я")
    no = types.KeyboardButton("Нет")

    markup.add(yes, no)

    bot.send_message(message.chat.id,
                     mess,
                     parse_mode='html',
                     reply_markup=markup)
    user_states[message.chat.id] = "default"
    users_answers[message.chat.id] = '********'
    user_answered[message.chat.id] = []


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Не смогли смириться с поражением')
    bot.send_message(message.chat.id, 'И куда вас это привело')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("Да, я")
    no = types.KeyboardButton("Нет")
    markup.add(yes, no)

    start(message)


@bot.message_handler(content_types=['text'])
def quiz(message):
    global users_answers
    try:
        if message.text == 'Да, я':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            bot.send_message(message.chat.id, 'The battle begins', reply_markup=markup)
            user_states[message.chat.id] = "quiz"

        elif message.text == 'Нет':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            bot.send_message(message.chat.id, 'Пидора ответ. Поехали', reply_markup=markup)
            user_states[message.chat.id] = "quiz"

        #Вопросы
        elif message.text == 'Дота за 300' and user_states[message.chat.id] == 'quiz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ans1 = types.KeyboardButton("54")
            ans2 = types.KeyboardButton("52")
            ans3 = types.KeyboardButton("104")
            ans4 = types.KeyboardButton("102")
            markup.add(ans1, ans2, ans3, ans4, row_width=2)
            bot.send_message(message.chat.id,
                             'Сколько получится стоимость_сентри + максимальное_количество_обсов_в_лавке = ?',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest1"

        elif message.text == 'Дота за 500' and user_states[message.chat.id] == 'quiz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ans1 = types.KeyboardButton("4")
            ans2 = types.KeyboardButton("5")
            ans3 = types.KeyboardButton("6")
            ans4 = types.KeyboardButton("7")
            markup.add(ans1, ans2, ans3, ans4, row_width=2)
            bot.send_message(message.chat.id,
                             'Сколько секунд длится Frost Shield на первом уровне прокачки?',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest2"

        elif message.text == 'Дота за 1000' and user_states[message.chat.id] == 'quiz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ans1 = types.KeyboardButton("1 и 3")
            ans2 = types.KeyboardButton("2 и 1")
            ans3 = types.KeyboardButton("1 и 2")
            ans4 = types.KeyboardButton("2 и 3")
            markup.add(ans1, ans2, ans3, ans4, row_width=2)
            bot.send_message(message.chat.id,
                             'Дединсайдик?? Сколько оборотов должен сделать враг в еуле, чтобы кастануть реквием без аркейн блинка и с ним? Ответ соотвественно: ',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest3"

        elif message.text == 'Жиза за 300' and user_states[message.chat.id] == 'quiz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ans1 = types.KeyboardButton("Голубой")
            ans2 = types.KeyboardButton("Красный")
            ans3 = types.KeyboardButton("Желтый")
            ans4 = types.KeyboardButton("Зеленый")
            markup.add(ans1, ans2, ans3, ans4, row_width=2)
            bot.send_message(message.chat.id,
                             'iPhone XR какого цвета нельзя найти: ',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest4"

        elif message.text == 'Жиза за 500' and user_states[message.chat.id] == 'quiz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ans1 = types.KeyboardButton("8 24 137")
            ans2 = types.KeyboardButton("8 25 173")
            ans3 = types.KeyboardButton("3 25 137")
            ans4 = types.KeyboardButton("8 25 137")
            markup.add(ans1, ans2, ans3, ans4, row_width=2)
            bot.send_message(message.chat.id,
                             'Какие номера квартир у твоих сегодняшних гостей? ',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest5"

        elif message.text == 'Жиза за 1000' and user_states[message.chat.id] == 'quiz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ans1 = types.KeyboardButton("До 18 отвечаю")
            ans2 = types.KeyboardButton("До 20 сто проц")
            ans3 = types.KeyboardButton("До 22 (надеемся)")
            ans4 = types.KeyboardButton("Extra")
            markup.add(ans1, ans2, ans3, ans4, row_width=2)
            bot.send_message(message.chat.id,
                             'Когда? ',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest6"

        elif message.text == 'Жиза за 1000' and user_states[message.chat.id] == 'quiz':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ans1 = types.KeyboardButton("До 18 отвечаю")
            ans2 = types.KeyboardButton("До 20 сто проц")
            ans3 = types.KeyboardButton("До 22 (надеемся)")
            ans4 = types.KeyboardButton("Extra")
            markup.add(ans1, ans2, ans3, ans4, row_width=2)
            bot.send_message(message.chat.id,
                             'Когда? ',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest6"

        elif message.text == 'Вопрос для ИБэшника' and user_states[message.chat.id] == 'quiz':
            if 'quest1' in user_answered[message.chat.id] and 'quest2' in user_answered[message.chat.id] and 'quest3' in user_answered[message.chat.id] and 'quest4' in user_answered[message.chat.id] and 'quest5' in user_answered[message.chat.id] and 'quest6' in user_answered[message.chat.id]:
                markup = types.ReplyKeyboardRemove()
                bot.send_message(message.chat.id,
                             'Вселенная перешла на новый (старый) алгоритм шифрования. Теперь все желания нужно шифровать перед отправкой. Скажи вселенной "Я обязательно поебусь" с помощью хэша SHA256',
                             reply_markup = markup)
                user_states[message.chat.id] = "quest7"
            else:
                bot.send_message(message.chat.id,
                                 f'Сначала ответь на другие вопросы')

        #Ответы
        elif message.text == '54' and user_states[message.chat.id] == "quest1":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            users_answers[message.chat.id] = str(54) + users_answers[message.chat.id][2:]
            bot.send_message(message.chat.id,
                             f'Ладно, это было легко. \nДержи подсказку: {users_answers[message.chat.id]}',
                             reply_markup=markup)
            user_states[message.chat.id] = "quiz"
            user_answered[message.chat.id].append('quest1')

        elif message.text == '5' and user_states[message.chat.id] == "quest2":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            users_answers[message.chat.id] = users_answers[message.chat.id][:5] + str(5) + users_answers[message.chat.id][6:]
            bot.send_message(message.chat.id,
                             f'Гений Лича, сразу видно. А вот и подсказка {users_answers[message.chat.id]}',
                             reply_markup=markup)
            user_states[message.chat.id] = "quiz"
            user_answered[message.chat.id].append('quest2')

        elif message.text == '1 и 2' and user_states[message.chat.id] == "quest3":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            users_answers[message.chat.id] = users_answers[message.chat.id][:7] + str(9)
            bot.send_message(message.chat.id,
                             f'Le le let me die. Держи бонус {users_answers[message.chat.id]}',
                             reply_markup=markup)
            user_states[message.chat.id] = "quiz"
            user_answered[message.chat.id].append('quest3')

        elif message.text == 'Голубой' and user_states[message.chat.id] == "quest4":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            users_answers[message.chat.id] = users_answers[message.chat.id][:3] + str(7) + users_answers[message.chat.id][4:]
            bot.send_message(message.chat.id,
                             f'В следующий раз сам пойдешь искать. Пришел кешбек {users_answers[message.chat.id]}',
                             reply_markup=markup)
            user_states[message.chat.id] = "quiz"
            user_answered[message.chat.id].append('quest4')

        elif message.text == '8 25 137' and user_states[message.chat.id] == "quest5":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            users_answers[message.chat.id] = users_answers[message.chat.id][:2] + '.' + users_answers[message.chat.id][3:]
            bot.send_message(message.chat.id,
                             f'Мы сами не знали ответ. Это тебе {users_answers[message.chat.id]}',
                             reply_markup=markup)
            user_states[message.chat.id] = "quiz"
            user_answered[message.chat.id].append('quest5')

        elif message.text == 'До 22 (надеемся)' and user_states[message.chat.id] == "quest6":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Да")
            quest2 = types.KeyboardButton("Да")
            markup.add(quest1, quest2, row_width=2)
            users_answers[message.chat.id] = users_answers[message.chat.id][:4] + str(2) + users_answers[message.chat.id][5:]
            bot.send_message(message.chat.id,
                             f'Точно-точно?',
                             reply_markup=markup)
            user_states[message.chat.id] = "quest6_extra"

        elif message.text == 'Да' and user_states[message.chat.id] == "quest6_extra":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            quest1 = types.KeyboardButton("Дота за 300")
            quest2 = types.KeyboardButton("Дота за 500")
            quest3 = types.KeyboardButton("Дота за 1000")
            quest4 = types.KeyboardButton("Жиза за 300")
            quest5 = types.KeyboardButton("Жиза за 500")
            quest6 = types.KeyboardButton("Жиза за 1000")
            quest7 = types.KeyboardButton("Вопрос для ИБэшника")
            markup.add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, row_width=3)
            bot.send_message(message.chat.id,
                             f'Верим на слово. Еще кусочек {users_answers[message.chat.id]}',
                             reply_markup=markup)
            user_states[message.chat.id] = "quiz"
            user_answered[message.chat.id].append('quest6')

        elif message.text.lower() == 'da41e71705709afbb5e0aa8b89aa53faa9923b902c171cb62ac22d56732f9de2' and user_states[message.chat.id] == "quest7":
            markup = types.ReplyKeyboardRemove()
            users_answers[message.chat.id] = users_answers[message.chat.id][:6] + str(5) + users_answers[message.chat.id][7]
            bot.send_message(message.chat.id,
                             f'Ты прошел катакомбы. Получить сокровищницу ты сможешь, используя эти секретные данные. \n{users_answers[message.chat.id]}\nНадеюсь ты знаешь, что делать',
                             reply_markup=markup)
            user_states[message.chat.id] = "end"
            user_answered[message.chat.id].append('quest7')

        elif message.text != '54' and user_states[message.chat.id] == "quest1":
            bot.send_message(message.chat.id,
                             f'Давай чуть-чуть подумаем')

        elif message.text != '5' and user_states[message.chat.id] == "quest2":
            bot.send_message(message.chat.id,
                             f'Ты столько играл и не запомнил??')

        elif message.text != '1 и 2' and user_states[message.chat.id] == "quest3":
            bot.send_message(message.chat.id,
                             f'Гули недовольны тобой')

        elif message.text != 'Голубой' and user_states[message.chat.id] == "quest4":
            bot.send_message(message.chat.id,
                             f'Гаджет мой любимый магазин')

        elif message.text != '8 25 137' and user_states[message.chat.id] == "quest5":
            bot.send_message(message.chat.id,
                             f'В гости больше не зовем')

        elif message.text != 'До 22 (надеемся)' and user_states[message.chat.id] == "quest6":
            bot.send_message(message.chat.id,
                             f'Мимо вопрос')

        elif message.text != 'Да' and user_states[message.chat.id] == "quest6_extra":
            bot.send_message(message.chat.id,
                             f'Там другой ответ')

        elif message.text != 'da41e71705709afbb5e0aa8b89aa53faa9923b902c171cb62ac22d56732f9de2' and user_states[message.chat.id] == "quest7":
            bot.send_message(message.chat.id,
                             f'Попробуй еще раз...')

        elif user_states[message.chat.id] == "end":
            bot.send_message(message.chat.id,
                             f'Ты прошел тест. Твоя подсказка {users_answers[message.chat.id]}')

        else:
            bot.send_message(message.chat.id, 'Кнопки для тебя шутка?')
            user_states[message.chat.id] = 'quiz'
    except:
        user_states[message.chat.id] = 'default'
        bot.send_message(message.chat.id, 'Произошла ошибка. Начни сначала. \n/start')


bot.polling(none_stop=True)