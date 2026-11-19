

import turtle
import math
import time
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Code and Seek Winter!"

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)
t = turtle.Turtle()


screen.tracer(0)

## snowflake
def bigsnowflake():                #bigger snowflake for splash screen
    for i in range(8):
        t.pencolor("white")

        t.fd(20)
        t.backward(5)
        t.right(30)
        t.fd(10)
        t.backward(10)
        t.left(60)
        t.fd(10)
        t.backward(10)
        t.right(30)
        #second

        t.backward(7.5)
        t.right(30)
        t.fd(8)
        t.backward(8)
        t.left(60)
        t.fd(8)
        t.backward(8)
        t.right(30)
        t.backward(7.5)
        t.fd(25)
        t.backward(25)
        t.right(45)

def smallsnowflake():              #smaller snowflake for the game
    for i in range(8):
        t.pencolor(0.95,0.92,1)

        t.fd(12)
        t.backward(2)
        t.backward(5/2)
        t.right(30)
        t.fd(10/2)
        t.backward(10/2)
        t.left(60)
        t.fd(10/2)
        t.backward(10/2)
        t.right(30)
        #second

        t.backward(7.5/2)
        t.right(30)
        t.fd(8/2)
        t.backward(8/2)
        t.left(60)
        t.fd(8/2)
        t.backward(8/2)
        t.right(30)
        t.backward(7.5/2)
        t.fd(14)
        t.backward(14)
        t.right(45)

##splash screen
screen.bgcolor(0.058,0.0039, 0.301)
t.color("white")
t.write("CODE AND SEEK (WINTER THEME!!)", align="center", font=("Courier", 25, "bold"))
t.penup()
t.goto(0,-40)
t.pendown()
t.write("1.Allow Player 1 to choose a secret location for the target while Player 2 looks away ", align="center", font=("Courier", 12, "italic"))
t.penup()
t.goto(0,-60)
t.pendown()
t.write(" 2.Player 2 has 4 tries to guess the coordinate", align="center", font=("Courier", 12, "italic"))
t.penup()
t.goto(0,-80)
t.pendown()
t.write(" 3.Boundaries: x = -450 to 450 and y = -225 to 225.", align="center", font=("Courier", 12, "italic"))


def snowflakes_splash(a,b):
    for i in range (100):

        t.penup()
        t.goto(a,b)
        t.pendown()
        t.pensize(2.4)
        bigsnowflake()
        a+=60

snowflakes_splash(-450,-150)         #snowflake border for splash screen
snowflakes_splash(-450,150)


screen.update()

time.sleep(5)

##background gradient

x=0.15
t.penup()
t.goto(-450,222)
t.pendown()


for i in range(12):

    t.fillcolor(0, 0, x)
    t.pencolor(0,0,x)
    t.begin_fill()
    #rectangle for fill
    for j in range(2):      #rectangles to fill up different hues to create gradient
        t.forward(900)
        t.right(90)
        t.fd(30)
        t.right(90)
    t.end_fill()


    t.right(90)
    t.forward(30)
    t.left(90)
    x = x + 0.035           #increments of colour for gradient

##Snow on ground
#first hill
t.pencolor(0.97,0.96,0.93 )
t.fillcolor(0.97,0.96,0.93 )
t.begin_fill()
t.goto(-1125,-1100)
t.right(90)
t.circle(1040)
t.end_fill()
#second hill
t.penup()
t.goto(825,-605)
t.left(180)
t.pendown()
t.fillcolor(0.97,0.96,0.93 )
t.begin_fill()
t.circle(540)
t.end_fill()






##snowflake call
#snowflake spread out
for i in range (40):
    a=random.randrange(-450,450)
    b=random.randrange(-50,225)
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.pensize(1)

    smallsnowflake()



##snowman
def snowman():
    t.pencolor("white")
    t.right(90)
    t.penup()

    t.pendown()
    t.dot(50)
    t.left(90)
    t.fd(45)
    t.dot(40)
    t.fd(15)
    t.left(90)
    t.backward(16)
    #snowman accessories
    #scarf
    for j in range(2):
        t.pencolor("darkorchid4")
        t.fillcolor("darkorchid4")
        t.begin_fill()
        t.fd(32)
        t.right(90)
        t.fd(8)
        t.right(90)
        t.end_fill()
    t.penup()
    t.pencolor("white")
    t.fd(16)
    t.right(90)
    t.fd(20)

    t.dot(30)
    t.penup()
    t.backward(60)
    t.pendown()
    t.pencolor("black")
    t.penup()
    t.fd(8)
    t.pendown()

    #snowman accessories
    #button
    for i in range(3):
        t.penup()
        t.fd(10)
        t.dot(5)
        t.pendown()
    #nose
    t.penup()
    t.fd(20)
    t.pendown()
    t.pencolor("orange")
    t.dot(5)
    #eyes
    t.penup()
    t.right(45)
    t.fd(10)
    t.pendown()
    t.pencolor("black")
    t.dot(5)
    t.left(135)
    t.penup()
    t.fd(12)
    t.pendown()
    t.dot(5)

    t.pensize(1)
    #hat
    t.penup()
    t.right(90)
    t.fd(10)
    t.pendown()
    t.right(90)
    t.fd(20)
    t.backward(28)
    t.left(90)
    t.color("black")
    t.begin_fill()
    for i in range(2):
        t.fd(4)
        t.right(90)
        t.fd(28)
        t.right(90)

    t.fd(4)
    t.right(90)
    t.fd(7)
    t.left(90)
    for i in range(4):
        t.fd(15)
        t.right(90)


    t.end_fill()

    t.penup()


#snowman location row wise
def snowmanlocation(a,b):
    for i in range (9):
        d=(200)
        t.penup()
        t.goto(a,b)
        t.pendown()
        snowman()
        a+=d
snowmanlocation(-400,-90)
snowmanlocation(-300,-200)




##location finding
x_hiding=turtle.numinput("Hiding loaction", "x coordinate")    #hiding location x coordinate
y_hiding=turtle.numinput("Hiding loaction", "y coordinate")    #hiding location y coordinate
highestscore=0
bestguess=1000000
totdistance=0
for i in range(4):
    P2_x_guess=turtle.numinput(" Guess hiding loaction", "x coordinate guess")  #hiding location guess for x coordinate
    P2_y_guess=turtle.numinput("Guess hiding loaction", "y coordinate guess")   #hiding location guessfor y coordinate
    t.penup()
    t.goto( P2_x_guess,P2_y_guess)
    t.pendown()
    t.pencolor("red")
    distance=round(math.sqrt(((x_hiding- P2_x_guess)**2 + (y_hiding-P2_y_guess)**2)),2)                 #euclidean distance from hiding point
    bestguess=min(bestguess,distance)
    score2=max(0,200-distance)
    score1=((score2)**2)/4000                                          #scoring system
    score=round(score1,2)
    highestscore = max(highestscore, score)                            #getting max score
    t.dot(15)
    t.write(f"location {i+1},\n distance= {distance},\n {score}", font=("courier", 10, "bold"))
    screen.update()
    totdistance+=distance                                              #total distance travelled by the turtle

#marking the hiding spot
time.sleep(1)
t.penup()
t.goto(x_hiding,y_hiding)
t.pendown()
t.color("green")
t.dot(15)
t.write(f"chosen coordinate {x_hiding}, {y_hiding}", font=("courier", 16, "bold"))
screen.update()
time.sleep(2)
screen.clearscreen()




##display score

screen.bgcolor(0.058,0.0039, 0.301)
t.color("white")
screen.tracer(0)
t.goto(0,0)
t.write(f"YOUR HIGHEST SCORE IS {highestscore}!!!\nBest guess:{bestguess}pixels away\nTotal distance: {totdistance} ",align="center", font=("Courier", 15, "bold"))
t.penup()
t.goto(270,10)
t.pendown()
snowflakes_splash(-450,-150)
snowflakes_splash(-450,150)
screen.update()












# ------------------
# End of your code

# Make a clean exit
screen.exitonclick()