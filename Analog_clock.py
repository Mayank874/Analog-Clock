import time
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 600, height = 600),
wn.title("Simple Analog Clock")
wn.tracer(0)

#Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):

    #Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(100)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    #Draw the lines for the hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
    
    #Draw the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (h /12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    #Draw the minute hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (m /60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    #Draw the second hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (s /60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%I"))
    s = int(time.strftime("%s"))

    draw_clock(10, 15, 45, pen)
    wn.update()
    
    time.sleep(1)

    pen.clear()

wn.mainloop()
