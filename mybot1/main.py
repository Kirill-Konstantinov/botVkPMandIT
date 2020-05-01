#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import mems
import prediction
import do
import Sticker
import data

token = data.tok()
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'начать':
        keyboard.add_button('Функции', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Старт', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Закрыть', color=VkKeyboardColor.NEGATIVE)

    elif response == 'привет':
        keyboard.add_button('Функции', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Старт', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Закрыть', color=VkKeyboardColor.NEGATIVE)

    elif response == 'старт':
        keyboard.add_button('Предсказание', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мем', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('!шо поделать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Стикер', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Ясновидящий', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    elif response == 'мем':
        keyboard.add_button('Предсказание', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мем', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('!шо поделать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Стикер', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Ясновидящий', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    elif response == 'предсказание':
        keyboard.add_button('Предсказание', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мем', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('!шо поделать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Стикер', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Ясновидящий', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    elif response == 'стикеры':
        keyboard.add_button('Предсказание', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мем', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('!шо поделать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Стикер', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Ясновидящий', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    elif response == '!шо поделать':
        keyboard.add_button('Предсказание', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мем', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('!шо поделать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Стикер', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Ясновидящий', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    elif response == 'ясновидящий':
        keyboard.add_button('Предсказание', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мем', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('!шо поделать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Стикер', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Ясновидящий', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    elif response == 'назад':
        keyboard.add_button('Функции', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Начать', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Закрыть', color=VkKeyboardColor.NEGATIVE)

    elif response == 'закрыть':
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            keyboard = create_keyboard(response)

            if event.from_user and not (event.from_me):
                if response == 'привет':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': 'Я очень рад с тобой познакомиться, аж сложно сдержать улыбку&#9786;'
                                                  '\n Меня'
                                                  ' зовут бот-ласточка, чтобы узнать, что я умею, нажми на клавишу '
                                                  '"функции", а потом "старт", чтобы я начал развлекать тебя!&#128540;',
                                       'keyboard': keyboard,
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'функции':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': 'Я имею следующие функции:\n\n'
                                                  '&#128519;Ясновидящий: хочешь узнать, насколько % ты сегодня '
                                                  'красив/успешен/выспавшийся и не только? Тогда эта функция для '
                                                  'тебя! Просто спроси меня «Насколько я ...?» и узнай ответ.\n\n'
                                                  '&#128569;Мемы: чтобы получить порцию годных мемов от ПМиИТа, просто '
                                                  'нажми кнопку «Мем» и ты вооружён угаром!\n\n'
                                                  '&#128125;Предсказание: что будет сегодня? А завтра? Узнать об этом '
                                                  'ты сможешь с помощью «предсказаний». Нажми кнопку и твоё будущее '
                                                  'станет явным. \n\n &#128515;!Шо поделать: чтобы узнать, чем тебе '
                                                  'заняться, нажми на !шо поделать и я тебе обязательно подскажу!\n\n '
                                                  '&#128584;Стикерпак: встречаем самые ПМиИТовские стикеры! '
                                                  'Наш кот готов описать твои эмоции/состояние, которое ты узнаёшь, '
                                                  'если выберешь «Стикерпак»\n\n Для получения стикеров ПМиИТа в '
                                                  'телеграме тебе всего лишь нужно:\n\n1. Перейти по нужной ссылке:\n'
                                                  'веб-версия: https://www.web-telegram.ru/#/im?p=@PMandIT_bot \n'
                                                  'приложение: https://teleg.run/PMandIT_bot\n2. '
                                                  'Пройти игру\n3. Получить массу удовольствия и готово! '
                                                  'Стикеры у тебя в руках! &#128521;',
                                       'attachment': 'photo-193491601_457239056',
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'начать':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': 'Я очень рад с тобой познакомиться, аж сложно сдержать улыбку&#9786;'
                                                  '\nМеня зовут бот-ласточка, чтобы узнать, что я умею, нажми на клавишу'
                                                  ' "функции", а потом "старт", чтобы я начал развлекать тебя!&#128540;',
                                       'keyboard': keyboard,
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'старт':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': 'Выбери одну из команд!',
                                       'keyboard': keyboard,
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'назад':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': 'Уже уходишь?&#128148; Или хочешь вспомнить функции?)',
                                       'keyboard': keyboard,
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'закрыть':
                    bye = ['Бип-бип, пока-пока! И вам хорошего, чего-нибудь. Аривуар. Бай. Си ю лэйте. '
                           'Дистанционно пожимаю руку.',
                           'Выключаюсь( Я не прощаюсь! Пока-пока, до встречи! Еще увидимся, пока. Дистанционное пока.']
                    ind = random.randint(0, 1)
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': bye[ind],
                                       'keyboard': keyboard,
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'мем':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'peer_id': event.user_id,
                                       'message': 'Лови мем!',
                                       'attachment': mems.mem(),
                                       'random_id': random.randint(1, 124124141)})

                elif response == 'предсказание':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'peer_id': event.user_id,
                                       'message': prediction.prediction(),
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == '!шо поделать':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'peer_id': event.user_id,
                                       'message': do.whatToDo(),
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'ясновидящий':
                    notes = ['Включаю алгоритмы, вот-вот начнется магия!&#10024;',
                             'Один момент, достану магический шар&#127921;',
                             'Раскладываю карты и зажигаю свечи&#127183;']
                    note = random.randint(0, len(notes)-1)
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'peer_id': event.user_id,
                                       'message': 'Спроси меня «Насколько я ...?» и узнай ответ.\n\n' + notes[note],
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif response == 'стикер':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'peer_id': event.user_id,
                                       'attachment': Sticker.stick(),
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif 'пмиит' in response:
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': 'ПМиИТ - пушка! (они ведь меня создали)',
                                       'random_id': random.randint(-1314141412, +124124141)})

                elif "насколько" in response:
                    lastword = response.split()[-1]
                    prelastword = response.split()[-2]
                    lastword = lastword[:-1]
                    if prelastword.lower() == 'я':
                        vk_session.method('messages.send', {'user_id': event.user_id,
                                                            'message': 'Ты ' + lastword + ' на ' + str(
                                                                random.randint(1, 100)) + '%',
                                                            'random_id': random.randint(-1314141412, +124124141)})

                    elif prelastword.lower() == 'настя' or prelastword.lower() == 'анастасия' or prelastword.lower() == 'настюха':
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id,
                                           'message': "Все Настюхи просто пушка! А одна особенно!&#10084;&#9802;",
                                           'random_id': random.randint(-1314141412, +124124141)})

                    else:
                        vk_session.method('messages.send', {'user_id': event.user_id,
                                                            'message': prelastword.title() + ' ' + lastword + ' на ' + str(
                                                                random.randint(1, 100)) + '%',
                                                            'random_id': random.randint(-1314141412, +124124141)})

                elif 'a' <= response <= 'z':
                    vk_session.method('messages.send', {'user_id': event.user_id,
                                                        'message': 'Извини, я не понимаю бурятский(',
                                                        'random_id': random.randint(-1314141412, +124124141)})

                else:
                    vk_session.method('messages.send', {'user_id': event.user_id,
                                                        'message': 'Прости, но я тебя не понимаю((',
                                                        'random_id': random.randint(-1314141412, +124124141)})

        print('-' * 15)
