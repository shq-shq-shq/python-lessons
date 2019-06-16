print("Оценки по математике:")

print("Ушат Помоев:", 3)
print("Роман Баранов:", 3)
print("Майя Пчелко:", 3)
print("Наум Приходящий:", 4)
print("Любовь Пожри-Кобыла:", 4)
print("Нина Конина:", 5)
print("")
print("Средняя оценка: " + str((3 + 3 + 3 + 4 + 4 + 5) / 6))
print("")





#
#
# Версия с переменными
#
#

оценкаПомоева = 3
оценкаБаранова = 3
оценкаПчелко = 3
оценкаПриходящего = 4
оценкаПожриКобыла = 4
оценкаКонины = 5
оценкаШироковых = 2

print("Ушат Помоев:", оценкаПомоева)
print("Роман Баранов:", оценкаБаранова)
print("Майя Пчелко:", оценкаПчелко)
print("Наум Приходящий:", оценкаПриходящего)
print("Любовь Пожри-Кобыла:", оценкаПожриКобыла)
print("Нина Конина:", оценкаКонины)
print("")
print("Средняя оценка:", ((оценкаПомоева + оценкаБаранова + оценкаПчелко + оценкаПриходящего + оценкаПожриКобыла + оценкаКонины) / 6))
print("")

#
#
# Версия с массивом
#
#

оценки = [3, 3, 3, 4, 4, 5]

print("Ушат Помоев:", оценки[0])
print("Роман Баранов:", оценки[1])
print("Майя Пчелко:", оценки[2])
print("Наум Приходящий:", оценки[3])
print("Любовь Пожри-Кобыла:", оценки[4])
print("Нина Конина:", оценки[5])
print("")
print("Средняя оценка:", sum(оценки) / len(оценки))
print("")

#
#
# Версия с двумя массивами
#
#

имена = ["Ушат Помоев", "Роман Баранов", "Майя Пчелко", "Наум Приходящий", "Любовь Пожри-Кобыла", "Нина Конина"]
оценки = [3, 3, 3, 4, 4, 5]

print(имена[0], оценки[0])
print(имена[1], оценки[1])
print(имена[2], оценки[2])
print(имена[3], оценки[3])
print(имена[4], оценки[4])
print(имена[5], оценки[5])
print("")
print("Средняя оценка:", sum(оценки) / len(оценки))
print("")

#
#
# Версия с циклом
#
#

имена = ["Ушат Помоев", "Роман Баранов", "Майя Пчелко", "Наум Приходящий", "Любовь Пожри-Кобыла", "Нина Конина"]
оценки = [3, 3, 3, 4, 4, 5]

i = 0
while i < len(оценки):
    print(имена[i], оценки[i])
    i += 1
i = 5

print("")
print("Средняя оценка:", sum(оценки) / len(оценки))
print("")

#
#
# Версия со вложенными массивами
#
#

именаОценки = [["Ушат Помоев", 3], ["Роман Баранов", 3], ["Майя Пчелко", 3],
               ["Наум Приходящий", 4], ["Любовь Пожри-Кобыла", 4], ["Нина Конина", 5]]

i = 0
while i < len(именаОценки):
    print(именаОценки[i][0], именаОценки[i][1])
    i += 1

i = 0
суммаОценок = 0
while i < len(именаОценки):
    суммаОценок += именаОценки[i][1]
    i += 1

print("")
print("Средняя оценка:", суммаОценок / len(именаОценки))
print("")

#
#
# Версия с for
#
#

именаОценки = [["Ушат Помоев", 3], ["Роман Баранов", 3], ["Майя Пчелко", 3],
               ["Наум Приходящий", 4], ["Любовь Пожри-Кобыла", 4], ["Нина Конина", 5]]

i = 0
while i < len(именаОценки):
    print(именаОценки[i][0], именаОценки[i][1])
    i += 1

суммаОценок = 0
for имяОценка in именаОценки:
    суммаОценок += имяОценка[1]

print("")
print("Средняя оценка:", суммаОценок / len(именаОценки))
print("")