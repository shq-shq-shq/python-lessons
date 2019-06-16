x = 0
y = 0


def up():
    global y
    y += 1

def down():
    global y
    y -= 1

def left():
    global x
    x -= 1

def right():
    global x
    x += 1


right()
right()
right()
up()
left()
down()
up()


print(x, y)