import json
import random
from answers import dict_of_answers
from fact import fct
# кнопки "начать", "факты", "помощь", "о навыке", "что ты умеешь", и "выход"
buttons = [
    {
        "title": "Начать ✨",
        "hide": True
    },
    {
        "title": "Факты ✅",
        "hide": True
    },
    {
        "title": "Помощь 🆘",
        "hide": True
    },
    {
        "title": "О навыке 🌌",
        "hide": True
    },
    {
        "title": "Что ты умеешь ❓",
        "hide": True
    },
    {
        "title": "Продолжить путешествие",
        "hide": True
    },
    {
        "title": "Выход 🚪",
        "hide": True
    }
]


# абстрактный класс для классов, через которое идет взаимодействие с пользователем
class Dialog:
    def __init__(self, event):
        self._event = event
        # заготовка для response
        self.response = {
            'version': self._event['version'],
            'session': self._event['session'],
            'session_state': {}
        }
        self.response['session_state']['last_func'] = self.__class__.__name__
        try:
            self.response['session_state']['last_main'] = self._event['state']['session']['last_main']
        except KeyError:
            pass

    # эта функция будет проверять, нужно ли использовать при взаимодействии тот или иной класс
    def is_it(self):
        pass


# класс с начальным сообщением
class NewDialog(Dialog):
    def __init__(self, event, need=None):
        super().__init__(event)
        altern = random.choice(dict_of_answers["Hello"])
        self.response['response'] = {
            'text': altern[0],
            'tts': altern[1],
            'end_session': 'false',
            'buttons': buttons
        }

    def is_it(self, state=None) -> bool:
        return self._event["session"]["new"] or 'меню' in self._event['request']['command']


# класс, для запуска основной диалоговой ветки
class Start(Dialog):
    def __init__(self, event):
        super().__init__(event)
        altern = dict_of_answers["Start"]
        self.response['response'] = {
            'text': altern[0],
            'tts': altern[1],
            'end_session': 'false',
            'buttons': [
                {
                    "title": "К началу 🔙",
                    "hide": True
                },
                {
                    "title": "Готов ✅",
                    "hide": True
                }
            ]
        }
        self.response['response']["card"] = {
                        "type": "BigImage",
                        "image_id": "213044/620b5dec8032cb085edd",
                        "description": self.response['response']['text']
            }

    def is_it(self):
        return any([i in self._event['request']['command'] for i in ['начат', 'погна', 'го', 'старт']]) and self._event['state']['session']['last_func'] in ['NewDialog', 'AboutUs', 'WhatYouCan', 'Help']


# класс, для запуска диалоговой ветки с фактами
class Facts(Dialog):
    def __init__(self, event):
        super().__init__(event)
        altern = random.choice(dict_of_answers["Facts"])
        self.response['response'] = {
            'text': altern[0],
            'tts': altern[1],
            'end_session': 'false',
            'buttons': [
                {
                    "title": "К началу 🔙",
                    "hide": True
                },
                {
                    "title": "Планеты 🌎",
                    "hide": True
                }
            ]
        }

    def is_it(self):
        global fct
        isit = 'факт' in self._event['request']['command']
        return isit


# класс, для выдачи пользователю список команд
class Help(Dialog):
    def __init__(self, event):
        super().__init__(event)
        altern = random.choice(dict_of_answers["Help"])
        self.response['response'] = {
            'text': altern[0],
            'tts': altern[1],
            'end_session': 'false',
            'buttons': buttons
        }

    def is_it(self):
        return 'помо' in self._event['request']['command']


# класс, для выдачи пользователю информации о навыке
class AboutUs(Dialog):
    def __init__(self, event):
        super().__init__(event)
        altern = random.choice(dict_of_answers["About"])
        self.response['response'] = {
            'text': altern[0],
            'tts': altern[1],
            'end_session': 'false',
            'buttons': buttons
        }

    def is_it(self):
        return 'навык' in self._event['request']['command']


# класс, для выдачи пользователю информации, что может навык
class WhatYouCan(Dialog):
    def __init__(self, event):
        super().__init__(event)
        altern = dict_of_answers["WhatYouCan"]
        self.response['response'] = {
            'text': altern[0],
            'tts': altern[1],
            'end_session': 'false',
            'buttons': buttons
        }

    def is_it(self):
        return 'умеешь' in self._event['request']['command']


# класс, для выхода из навыка
class Exit(Dialog):
    def __init__(self, event):
        text = random.choice(dict_of_answers["Bye"])
        super().__init__(event)
        self.response['response'] = {
            'text': text[0],
            'tts': text[1],
            'end_session': 'true',
            'buttons': buttons
        }

    def is_it(self):
        return 'выход' in self._event['request']['command']


# класс, для возвращения в начало работы навыка
class Back(Dialog):
    def __init__(self, event):
        super().__init__(event)
        self.response = NewDialog(event).response

    def is_it(self):
        return 'начал' in self._event['request']['command']


class SunSys(Dialog):
    def __init__(self, event):
        super().__init__(event)
        altern = fct["planets"]
        self.response['response'] = {
            'text': altern[0],
            'tts': altern[1],
            'end_session': 'false',
            "buttons": [
                {
                    "title": "К началу 🔙",
                    "hide": True
                }
            ]
        }

    def is_it(self) -> bool:
        return 'планет' in self._event['request']['command']


