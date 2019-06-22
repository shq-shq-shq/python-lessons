def hanoi(fromRod, toRod, auxRod, count):
    if count == 1:
        print("Кольцо", count, "с", fromRod, "на", toRod)
    else:
        hanoi(fromRod, auxRod, toRod, count - 1)
        print("Кольцо", count, "с", fromRod, "на", toRod)
        hanoi(auxRod, toRod, fromRod, count - 1)

hanoi("A", "B", "C", 3)

# Hanoi towers online:
# https://www.mathsisfun.com/games/towerofhanoi.html
