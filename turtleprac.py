import turtle
george = turtle.Turtle()
george.shape("turtle")
george.color("misty rose")
george.dot()
george.speed(6)
screen = turtle.Screen()
screen.bgcolor("black")

#square
'''
for i in range(4):
    george.forward(100)
    george.right(90)
george.penup()
george.goto(25,-25)
george.pendown()
for i in range(4):
    george.forward(50)
    george.right(90)
turtle.done()
'''
#star
'''
for i in range(5):
    george.forward(100)
    george.right(145)

turtle.done()
'''
#hexagon
'''
george.right(90)
for i in range(6):
    george.forward(100)
    george.left(60)
turtle.done()
'''
# Outside_In
'''
size=140#40
for i in range(28):
    george.fd(size)
    george.left(90)
    size = size - 5 #size+=5
turtle.done()
'''
#spiral helix
'''
for i in range(100):
    george.circle(5*i)
    george.circle(-5*i)
    george.left(i)
turtle.done()
'''
#spiral star
'''
size=50
for i in range(100):
    george.forward(size)
    george.right(144)
    size=size+5
turtle.done()
'''
#changing pencolor
'''
george.pencolor("blue")
for i in range(50):
    george.forward(250)
    george.left(123)
george.pencolor("pink")
for i in range(50):
    george.forward(200)
    george.left(123)
george.pencolor("yellow")
for i in range(50):
    george.forward(150)
    george.left(123)
george.pencolor("red")
for i in range(50):
    george.forward(100)
    george.left(123)
george.pencolor("green")
for i in range(50):
    george.forward(50)
    george.left(123)
turtle.done()
'''
#iterative dots
'''
width=11
height=10
for i in range(height):
    for j in range(width):
        george.stamp()
        george.penup()
        george.forward(25)
        george.pendown()
    george.penup()
    george.backward(25*width)
    george.right(90)
    george.forward(25)
    george.left(90)

turtle.done()
'''
# design 1
'''
for i in range(500):
    george.pendown()
    george.forward(100)
    george.right(30)
    george.forward(50)
    george.left(120)
    george.forward(50)
    george.right(30)
    george.forward(50)

    george.penup()
    george.setposition(0,0)
    george.right(2)
turtle.done()
'''

# face

george.penup()
george.goto(-200,200)
george.pendown()
george.circle(50)
#for i in range(4):
 #   george.forward(50)
  #  george.left(90)
george.penup()
george.goto(200,200)
george.pendown()
george.circle(50)
#for i in range(4):
 #   george.forward(50)
  #  george.left(90)
george.penup()
george.setposition(0,0)
george.forward(100)
george.left(135)
george.pendown()
for i in range(4):
    george.forward(141.4)
    george.left(90)
george.penup()
george.setposition(0,0)
george.goto(-150,-200)
george.pendown()
george.right(135)
george.forward(350)
turtle.done()

#circle through straight lines
'''
from math import sin,cos,pi
r=100
t=0
n=1.5
inc=2*pi/100
for i in range(200):
    x1=r*sin(t)
    y1=r*cos(t)
    x2=r*sin(r+t)
    y2=r*cos(r+t)
    george.penup()
    george.goto(x1,y1)
    george.pendown()
    george.goto(x2,y2)
    t+=inc
turtle.done()
'''
#rainbow hexagon
'''
george.pensize(3)
screen.setup(300,300)
colors=['green','yellow','red','violet','blue','indigo','orange']
for i in range(180):
    george.pencolor(colors[i%7])
    george.forward(i)
    george.right(55)
george.penup()
george.setpos(-100,300)
george.write("RAINBOW HEXAGON",font=("Arial",15,"bold"))
george.ht()
turtle.done()
'''

#octagon with squares
'''
colors=["green","cyan","misty rose","navy","light blue","purple","red","yellow","orange"]
george.width(4)
for k in range(8):
    color=colors[k%9]
    george.pencolor(color)
    for i in range(4):
        george.forward(100)
        george.right(90)
        for j in range(4):
           george.forward(50)
           george.right(90)
    george.penup()
    george.backward(35)
    george.right(45)
    george.forward(50)
    george.pendown()

george.hideturtle()
turtle.done()
'''

#just fun things
# screen.title("CRISS CROSS AND HOTSPOT!")
# amy=turtle.Turtle()
# amy.shape("turtle")
# colors = ["green", "cyan","navy", "purple", "red", "yellow", "orange"]
# george.width(2)
# george.penup()
# george.goto(-200,30)
# george.pendown()
# for k in range(160):
#     color = colors[k % 7]
#     george.pencolor(color)
#     george.forward(k)
#     george.penup()
#     george.forward(10)
#     george.right(60)
#     george.pendown()
# george.hideturtle()
# amy.width(2)
# amy.penup()
# amy.goto(200,30)
# amy.pendown()
# for k in range(160):
#     color = colors[k % 7]
#     amy.pencolor(color)
#     amy.forward(k)
#     amy.penup()
#     amy.forward(10)
#     amy.right(60)
#     amy.pendown()
#
# amy.hideturtle()
# turtle.done()
