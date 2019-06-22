x = 5

myDictionary = {"Вася" : 11, "Иван" : 14, "Кирилл" : 44}

myList = [1, "Вася", "Иван", "Кирилл", "Иван", "Иван", "Иван"]

mySet = {1, "Вася", "Иван", "Кирилл", "Иван", "Иван", "Иван"}

myTuple = ("Вася", "Иван", "Кирилл")

myScalarString = "Скаляр"

myMultilineString = """Я хочу написать роман.
Не хватит мне одной строки.
Стану знаменитым, как Лев Толстой.
Только не знаю, что писать."""

myScalarNumber = 10.5

for i in myDictionary.items():
    print(i)

x = ['x', 'y']

x.append('z')

x = x + ['z']

y = 'asdfasdf'

x = x + [y]
x.append(y)


class MyIterable:
    def __init__(self):
        self.номерКонфеты = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.номерКонфеты < 10:
            self.номерКонфеты += 1
            return "Конфета " + str(self.номерКонфеты)
        else:
            raise StopIteration

for i in MyIterable():
    print(i)
