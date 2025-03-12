from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height = 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
#top_paddle = Paddle((100,100))
ball = Ball()


# Create paddle 
# paddle = Turtle()
# paddle.shape("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.penup()
# paddle.goto(350,0)


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(),new_y)
    
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(),new_y)    

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #Detect collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -300:
    #need to bounce 
        ball.bounce_y()
        
    # Detect collision with paddle 
    if ball.distance(r_paddle) < 50 and ball.xcor >340: 
        ball.bounce_x()
        
        
    #Detect R paddle misses 
    if ball.xcor() > 380:
        ball.reset_position()
        
    #Detect L paddle misses 
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()