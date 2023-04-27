import random


class Planet:
    def __init__(self, event):
        self._event = event
        self.res = {
            'version': self._event['version'],
            'session': self._event['session'],
            'session_state': dict(),
            'response': {
                'buttons': [
                    {
                        "title": "К началу🔙",
                        "hide": True
                    },
                    {
                        "title": "Назад к планетам🔙",
                        "hide": True
                    }
                ]
            }
        }
        self.res['session_state']['last_func'] = self.__class__.__name__
        try:
            self.res['session_state']['last_main'] = self._event['state']['session']['last_main']
        except KeyError:
            pass

    def is_it(self) -> bool:
        pass


class Mercury(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Меркурий']
        random.shuffle(self.facts)

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'меркур' in self._event['request']['command']


class Venus(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Венера']

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'венер' in self._event['request']['command']


class Earth(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Земля']

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'земл' in self._event['request']['command']


class Mars(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Марс']

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'марс' in self._event['request']['command']


class Jupiter(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Юпитер']

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'юпитер' in self._event['request']['command']


class Saturn(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Сатурн']

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'сатурн' in self._event['request']['command']


class Uranus(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Уран']

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'уран' in self._event['request']['command']


class Neptune(Planet):
    def __init__(self, event, facts):
        super().__init__(event)
        self.facts = facts['facts']['Нептун']

    def __call__(self):
        try:
            altern = self.facts.pop()
            self.res['response']['text'] = altern[0] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
            self.res['response']['tts'] = altern[1] + '\n Чтобы услышать ещё факт про эту планету, скажи "Ещё"'
        except IndexError:
            self.res['response']['text'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'
            self.res['response']['tts'] = 'Ты уже узнал все факты о этой планете на сегодня, но ты можешь узнать про другие планеты, сказав её название.'

    def is_it(self):
        return 'нептун' in self._event['request']['command']


