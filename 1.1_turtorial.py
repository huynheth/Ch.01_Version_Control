'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
answer=0
for i in range(10):
  if i!=3:
    answer+=i
print(answer)

#here is code.
import turtle
kit=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the screen
kit.pensize(3) # width of pen line
kit.speed(75)  # speed of drawing. Go fast to not waste time.



#ears
def ears():
  kit.begin_fill()
  kit.color('black')
  kit.circle(30)
  kit.end_fill()
  kit.begin_fill()
  kit.color('pink')
  kit.circle(15)
  kit.end_fill()
  kit.penup()
kit.goto(-10,0)
ears()
kit.penup()
kit.forward(120)
ears()

#face base
kit.goto(50,-125)
kit.left(120)
kit.begin_fill()
kit.color('grey')
kit.pendown()
kit.forward(150)
kit.right(120)
kit.forward(150)
kit.right(120)
kit.forward(150)
kit.end_fill()
kit.penup()
kit.left(210)

#eyes
def eyes():
  kit.begin_fill()
  kit.color('black')
  kit.circle(22)
  kit.end_fill()
  kit.begin_fill()
  kit.color('white')
  kit.circle(20)
  kit.end_fill()
  kit.pendown
  kit.circle(20)
  kit.begin_fill()
  kit.color('black')
  kit.circle(5)
  kit.end_fill()
kit.goto(10,-20)
eyes()
kit.goto(90,-20)
kit.right(180)
eyes()

#nose/teeth
def whiskers():
  kit.color('black')
  kit.pensize(1)
  kit.pendown()
  kit.forward(75)
  kit.penup()

kit.goto(50,-125)
kit.pendown()
kit.left(90)
kit.forward(10)
kit.right(90)
kit.pensize(2)
kit.forward(20)
kit.right(90)
kit.forward(10)
kit.right(90)
kit.forward(20)
kit.right(180)
kit.forward(17)
kit.right(90)
kit.forward(10)
kit.right(90)
kit.forward(17)
kit.pensize(3)
kit.right(90)
kit.forward(10)
kit.begin_fill()
kit.color('pink')
kit.circle(20)
kit.end_fill()
kit.penup()
kit.goto(67,-115)
whiskers()
kit.goto(67,-115)
kit.right(45)
whiskers()
kit.goto(67,-115)
kit.left(90)
whiskers()
kit.goto(33,-115)
kit.right(180)
whiskers()
kit.goto(33,-115)
kit.right(45)
whiskers()
kit.goto(33,-115)
kit.right(45)
whiskers()

kit.penup()
kit.goto(-100,-100)
kit.color('red')
kit.write('Ethan H',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
