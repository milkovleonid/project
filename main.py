import random

from functions import *
import json
from facts import *
from mainbranch import *
from PhraseAlice import phrase
from fact import problems, fct
from answers import dict_of_answers


# список классов(не основных веток), по которым мы пройдемся, благодаря полиморфизму
start_menu = [NewDialog, Start, Facts, AboutUs, WhatYouCan, Help, Exit, SunSys, Back]
facts_branch = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
main_branch = [Q1, Q1K, Q1DK, Q2, Q2K, Q2DK, Q3, Q3DK, Q3K, Q4, Q4K, Q4DK, Q5, Q5K, Q5DK, Q6, Q6K, Q6DK, Q7K, Q7DK,
               Q8, Q8K, Q8DK, Q9DK, Q9K, Q10, Q10K, Q10DK, Q11, Q11K, Q11DK, Q12, Q12K, Q12DK, Q13, Q13K, Q13DK, Q14, NoWhat, NewDialog, ToQwest]

all_class = dict()
plan = dict()

for i in start_menu:
    all_class[i.__name__] = i
for i in main_branch:
    all_class[i.__name__] = i
for i in facts_branch:
    all_class[i.__name__] = SunSys
for i in facts_branch:
    plan[i.__name__] = i


def smenu(event):
    for i in start_menu:
        example_of_class = i(event)
        if example_of_class.is_it():
            return example_of_class.response


# точка входа
def handler(event: dict, context):
    try:
        global fct

        if smenu(event):
            return smenu(event)

        state = event['state']['session']['last_func']

        # ветка факты
        if state in ['Facts', 'SunSys', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
            for i in facts_branch:
                example_of_class = i(event, fct)
                if example_of_class.is_it():
                    example_of_class()
                    return example_of_class.res
        if 'ещ' in event['request']['command'] and all_class[state] == SunSys:
            example_of_class = plan[state](event, fct)
            example_of_class()
            return example_of_class.res
        # основная ветка
        for i in main_branch:
            example_of_class = i(event, phrase)
            if example_of_class.is_it(state) and example_of_class.response != None:
                return example_of_class.response
        raise BaseException
    except:
        # обработка ошибка
        try:
            res = all_class[state](event).response
            rnd = random.choice(problems)
            res['response']['text'] = rnd[0] + res['response']['text']
            res['response']['tts'] = rnd[1] + res['response']['tts']
            try:
                res['session_state']['last_main'] = event['state']['session']['lastmain']
            except KeyError:
                pass
            return res
        except:
            res = all_class[state](event, phrase).response
            rnd = random.choice(problems)
            res['response']['text'] = rnd[0] + res['response']['text']
            res['response']['tts'] = rnd[1] + res['response']['tts']
            return res

    # если ваще хуйня неведомая происходит, просто начнем с начала (но сессия сохранится)
    res = NewDialog(event).response
    rnd = random.choice(problems)
    res['response']['text'] = rnd[0] + res['response']['text']
    res['response']['tts'] = rnd[1] + res['response']['tts']
    return res
