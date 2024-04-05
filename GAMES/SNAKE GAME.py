import turtle
import time
import random

delay = 0.1
playerOne = 0
playerTwo = 0



wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")

wn.setup(width=600, height=600)
wn.tracer(0)


head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(-100, 0)
head.direction = "Stop"

head1 = turtle.Turtle()
head1.shape("square")
head1.color("white")
head1.penup()
head1.goto(100, 0)
head1.direction = "Stop"


food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(200, 100)

food1 = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food1.speed(0)
food1.shape(shapes)
food1.color(colors)
food1.penup()
food1.goto(-200, 100)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player 1 : 0  Player 2 : 0", align="center",
          font=("candara", 24, "bold"))

segments = []
segments1 = []

def goup(head):
        if head.direction != "down":
            head.direction = "up"


def godown(head):
        if head.direction != "up":
            head.direction = "down"


def goleft(head):
        if head.direction != "right":
            head.direction = "left"


def goright(head):
        if head.direction != "left":
            head.direction = "right"
 
def move(head):
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def checkHeadBarrier(head):
    if head.xcor() > 290:
        head.goto(-290, head.ycor())
         
    if head.xcor() < -290:
        head.goto(290, head.ycor())

    if head.ycor() > 290:
        head.goto(head.xcor(), -290)

    if head.ycor() < -290:
        head.goto(head.xcor(), 290)

def checkHeadFood(head, food, segment):
     global delay
     if head.distance(food) < 30:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.color = random.choice(['red', 'green', 'black'])
        food.shape = random.choice(['square', 'triangle', 'circle'])
        food.goto(x, y)

      
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  
        new_segment.penup()
        segment.append(new_segment)
        delay -= 0.001
        
        return True
     else:
          return False 

def headBodyCollision(head, segments):
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move(head)    
    for segment in segments:
        if segment.distance(head) < 5:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                playerOne, playerTwo), align="center", font=("candara", 24, "bold"))    

wn.listen()
wn.onkeypress(lambda: goup(head), "Up")
wn.onkeypress(lambda: godown(head), "Down")
wn.onkeypress(lambda: goleft(head), "Left")
wn.onkeypress(lambda: goright(head), "Right")
wn.onkeypress(lambda: goup(head1), "w")
wn.onkeypress(lambda: godown(head1), "z")
wn.onkeypress(lambda: goleft(head1), "a")
wn.onkeypress(lambda: goright(head1), "s")


while playerOne < 20 and playerTwo < 20:
    wn.update()
    checkHeadBarrier(head)
    checkHeadBarrier(head1)
    if checkHeadFood(head, food, segments):
            playerOne += 2
            
    if checkHeadFood(head, food1, segments):
            playerOne += 2
                  
    if checkHeadFood(head1, food, segments1):
            playerTwo += 2
              
    if checkHeadFood(head1, food1, segments1):
            playerTwo += 2
               
    pen.clear()
    pen.write("Player 1 : {} Player 2 : {} ".format(
        playerOne, playerTwo), align="center", font=("candara", 24, "bold"))
    headBodyCollision(head, segments)
    headBodyCollision(head1, segments1)
    
    time.sleep(delay)

if playerOne > playerTwo:
    pen.goto(0,0)
    pen.clear()
    pen.write("Gameover! Player 1 wins!!", align="center", font=("candara", 24, "bold"))
else:
    pen.goto(0,0)
    pen.clear()
    pen.write("Gameover! Player 2 wins!!", align="center", font=("candara", 24, "bold"))
         
     
wn.mainloop()