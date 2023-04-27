from functions import buttons as final_buts
from functions import NewDialog

buttons = [
    {
        "title": "Да",
        "hide": True
    },
    {
        "title": "Нет",
        "hide": True
    }
]


class QuestSession:
    def __init__(self, event):
        self._event = event
        self.response = {
            'version': self._event['version'],
            'session': self._event['session'],
            'session_state': dict(),
            'response': {
                'end_session': 'false',
                "text": '',
            }
        }
        self.response['session_state']['last_func'] = self.__class__.__name__
        try:
            self.response['session_state']['last_main'] = self.__class__.__name__
        except KeyError:
            pass

    def is_it(self, state) -> bool:
        pass


class NoWhat:
    def __init__(self, event, phrase):
        self._event = event
        self.response = {
            'version': self._event['version'],
            'session': self._event['session'],
            'session_state': dict(),
            'response': {
                'end_session': 'false',
                "text": '',
            }
        }
        self.response['session_state']['last_func'] = self.__class__.__name__
        try:
            self.response['session_state']['last_main'] = self._event['state']['session']['last_main']
        except KeyError:
            pass
        altern = phrase["Back"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = [
            {
                'title': 'В главное меню',
                "hide": True
            },
            {
                "title": "Выход",
                "hide": True
            },
            {
                'title': 'Назад к квесту',
                "hide": True
            }
        ]

    def is_it(self, state) -> bool:
        return 'нет' in self._event['request']['command'] and (
                state in ['Q1K', 'Q1DK', 'Q2K', 'Q2DK', 'Q3DK', 'Q3K', 'Q4K', 'Q4DK', 'Q5K', 'Q5DK', 'Q6K', 'Q6DK',
                          'Q7K', 'Q7DK',
                          'Q8K', 'Q8DK', 'Q9K', 'Q9DK', 'Q10DK', 'Q10K', 'Q11K', 'Q11DK', 'Q12K', 'Q12DK', 'Q13K', 'Q13DK'])


class Q1(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q1"]
        self.response['response']['text'] = altern[0]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response'][
            'tts'] = f'<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/8ee6addd-8e4f-4957-a555-8ba1db2b6c79.opus"> {altern[1]}'
        self.response['response']["card"] = {
                        "type": "BigImage",
                        "image_id": "213044/1dddcbddbb3f3241fa20",
                        "description": self.response['response']['text']
            }


    def is_it(self, state) -> bool:
        return any([i in self._event['request']['command'] for i in
                    ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and state == 'Start'


class Q1DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q1DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('гагарин' in self._event['request']['command']) and state == 'Q1'


class Q1K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q1K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'гагарин' in self._event['request']['command'] and state == 'Q1'


class Q2(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        altern = phrase["Q2"]
        self.response['response']['text'] = altern[0]
        self.response['response'][
            'tts'] = f'{altern[0][:23]} <speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/0f83c01a-7f38-4434-874a-f265668d3e4b.opus"> {altern[0][23:]}'
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "997614/f9bc8fe9edc4b0978a07",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q1K' or state == 'Q1DK')


class Q2DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q2DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('зенит' in self._event['request']['command']) and state == 'Q2'


class Q2K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q2K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'зенит' in self._event['request']['command'] and state == 'Q2'


class Q3(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q3"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "937455/588f6b00616b42ad7117",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q2K' or state == 'Q2DK')


class Q3DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q3DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('бог' in self._event['request']['command']) and state == 'Q3'


class Q3K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q3K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'бог' in self._event['request']['command'] and state == 'Q3'


class Q4(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q4"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response'][
            'tts'] = f'<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/0f83c01a-7f38-4434-874a-f265668d3e4b.opus"> {altern[1]}'
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1540737/808667e08eb74c4f7d55",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q3K' or state == 'Q3DK')


class Q4DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q4DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('сутк' in self._event['request']['command'] or 'день' in self._event['request']['command']) and state == 'Q4'


class Q4K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q4K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return ('сутк' in self._event['request']['command'] or 'день' in self._event['request']['command']) and state == 'Q4'


class Q5(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q5"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response'][
            'tts'] = f'<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/d3fbc6f7-60de-4f20-beeb-44158dcb8fc4.opus"> {altern[1][:302]} <speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/f05ea0bc-38f0-4ba1-8ced-f8a12c3469ba.opus"> {altern[1][302:]}'
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1521359/3b2f4766f3f995078a7f",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q4K' or state == 'Q4DK')


class Q5DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q5DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('серн' in self._event['request']['command']) and state == 'Q5'


class Q5K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q5K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'серн' in self._event['request']['command'] and state == 'Q5'


class Q6(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q6"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1540737/150015ba55fa7856eb4d",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q5K' or state == 'Q5DK')


class Q6DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q6DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "213044/abb7fa78f027153f2616",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return not ('лун' in self._event['request']['command']) and state == 'Q6'


class Q6K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q6K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "213044/abb7fa78f027153f2616",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return 'лун' in self._event['request']['command'] and state == 'Q6'


class Q7DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q7DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('орб' in self._event['request']['command']) and (state == 'Q6K' or state == 'Q6DK')


class Q7K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q7K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'орб' in self._event['request']['command'] and (state == 'Q6K' or state == 'Q6DK')


class Q8(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q8"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = 'Тогда в путь!' + altern[0]
        self.response['response'][
            'tts'] = 'Тогда в путь!' + '<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/0f83c01a-7f38-4434-874a-f265668d3e4b.opus">' + \
                     altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "997614/4af52ebb42f01f6f84f4",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q7K' or state == 'Q7DK')


class Q8DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q8DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1521359/f7aaa6e746e8b3c754a6",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return not ('льд' in self._event['request']['command'] or 'лед' in self._event['request']['command'] or 'лёд' in
                    self._event['request']['command']) and state == 'Q8'


class Q8K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q8K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1521359/f7aaa6e746e8b3c754a6",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return ('льд' in self._event['request']['command'] or 'лед' in self._event['request']['command'] or 'лёд' in
                self._event['request']['command']) and state == 'Q8'


class Q9DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q9DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('олимп' in self._event['request']['command']) and (state == 'Q8K' or state == 'Q8DK')


class Q9K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q9K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'олимп' in self._event['request']['command'] and (state == 'Q8K' or state == 'Q8DK')


class Q10(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q10"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response'][
            'tts'] = '<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/0f83c01a-7f38-4434-874a-f265668d3e4b.opus">' + \
                     altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1521359/7cbcd7f0888873f842f1",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q9K' or state == 'Q9DK')


class Q10DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q10DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('не' in self._event['request']['command']) and state == 'Q10'


class Q10K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q10K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'не' in self._event['request']['command'] and state == 'Q10'


class Q11(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q11"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response'][
            'tts'] = '<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/d3fbc6f7-60de-4f20-beeb-44158dcb8fc4.opus">' + \
                     altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "965417/79a8ad3e305c10dc0241",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q10K' or state == 'Q10DK')


class Q11DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q11DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('гани' in self._event['request']['command']) and state == 'Q11'


class Q11K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q11K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'гани' in self._event['request']['command'] and state == 'Q11'


class Q12(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q12"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response'][
            'tts'] = '<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/0f83c01a-7f38-4434-874a-f265668d3e4b.opus">' + \
                     altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "965417/9406b5a468a2cdbd5a17",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q11K' or state == 'Q11DK')


class Q12DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q12DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('сияние' in self._event['request']['command']) and state == 'Q12'


class Q12K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q12K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'сияние' in self._event['request']['command'] and state == 'Q12'


class Q13(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q13"]
        self.response['response']['buttons'] = [
            {
                "title": "Не знаю",
                "hide": True
            }
        ]
        self.response['response']['text'] = altern[0]
        self.response['response'][
            'tts'] = '<speaker audio="dialogs-upload/fc5d17ba-8675-4c01-bc84-3142afa6e6f0/0f83c01a-7f38-4434-874a-f265668d3e4b.opus">' + \
                     altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1030494/e11136065c540d000024",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q12K' or state == 'Q12DK')


class Q13DK(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q13DK"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return not ('алмаз' in self._event['request']['command']) and state == 'Q13'


class Q13K(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q13K"]
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']['buttons'] = buttons

    def is_it(self, state) -> bool:
        return 'алмаз' in self._event['request']['command'] and state == 'Q13'


class Q14(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        altern = phrase["Q14"]
        self.response['response']['buttons'] = final_buts
        self.response['response']['text'] = altern[0]
        self.response['response']['tts'] = altern[1]
        self.response['response']["card"] = {
            "type": "BigImage",
            "image_id": "1521359/e2caa173a8373aa250fd",
            "description": self.response['response']['text']
        }

    def is_it(self, state) -> bool:
        return any(
            [i in self._event['request']['command'] for i in ('готов', 'поехали', 'вперёд', 'давай', 'да', 'погнали')]) and (
                state == 'Q13K' or state == 'Q13DK')


class ToQwest(QuestSession):
    def __init__(self, event, phrase):
        super().__init__(event)
        self.response['response']['buttons'] = final_buts
        try:
            self.response['response']['text'] = phrase[self._event['state']['session']['last_main']][0]
            self.response['response']['tts'] = phrase[self._event['state']['session']['last_main']][1]
            self.response['session_state']['last_func'] = self._event['state']['session']['last_main']
            self.response['session_state']['last_main'] = self._event['state']['session']['last_main']
            self.response['response']['buttons'] = []
        except:
            self.response = NewDialog(event).response
            self.response['response']['text'] = 'Вы ещё не начинали путешествие. Чтобы это сделать, скажите "Начать". \n' + self.response['response']['text']
            self.response['response']['tts'] = 'Вы ещё не начинали путешествие. Чтобы это сделать, скажите "Начать"' + self.response['response']['tts']

    def is_it(self, state) -> bool:
        return ('шеств' in self._event['request']['command'] or 'квест' in self._event['request']['command']) and (not('заверш' in self._event['request']['command']) and not('закон' in self._event['request']['command']))


