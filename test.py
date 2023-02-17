
import telebot
from telebot import types # для указание типов
# import config

bot = telebot.TeleBot('6091779298:AAHnD3kh4r8BKOCXQiQM2QUL3-2DLM-zzIk')

@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    print(message)
    if message.text == "Главное меню" or message.text =="/start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Архитектура предприятий")
        btn2 = types.KeyboardButton("Гибкие технологии Agile")
        btn3 = types.KeyboardButton("Интеллектуальный анализ данных")
        btn4 = types.KeyboardButton("Информационная безопасность IT инфраструктуры")
        btn5 = types.KeyboardButton("Информационные системы и информационно-коммуникационные технологии управления бизнесом")
        btn6 = types.KeyboardButton("Проектирование бизнес-процессов")
        btn7 = types.KeyboardButton("Проектная деятельность")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери предмет, который тебе по душе".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Архитектура предприятий"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить список файлов")
        btn2 = types.KeyboardButton("Добавить файл")
        back = types.KeyboardButton("Главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Тьютор: Потехина Елена Витальевна", reply_markup=markup)
    
    elif(message.text == "Гибкие технологии Agile"):
        ma = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить список файлов")
        btn2 = types.KeyboardButton("Добавить файл")
        back = types.KeyboardButton("Главное меню")
        ma.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Тьютор: Кузнецов Андрей Сергеевич",reply_markup=ma)
    
    elif(message.text == "Интеллектуальный анализ данных"):
        q = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить список файлов")
        btn2 = types.KeyboardButton("Добавить файл")
        back = types.KeyboardButton("Главное меню")
        q.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Тьютор: Романова Елена Юрьевна",reply_markup=q)

    elif(message.text == "Информационная безопасность IT инфраструктуры"):
        w = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить список файлов")
        btn2 = types.KeyboardButton("Добавить файл")
        back = types.KeyboardButton("Главное меню")
        w.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Тьютор: Мельникова Елена Анатольевна, Скороходов Сергей Вадимович",reply_markup=w)

    elif(message.text == "Информационные системы и информационно-коммуникационные технологии управления бизнесом"):
        e = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить список файлов")
        btn2 = types.KeyboardButton("Добавить файл")
        back = types.KeyboardButton("Главное меню")
        e.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Тьютор: Романова Елена Юрьевна",reply_markup=e)
    
    elif(message.text == "Проектирование бизнес-процессов"):
        r = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить список файлов")
        btn2 = types.KeyboardButton("Добавить файл")
        back = types.KeyboardButton("Главное меню")
        r.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Тьютор: Блинов Александр Олегович",reply_markup=r)

    elif(message.text == "Проектная деятельность"):
        t = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Получить список файлов")
        btn2 = types.KeyboardButton("Добавить файл")
        back = types.KeyboardButton("Главное меню")
        t.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Тьютор: Потехина Елена Витальевна",reply_markup=t)
    
    elif message.text == "Главное меню" or message.text =="/start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Архитектура предприятий")
        btn2 = types.KeyboardButton("Гибкие технологии Agile")
        btn3 = types.KeyboardButton("Интеллектуальный анализ данных")
        btn4 = types.KeyboardButton("Информационная безопасность IT инфраструктуры")
        btn5 = types.KeyboardButton("Информационные системы и информационно-коммуникационные технологии управления бизнесом")
        btn6 = types.KeyboardButton("Проектирование бизнес-процессов")
        btn7 = types.KeyboardButton("Проектная деятельность")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери предмет, который тебе по душе".format(message.from_user), reply_markup=markup)
    


    # elif(message.text == "Гибкие технологии Agile"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn1 = types.KeyboardButton("Как меня зовут?")
    #     btn2 = types.KeyboardButton("Что я могу?")
    #     back = types.KeyboardButton("Вернуться в главное меню")
    #     markup.add(btn1, btn2, back)
    #     bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
#     elif(message.text == "Как меня зовут?"):
#         bot.send_message(message.chat.id, "У меня нет имени..")
    
#     elif message.text == "Что я могу?":
#         bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
#     elif (message.text == "Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("👋 Поздороваться")
#         button2 = types.KeyboardButton("❓ Задать вопрос")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)