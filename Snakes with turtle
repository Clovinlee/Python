import turtle
import time
import random

delay = 0.05

main = turtle.Screen()
main.title("My Snake Game")
main.bgcolor("gray")
main.setup(width=620, height=620)
main.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("yellow")
food.shapesize(0.5,0.5)
food.penup()
food.goto(0,100)

segments = []

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction =="up":
        head.sety(head.ycor() + 20)
    if head.direction =="down":
        head.sety(head.ycor() - 20)
    if head.direction =="right":
        head.setx(head.xcor() + 20)
    if head.direction =="left":
        head.setx(head.xcor() - 20)

def addSegment():
    new_segment = turtle.Turtle()
    new_segment.shape('square')
    new_segment.color('green')
    new_segment.penup()
    segments.append(new_segment)

#Scores
scorenow = 0
highscore = 0
score = turtle.Turtle()
score.shape('square')
score.color('black')
score.penup()
score.speed(0)
score.hideturtle()
score.goto(120,290)
score.write("Score : {}   High Score : {}".format(scorenow, highscore), font=("Arial", 10, "normal"))

#Keyboard detect
main.listen()
main.onkeypress(go_up, 'w')
main.onkeypress(go_down, 's')
main.onkeypress(go_left, 'a')
main.onkeypress(go_right, 'd')

foodValid = False
gameOver = False

#Main game loop
while True:
    main.update()
    move()

    for x in segments:
        if head.distance(x)<20:
            gameOver = True

    if gameOver == True:
        time.sleep(2)
        for x in segments:
            x.color = 'white'
            x.hideturtle()
        segments.clear()
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        food.goto(0,200)
        scorenow = 0
        gameOver = False


    if head.xcor() < -290:
        head.setx(290)
    if head.xcor() > 290:
        head.setx(-290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)
    score.clear()
    #Check food collision
    if head.distance(food) < 17:
        #Move food to random spot but NOT in body
        if len(segments) > 0:
            while foodValid == False:
                food.goto(random.randint(-290, 290) // 1, random.randint(-290, 290) // 1)
                for x in segments:
                    if food.distance(x) > 20:
                        if x == segments[-1]:
                            foodValid = True
                        pass
                    else:
                        print(food.xcor(),food.ycor(), "Body :", x.xcor(),x.ycor())
                        break
        else:
            food.goto(random.randint(-290, 290) // 1, random.randint(-290, 290) // 1)
        #Create new segments
        addSegment()
        #Add Scores

        scorenow += 10
        if scorenow > highscore:
            highscore = scorenow
    score.write("Score : {}   High Score : {}".format(scorenow, highscore), font=("Arial", 10, "normal"))
    #Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #Move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    foodValid = False
    time.sleep(delay)

main.mainloop()
