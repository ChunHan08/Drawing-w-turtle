import turtle 
import math 

squareWidth = 20
circleRadius = 10
triangleLength = 20

itemNum = 0
maxItem = 3

colorNum = 0
colors = ["red", "blue", "green", "yellow", "purple", "orange", "black", "brown", "pink", "cyan", "magenta", "gray", "gold", "silver"]

turtle.hideturtle()
turtle.speed(0)
turtle.up()

def circle(x, y):
  turtle.begin_fill()
  turtle.goto(x, y-circleRadius)
  turtle.circle(circleRadius)
  turtle.end_fill()

def square(x, y):
  turtle.begin_fill()
  turtle.goto(x-squareWidth/2, y-(squareWidth/2))
  turtle.setheading(0)
  for x in range(4):
    turtle.forward(20)
    turtle.left(90)
    turtle.end_fill()

def triangle(x, y):
  turtle.goto(x-(triangleLength/2), y-((triangleLength * math.sqrt(3))/6))
  turtle.setheading(0)
  turtle.begin_fill()
  for x in range(3):
    turtle.forward(triangleLength)
    turtle.left(120)
    turtle.end_fill()
    turtle.setheading(0)
    
def switchShape(x,y):
  global itemNum
  global maxItem

def switchshape(x,y):
  global itemNum
  global maxItem
  itemNum += 1
  if (itemNum >= maxItem):
    itemNum = 0

def drawItem(x, y):
  print("HERE")
  global itemNum 
  if (itemNum == 0):
    circle(x, y)
  elif(itemNum == 1):
    square(x,y)
  elif (itemNum == 2):
    triangle(x, y)
  else:
    print(itemNum)

def switchColor(x,y):
  global colorNum
  global colors 
  colorNum += 1
  if (colorNum >= len(colors)):
    colorNum = 0
  turtle.color(colors[colorNum])
turtle.onscreenclick(drawItem, 1)
turtle.onscreenclick(switchColor, 2)
turtle.onscreenclick(switchShape, 3)\

def alternativeControlColor():
  canvas = turtle.getcanvas()
  x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
  switchColor(x,y)

def alternativeControlShape():
  canvas = turtle.getcanvas()
  x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
  switchShape(x,y)

turtle.onkey(alternativeControlColor, "s")
turtle.onkey(alternativeControlShape, "d")

turtle.listen()
turtle.mainloop()