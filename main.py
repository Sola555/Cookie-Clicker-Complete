import turtle
import os
wn = turtle.Screen()
wn.setup(width=1000, height=1000)
cookie = turtle.Turtle()
cookie.shape('circle')

cookie.shapesize(stretch_wid=5,stretch_len=5)
cookie.color('brown')
cookie.penup()
cookie.goto(0,-50)
global clicks
clicks = 0
global gain
gain = 1

def add_click(x, y):
    global clicks
    clicks = clicks + gain
    pen.clear()
    pen.write("Clicks = {}".format(clicks), align="center", font=("Courier", 24, "normal"))
#cookie clicking
cookie.onclick(add_click)
#farm
farm = turtle.Turtle()
farm.penup()
farm.hideturtle
farm.goto(0,50)
wn.listen()
#The pen is the label that tells you how many clicks
pen = turtle.Turtle()
pen.hideturtle()
#variable for farm level
farming = 0

def farmer():
    global clicks
    if (clicks > 50):
        global farming
        farming = farming+1
        clicks-=50
        global gain
        gain = gain * 2
        farm.clear()
        farm.goto(0,220)
        farm.write("Farm level: {}".format(farming), align="center", font=("Courier", 24, "normal"))
    else:
        print("You need more than 20 clicks to buy a farm.")

printings = 0
#PRINTER
def printingaa():
    global clicks
    if (clicks > 10):
        global printings
        printings = printings+1
        clicks-=10
        global gain
        gain = gain + 1
        print.clear()
        print.goto(0,160)
        print.write("Printer level: {}".format(printings), align="center", font=("Courier", 24, "normal"))
    else:
        print("You need more than 10 clicks to buy a printer.")
#factory
buyfactory = turtle.Turtle()
buyfactory.penup()
buyfactory.hideturtle()
ffactory = turtle.Turtle()
Factoring = 0
ffactory.hideturtle()
ffactory.penup()
factory = turtle.Turtle()
factory.hideturtle()
factory.penup()
factory.goto(0,150)

#farm
buyfarm = turtle.Turtle()
buyfarm.penup()
buyfarm.hideturtle()
ffarm = turtle.Turtle()
ffarm.hideturtle()
ffarm.penup()

#printer
buyprinter = turtle.Turtle()
buyprinter.penup()
buyprinter.hideturtle()
pprinter = turtle.Turtle()
pprinter.hideturtle()
printing = 0
pprinter.hideturtle()
pprinter.penup()
printer = turtle.Turtle()
printer.hideturtle()
printer.penup()
printer.goto(0,170)
print = turtle.Turtle()
print.penup()
print.hideturtle
print.goto(0,50)


def factorian():
    global clicks
    if (clicks > 100):
        global Factoring
        Factoring = Factoring+1
        clicks-=50
        global gain
        gain = gain ** 2
        factory.clear()
        factory.goto(0,190)
        factory.write("Factory level: {}".format(Factoring), align="center", font=("Courier", 24, "normal"))

while True:
    #farm
    if clicks > 50:
        ffarm.goto(0,-150)
        ffarm.write("Click f to buy a farm!", align="center", font=("Courier", 15, "normal"))
        wn.onkeypress(farmer, "f")
        
    else:
        buyfarm.goto(0,70)
        buyfarm.write("You can buy a farm if you have more than 50 clicks!", align="center", font=("Courier", 24, "normal"))
        #factory
    if clicks > 100:
        ffactory.goto(0,-180)
        ffactory.write("Click H to buy a factory!", align="center", font=("Courier", 15, "normal"))
        wn.onkeypress(factorian, "h")
    else:
        buyfactory.goto(0,100)
        buyfactory.write("You can buy a factory if you have more than 100 clicks!", align="center", font=("Courier", 24, "normal"))
    #printer
    if clicks > 10:
        pprinter.goto(0,-130)
        pprinter.write("Click P to buy a printer!", align="center", font=("Courier", 15, "normal"))
        wn.onkeypress(printingaa, "p")
    else:
        buyprinter.goto(0,130)
        buyprinter.write("You can buy a printer if you have more than 10 clicks!", align="center", font=("Courier", 24, "normal"))
    



wn.mainloop()
    



