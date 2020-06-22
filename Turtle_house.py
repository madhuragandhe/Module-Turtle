#  program to draw a house using turtle module

import turtle
import math
# set background color
screen = turtle.Screen()
screen.bgcolor("black")
# create our turtle
george = turtle.Turtle()
george.color("pink")
george.shape("turtle")
george.speed(3)
# functions to draw and fill rectangle
def drawRectangle(t,width,height,color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
# functions to draw and fill equilateral triangle
def drawTriangle(t,length,color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.end_fill()
# functions to draw and fill parallelogram
def drawParallelogram(t,width,height,color):
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    t.forward(width)
    t.left(120)
    t.forward(height)
    t.left(60)
    t.forward(width)
    t.left(120)
    t.forward(height)
    t.left(60)
    t.end_fill()
# draw and fill the front of the house
george.penup()
george.goto(-150,-120)
george.pendown()
drawRectangle(george,100,110,"lime green")
# draw and fill the front door
george.penup()
george.goto(-120,-120)
george.pendown()
drawRectangle(george,40,60,"maroon")
# front roof
george.penup()
george.goto(-150,-10)
george.pendown()
drawTriangle(george,100,"olive")
george.penup()
george.goto(-100,0)
george.pendown()
george.fillcolor("cyan")
george.begin_fill()
george.circle(20)
george.end_fill()
# side of the house
george.penup()
george.goto(-50,-120)
george.pendown()
drawRectangle(george,150,110,"teal")
# window
george.penup()
george.goto(-35,-80)#(-30,-60)
george.pendown()
drawRectangle(george,30,30,"fuchsia")
george.penup()
george.goto(40,-80)
george.pendown()
drawRectangle(george,30,30,"fuchsia")
# side roof
george.penup()
george.goto(-50,-10)
drawParallelogram(george,150,100,"dark green")
# bring the turtle down to front door
george.penup()
george.goto(-100,-150)
george.left(90)

turtle.done()
