def insertIntoList(list, item):
    pass

lastNamesList = list()

while True:
    lastName = input("Фамилия ученика: ")

    if lastName == "stop":
        break

    insertIntoList(lastNamesList, lastName)

print("Список учеников:")
for lastName in lastNamesList:
    print("\t" + lastName)