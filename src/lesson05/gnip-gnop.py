from graphics import *
from time import sleep
import random

win = GraphWin(title="GNIP GNOP", width=600, height=400)

ball = Circle(Point(win.width / 2, win.height / 2), 10)
ball.setFill("red")
ball.draw(win)

racket = Rectangle(Point(win.width / 2 - 10, win.height - 10), Point(win.width / 2 + 10, win.height - 5))
racket.setFill("black")
racket.draw(win)

scoreText = Text(Point(30, 30), "")
scoreText.setSize(36)
scoreText.setTextColor("green")
scoreText.draw(win)

looserText = Text(Point(win.width / 2, win.height / 2), "LOOSER!")
looserText.setSize(36)
looserText.setTextColor("red")

def updateScore():
    scoreText.setText(str(score))

def setRandomDxDy():
    global dx
    global dy
    dx = random.randint(-11, 9) + 1
    dy = random.randint(3, 10)

score = 0

setRandomDxDy()

while not win.closed:
    mouse = win.getMousePos()

    if 0 < mouse.x < win.width and 0 < mouse.y < win.height:
        racket.moveTopLeft(mouse.x, racket.topLeft.y)

    if ball.topLeft.x < 0 or ball.bottomRight.x > win.width:
        dx = -dx

    if ball.topLeft.y < 0:
        dy = -dy

    if ball.bottomRight.y >= racket.topLeft.y and dy >= 0:
        midX = (ball.topLeft.x + ball.bottomRight.x) / 2
        if racket.topLeft.x <= midX <= racket.bottomRight.x:
            dy = -abs(dy)
            score += 1
            updateScore()

    if ball.topLeft.y > win.height:
        score -= 10
        updateScore()

        looserText.draw(win)
        sleep(0.5)
        looserText.undraw()

        ball.moveTopLeft(random.randint(0, win.width), 1)
        setRandomDxDy()

    ball.move(dx, dy)

    sleep(0.05)
