# Hexagon

import turtle
import random

wn = turtle.Screen()
wn.title("Hexagon")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.speed(0)

def draw_hexagon(x, y, size, color, pen):
    pen.color(color)
    pen.penup()
    pen.setheading(0)
    pen.goto(x,y)
    pen.pendown()
    pen.pensize(2)
    pen.fd(size)
    for _ in range(6):
        pen.rt(60)
        pen.fd(size)
    pen.penup()

colors = ["red", "orange", "yellow", "green", "blue", "purple","white"]

while True:
    for row in range(16):
        for column in range(20):
            screen_x = -320 + column * 31
            screen_y = 300 - row * 37
            if column % 2 == 0:
                screen_y += 18
            color = random.choice(colors)
            draw_hexagon(screen_x, screen_y, 20, color, pen)

    wn.update()
    pen.clear()

wn.mainloop()
