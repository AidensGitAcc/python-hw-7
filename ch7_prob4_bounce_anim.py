# Chapter 7, Problem 4 — Animated Bouncing Ball (graphics version of Problem 3)
# Uses setCoords so the window height maps to the initial release height.
# The ball is shown at the top of each bounce, then at the ground, until below 1 mm.

from graphics import *
import time

def main():
    win = GraphWin("Bouncing Ball", 400, 600)
    win.setBackground("lightyellow")

    prompt = Text(Point(200, 300), "Release height (m):")
    prompt.draw(win)
    entry = Entry(Point(200, 330), 6)
    entry.draw(win)
    btn = Rectangle(Point(160, 355), Point(240, 380))
    btn.setFill("lightblue")
    btn.draw(win)
    btnLabel = Text(Point(200, 367), "Start")
    btnLabel.draw(win)
    win.getMouse()

    initialHeight = float(entry.getText())

    prompt.undraw()
    entry.undraw()
    btn.undraw()
    btnLabel.undraw()

    win.setCoords(0, 0, 1, initialHeight)

    radius = initialHeight * 0.03
    ball = Circle(Point(0.5, initialHeight), radius)
    ball.setFill("tomato")
    ball.setOutline("darkred")
    ball.draw(win)

    bounceHeight = initialHeight

    while bounceHeight >= 0.001:
        dy = radius - ball.getCenter().getY()
        ball.move(0, dy)
        time.sleep(0.35)

        bounceHeight = bounceHeight * 0.6
        dy = bounceHeight - ball.getCenter().getY()
        ball.move(0, dy)
        time.sleep(0.35)

    dy = radius - ball.getCenter().getY()
    ball.move(0, dy)

    done = Text(Point(0.5, initialHeight * 0.9), "Done! Click to exit.")
    done.draw(win)
    win.getMouse()
    win.close()

main()
