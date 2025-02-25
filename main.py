# https://trinket.io/python/b87ed29ab3c4

import turtle
monty = turtle.Turtle()
monty.shape("turtle")

black = "black"
blue = "blue"
white = "white"
green = "green"
lblue = "light blue"
gray = "gray"
red = "red"
brown = "brown"

def pu():
  monty.penup()

def pd():
  monty.pendown()

def coloring(a):
  monty.color(a)
  monty.fillcolor(a)

def move(x,y):
  monty.goto(x,y)

def start_fill(x,y,color):
  pu()
  monty.goto(x,y)
  pd()
  coloring(color)
  monty.begin_fill()

def end_fill():
  monty.end_fill()

def rectangle(x1,x2,y1,y2,color):
  start_fill(x1,y1,color)
  move(x2,y1)
  move(x2,y2)
  move(x1,y2)
  move(x1,y1)
  end_fill()

def circle(x,y,r,color):
  start_fill(x,y,color)
  monty.circle(r)
  end_fill()

def triangle(x1,x2,y1,y2,color):
  start_fill(x1,y1,color)
  move(x2,y1)
  move(x2,y2)
  move(x1,y1)
  end_fill()
  
def full_triangle(x1,x2,x3,y1,y2,color):
  start_fill(x1,y1,color)
  move(x2,y1)
  move(x3,y2)
  move(x1,y1)
  end_fill()
  
def window(x1,x2,x3,y1,y2,y3,r,color):
  rectangle(x1,x2,y1,y2,color)
  circle(x3,y3,r,color)
  
# teren
rectangle(-200,200,-200,200,lblue)
rectangle(-200,200,-200,-180,blue)
circle(80,-350,120,green)
circle(-140,-300,80,green)

# most
rectangle(-120,0,-80,-20,gray)
circle(-60,-150,60,lblue)

# boczna wieża
rectangle(-160,-120,-150,90,gray)
full_triangle(-170,-110,-140,90,120,red)
window(-145,-135,-140,50,60,55,5,black)
window(-145,-135,-140,10,20,15,5,black)

# główny zamek
rectangle(0,160,-145,0,gray)
window(60,100,80,-145,-115,-135,20,brown)
window(20,30,25,-50,-40,-45,5,black)
window(20,30,25,-80,-70,-75,5,black)

window(50,60,55,-50,-40,-45,5,black)
window(50,60,55,-80,-70,-75,5,black)


window(100,110,105,-50,-40,-45,5,black)
window(100,110,105,-80,-70,-75,5,black)

window(130,140,135,-50,-40,-45,5,black)
window(130,140,135,-80,-70,-75,5,black)

rectangle(20,140,0,45,gray)
window(42.5,52.5,47.5,20,30,25,5,black)
window(75,85,80,20,30,25,5,black)
window(107.5,117.5,112.5,20,30,25,5,black)

# wieża lewa
rectangle(20,40,45,75,gray)
rectangle(20,24,75,80,gray)
rectangle(28,32,75,80,gray)
rectangle(36,40,75,80,gray)

# wieża prawa
rectangle(120,140,45,75,gray)
rectangle(120,124,75,80,gray)
rectangle(128,132,75,80,gray)
rectangle(136,140,75,80,gray)

# ozdobnik
triangle(100,200,-200,-100,black)
triangle(100,200,200,100,black)
triangle(-100,-200,200,100,black)
triangle(-100,-200,-200,-100,black)