from turtle import *

def draw_square(length):
    #right now this function draws a line, update it iteravely to draw a square
    forward(length)
    right(90)


speed(0)
penup()
goto(-200, 100)
pendown()
draw_square(50)
done()