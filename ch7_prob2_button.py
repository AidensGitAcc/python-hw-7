# Chapter 7, Problem 2 - "Buttony" Button (based on Supplemental Ch 5, Problem 4)
# Adds an inButton function so clicks are only accepted inside the button region.

from graphics import *

def inButton(click, button):
    p1 = button.getP1()
    p2 = button.getP2()
    if p1.getX() < p2.getX():
        xMin = p1.getX()
        xMax = p2.getX()
    else:
        xMin = p2.getX()
        xMax = p1.getX()
    if p1.getY() < p2.getY():
        yMin = p1.getY()
        yMax = p2.getY()
    else:
        yMin = p2.getY()
        yMax = p1.getY()

    if click.getX() >= xMin and click.getX() <= xMax and click.getY() >= yMin and click.getY() <= yMax:
        return True
    else:
        return False

def main():
    win = GraphWin("Buttony Button", 400, 300)
    win.setBackground("white")

    button = Rectangle(Point(150, 110), Point(250, 160))
    button.setFill("lightblue")
    button.setOutline("navy")
    button.setWidth(2)
    button.draw(win)

    btnLabel = Text(Point(200, 135), "Click Me!")
    btnLabel.setStyle("bold")
    btnLabel.draw(win)

    prompt = Text(Point(200, 50), "Please click the button.")
    prompt.draw(win)

    clickedInButton = False
    while not clickedInButton:
        click = win.getMouse()
        clickedInButton = inButton(click, button)
        if not clickedInButton:
            prompt.setText("Click INSIDE the button!")

    button.setFill("lightgreen")
    prompt.setText("Button clicked! Click anywhere to exit.")
    win.getMouse()
    win.close()

main()
