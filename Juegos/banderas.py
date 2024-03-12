import turtle
import time

myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.speed(2)

window = turtle.Screen()
window.bgcolor("#DDDDDD")

myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()


myPen.color("white")
myPen.pensize(2)
myPen.fillcolor("white")
myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(360)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()  
  

myPen.color("green")
myPen.pensize(2)
myPen.fillcolor("green")

myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()

myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(120)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()  


myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")

myPen.penup()
myPen.goto(60, -120)
myPen.pendown()

myPen.begin_fill()
for i in range(0, 2):
  myPen.forward(120)
  myPen.left(90)
  myPen.forward(240)
  myPen.left(90)
myPen.end_fill()  



myPen.penup()
myPen.goto(-62, -160)
myPen.color("red")
myPen.write("ITALIA", None, None, "24pt bold")

myPen.hideturtle()
turtle.exitonclick()