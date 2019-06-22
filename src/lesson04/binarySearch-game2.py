def guess(start, end, tries):
    if end - start == 1:
        print("Значит, вы загадали", start, ". Угадал за", tries, "попыток!")
        return

    guessNum = (start + end) // 2

    reply = input("Вы загадали " + str(guessNum) + "? [<, =, >] ")

    if reply == "<":
        guess(start, guessNum, tries + 1)
    elif reply == ">":
        guess(guessNum + 1, end, tries + 1)
    elif reply == "=":
        print("Угадал за", tries, "попыток!")
        return
    else:
        print("Не понял ответа, введите '<', '=' или '>' без кавычек")
        guess(start, end, tries)

maxNum = 100

print("Загадайте число от 0 до", maxNum - 1, "включительно")

guess(0, maxNum, 1)
