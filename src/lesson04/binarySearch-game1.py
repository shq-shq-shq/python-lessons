maxNum = 1000

print("Загадайте число от 0 до", maxNum - 1, "включительно")

start = 0
end = maxNum
tries = 1

while True:
    if end - start == 1:
        print("Значит, вы загадали", start, ". Угадал за", tries, "попыток!")
        break

    guess = (start + end) // 2

    reply = input("Вы загадали " + str(guess) + "? [<, =, >] ")

    if reply == "<":
        end = guess
        tries += 1

    elif reply == ">":
        start = guess + 1
        tries += 1

    elif reply == "=":
        print("Угадал за", tries, "попыток!")
        break

    else:
        print("Не понял ответа, введите '<', '=' или '>' без кавычек")
