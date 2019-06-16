from simpleWebServer import SimpleWebServer
import random

answers = ['Да', "Нет", "Попробуйте ещё раз", "Спроси у мамы"]


def getContent(path):
    return random.choice(answers)

SimpleWebServer().serve(8088, getContent)
