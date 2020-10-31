import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @andreasuperchi")  # sets the title in the top bar of the application
wn.bgcolor("black")
wn.setup(width=800, height=600)  # sets the dimensions of the window when it opens up
wn.tracer(0)  # disables the refresh of the animation

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # creates a turtle object
paddle_a.speed(0)  # speed of animation, it sets it to the maximum value
paddle_a.shape("square")  # default is 20px x 20 px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # changes the dimensions of the paddle by stretching its dimensions
paddle_a.penup()  # doesn't draw when the object is moving
paddle_a.goto(-350, 0)  # 0,0 is in the middle of the screen

# Paddle B
paddle_b = turtle.Turtle()  # creates a turtle object
paddle_b.speed(0)  # speed of animation, it sets it to the maximum value
paddle_b.shape("square")  # default is 20px x 20 px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # changes the dimensions of the paddle by stretching its dimensions
paddle_b.penup()  # doesn't draw when the object is moving
paddle_b.goto(350, 0)  # 0,0 is in the middle of the screen

# Ball
ball = turtle.Turtle()  # creates a turtle object
ball.speed(0)  # speed of animation, it sets it to the maximum value
ball.shape("square")  # default is 20px x 20 px
ball.color("white")
ball.penup()  # doesn't draw when the object is moving
ball.goto(0, 0)  # 0,0 is in the middle of the screen
ball.dx = 0.13  # the ball will be moving x pixels at a time
ball.dy = 0.13

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B:  0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()  # returns the y coordinate
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # returns the y coordinate
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # returns the y coordinate
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # returns the y coordinate
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # listens for keyboard input

wn.onkeypress(paddle_a_up, "w")  # when user presses down w, we call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")  # when user presses down s, we call the function paddle_a_down


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B:  {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B:  {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # AI Player
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()
