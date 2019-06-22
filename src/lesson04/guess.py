def guess(minValue, maxValue, tries):
    if minValue == maxValue:
        print("Это точно", minValue, "! Угадано за", tries, "попыток")
        return

    value = (minValue + maxValue) // 2

    reply = input("Число " + str(value) + "? [<,=,>] ")

    if reply == "<":
        # minValue..value - 1
        guess(minValue, value - 1, tries + 1)
    elif reply == ">":
        guess(value + 1, maxValue, tries + 1)
    elif reply == "=":
        print("Ура! Угадали за", tries, "попыток!")
    else:
        print("Мы не уверены, что тебя поняли")
        guess(minValue, maxValue, tries)

guess(1, 100, 1)