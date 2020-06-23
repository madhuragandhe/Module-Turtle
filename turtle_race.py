#TURTLE RACE

import turtle
from random import randint
screen=turtle.Screen()
screen.bgcolor("black")
pointer=turtle.Turtle()
pointer.color("white")
pointer.shape("arrow")
pointer.speed(0)

#race tracks
max=9
pointer.penup()
pointer.goto(-350,250)
pointer.pendown()
for step in range(max):
    pointer.write(step,align='center')
    pointer.penup()
    pointer.right(90)
    pointer.pendown()
    pointer.forward(400)
    pointer.penup()
    pointer.backward(400)
    pointer.left(90)
    pointer.forward(100)
    pointer.pendown()

#participants
#1
pi=turtle.Turtle()
pi.color("blue")
pi.shape("turtle")
pi.penup()
pi.goto(-350,170)
#2
tau=turtle.Turtle()
tau.color("red")
tau.shape("turtle")
tau.penup()
tau.goto(-350,90)
#3
rho=turtle.Turtle()
rho.color("yellow")
rho.shape("turtle")
rho.penup()
rho.goto(-350,10)
#4
iota=turtle.Turtle()
iota.color("green")
iota.shape("turtle")
iota.penup()
iota.goto(-350,-70)

for i in range(36):
    pi.right(10)
    tau.left(10)
    rho.right(10)
    iota.left(10)

pi.pendown()
tau.pendown()
rho.pendown()
iota.pendown()
for i in range(220):
    pi.forward(randint(1,7))
    tau.forward(randint(1,7))
    rho.forward(randint(1,7))
    iota.forward(randint(1,7))

turtle.done()