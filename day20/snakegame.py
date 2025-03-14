from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2= Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)

# step 1: Creating snake body 

starting_positions =[(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
    

    
#step 2: Move the snake 
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
        
        
        

screen.exitonclick()