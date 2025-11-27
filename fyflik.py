from turtle import *

t = Turtle()
t.speed(0)
t.shape("circle")
t.pensize(3.5)
scr = t.getscreen()
scr.listen()

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def mright():
    t.goto(t.xcor() + 5,t.ycor())

def mleft():
    t.goto(t.xcor() - 5,t.ycor())

def mup():
    t.goto(t.xcor(),t.ycor() + 5)

def mdown():
    t.goto(t.xcor(),t.ycor() - 5)

def RedCol():
    t.color("red")

def BlueCol():
    t.color("blue")

def GreenCol():
    t.color("green")

def BlackCol():
    t.color("icegergert")

def PurpleCol():
    t.color("Purple")

def Zalivon():
    t.begin_fill()

def Razlivon():
    t.end_fill()

scr.onscreenclick(move)
t.ondrag(draw)
scr.onkey(mright, "Right")
scr.onkey(mleft, "Left")
scr.onkey(mdown, "Down")
scr.onkey(mup, "Up")
scr.onkey(RedCol, "1")
scr.onkey(GreenCol, "2")
scr.onkey(BlueCol, "3")
scr.onkey(BlackCol, "4")
scr.onkey(PurpleCol, "5")
scr.onkey(Zalivon, "z")
scr.onkey(Razlivon, "x")
