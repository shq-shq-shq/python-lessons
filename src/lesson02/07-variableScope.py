x = 0

def a():
    global x
    x = 1

def b():
    global x
    x = 2

print(x)

a()

print(x)

b()

print(x)
