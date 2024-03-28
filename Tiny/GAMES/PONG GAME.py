import turtle
import time
import random
screen = turtle.Screen()
screen.title("Impossible Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.direction = "right"

playerOne = turtle.Turtle()
playerOne.penup()
playerOne.goto(-270,0)
playerOne.shape("square")
playerOne.shapesize(stretch_wid=5, stretch_len=1)
playerOne.direction = "Stop"
playerOne.color("blue")

playerTwo = turtle.Turtle()
playerTwo.penup()
playerTwo.goto(270,0)
playerTwo.shape("square")
playerTwo.shapesize(stretch_wid=5, stretch_len=1)
playerTwo.direction = "Stop"
playerTwo.color("red")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player 1 : 0  Player 2 : 0", align="center",
          font=("candara", 24, "bold"))


def goUp(player):
    player.direction = "up"

def goDown(player):
    player.direction = "down"
 

def moveBar(player):
    if player.direction == "up":
        player.sety(player.ycor() + 20)
    if player.direction == "down":
        player.sety(player.ycor() - 20)


def moveBall():
    if ball.direction == "right":
        ball.setx(ball.xcor()+30)
    if ball.direction == "left":
        ball.setx(ball.xcor()-30)    


screen.listen()
screen.onkeypress(lambda: goUp(playerTwo), "Up")
screen.onkeypress(lambda: goDown(playerTwo), "Down")
screen.onkeypress(lambda: goUp(playerOne), "w")
screen.onkeypress(lambda: goDown(playerOne), "z")


playerOneScore = 0
playerTwoScore = 0

while playerOneScore <= 10 and playerTwoScore <= 10:
    screen.update()
    if ball.distance(playerOne) < 30:
        ball.direction = "right"
    if ball.distance(playerTwo) < 30:
        ball.direction = "left"  
    if ball.xcor() > 290:
        time.sleep(0.2)
        ball.goto(0,0)
        playerOneScore += 1
        pen.clear()
        pen.write("Player 1 : {} Player 2 : {} ".format(
            playerOneScore, playerTwoScore), align="center", font=("candara", 24, "bold"))
        
    if ball.xcor() < -290:
        time.sleep(0.2)
        ball.goto(0,0)
        playerTwoScore += 1
        pen.clear()
        pen.write("Player 1 : {} Player 2 : {} ".format(
            playerOneScore, playerTwoScore), align="center", font=("candara", 24, "bold"))

    if playerOne.ycor() > 220 or playerOne.ycor() < -220:
        playerOne.direction = "Stop"
        moveBar(playerOne)
    if playerTwo.ycor() > 220 or playerTwo.ycor() < -220:
        playerTwo.direction = "Stop" 
        moveBar(playerTwo)   

    moveBall()
    moveBar(playerOne)
    moveBar(playerTwo)
    time.sleep(0.1)

screen.update()
pen.clear()
pen.goto(0, 0)
if playerOneScore > playerTwoScore:
    pen.write("Gameover!!! Player 1 wins! :)", align="center", font=("candara", 24, "bold"))
else:
    pen.write("Gameover!!! Player 2 wins! :)", align="center", font=("candara", 24, "bold"))
screen.mainloop()       
