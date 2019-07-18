from graphics import *
from time import sleep
import random

win = GraphWin(title="GNIP GNOP", width=600, height=400)

separator = Line(Point(win.width / 2, 0), Point(win.width / 2, win.height))
# separator.setDash(4, 4)
separator.draw(win)

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
    dx = random.randint(-20, 20)
    if abs(dx) < 1:
        dx = 1
    dy = random.randint(3, 10)

score = 0

setRandomDxDy()

racketDx = 0
offset = 0
offsetSum = 0

while not win.closed:
    #mouse = win.getMousePos()

    #if 0 < mouse.x < win.width and 0 < mouse.y < win.height:
    #    racket.moveTopLeft(mouse.x, racket.topLeft.y)

    oldOffset = offset
    offset = ball.getCenter().x - racket.getCenter().x
    offsetSum += offset

    force = 0.18 * offset + 0.1 * offsetSum + 0.5 * (offset - oldOffset)

    racketDx += force * random.uniform(0.8, 1.2)

    racket.move(racketDx, 0)

    if racket.topLeft.x < 0:
        racket.move(-racket.topLeft.x, 0)
        racketDx = 0

    if racket.bottomRight.x > win.width:
        racket.move(win.width - racket.bottomRight.x, 0)
        racketDx = 0

    if ball.topLeft.x < 0 or ball.bottomRight.x > win.width:
        dx = -dx

    if ball.topLeft.y < 0:
        dy = -dy

    if ball.bottomRight.y >= racket.topLeft.y and dy >= 0:
        midX = (ball.topLeft.x + ball.bottomRight.x) / 2
        if racket.topLeft.x <= midX <= racket.bottomRight.x:
            dy = -abs(dy)
            # dx -= racketDx / 2
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
        racketDx = 0

    ball.move(dx, dy)

    sleep(0.05)
