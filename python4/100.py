import random
import turtle

wn=turtle.Screen()
wn.title("Game")
wn.setup(width=800, height=600)
wn.tracer(0)
score=0

player=turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("black")
player.penup()
player.goto(0,-250)
player.direction="stop"

playerlist2=[]

for i in range(20):
    player2 = turtle.Turtle()
    player2.shape("circle")
    player2.penup()
    player2.color("blue")
    player2.goto(-100,250)
    player2.speed=random.randint(1,4)
    playerlist2.append(player2)

playerlist3=[]

for i in range(20):#
    player3 = turtle.Turtle()
    player3.shape("circle")
    player3.penup()
    player3.color("red")
    player3.goto(100,250)
    player3.speed=random.randint(1,4)
    playerlist3.append(player3)

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0,260)
font=("Courier",24,"normal")
pen.write("Score: {}".format(score),align="center",font=font)


def go_left():
    player.direction="Left"

def go_right():
    player.direction="Right"

wn.listen()
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()
    if player.direction == "Left":
        x = player.xcor()
        x=x-3
        player.setx(x)

    if player.direction == "Right":
        x = player.xcor()
        x=x+3
        player.setx(x)

    for player2 in playerlist2:
        y=player2.ycor()
        y=y-player2.speed
        player2.sety(y)

        if y<-300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            player2.goto(x,y)

        if player2.distance(player)<20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            player2.goto(x, y)
            score=score+10
            pen.clear()
            pen.write("Score: {} ".format(score), align="center", font=font)

    for player3 in playerlist3:
        y = player3.ycor()
        y = y - player3.speed
        player3.sety(y)

        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            player3.goto(x, y)

        if player3.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            player3.goto(x, y)
            score=score-10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=font)



