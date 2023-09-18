import turtle as t
import datetime
import time

t.bgcolor("black")
t.hideturtle()
t.speed(0)
t.Screen().tracer(0)
t.pensize(3)
t.title("Analog Clock")
def pen_up_down(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
while True:
    t.pencolor("green")
    t.setheading(0)
    pen_up_down(0,-200)
    t.circle(200)
    pen_up_down(0,0)
    t.setheading(90)
    for i in range(0,12):
        t.penup()
        t.forward(180)
        t.pendown()
        t.forward(20)
        pen_up_down(0,0)
        t.right(30)

    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))

    t.setheading(90)
    t.pencolor("white")
    t.right((h/12)*360)
    t.forward(100)
    pen_up_down(0,0)
    
    t.setheading(90)
    t.pencolor("red")
    t.right((m/60)*360)
    t.forward(150)
    pen_up_down(0,0)
    
    t.setheading(90)
    t.pencolor("blue")
    t.right((s/60)*360)
    t.forward(180)
    pen_up_down(0,0)

    t.Screen().update()
    time.sleep(1)
    t.clear()


