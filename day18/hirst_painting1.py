# import colorgram

# rgb_colors =[]
# colors = colorgram.extract('download.jpg',200)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g 
#     b = color.rgb.b
#     new_color= (r,g,b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

import turtle as turtle_module 
import random 

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
# color_list = [(123, 105, 89), (91, 99, 104), (161, 144, 130), (101, 108, 105), (62, 44, 37), (146, 126, 104), (114, 103, 107), (176, 164, 167), (142, 121, 116), (85, 55, 46), (50, 55, 52), (127, 134, 126), (51, 54, 57), (46, 36, 38), (140, 120, 122), (123, 131, 122), (130, 132, 135), (71, 64, 53), (73, 58, 60), (62, 62, 73), (58, 66, 64), (126, 126, 130), (58, 66, 68), (125, 129, 130)]
color_list= [(166, 173, 181), (200, 203, 210), (214, 210, 205), (214, 205, 210), (204, 211, 207), (93, 110, 122), (186, 169, 138), (11, 21, 36), (187, 190, 200), (187, 160, 174), (156, 177, 167), (131, 88, 
64), (60, 29, 39), (126, 76, 94), (208, 181, 193), (201, 199, 156), (120, 126, 139), (171, 157, 37), (50, 35, 29), (190, 86, 118), (127, 27, 43), (71, 108, 93), (182, 198, 192), (180, 196, 200), (122, 40, 30), (67, 152, 169), (10, 82, 97), (212, 183, 178), (32, 45, 39), (192, 86, 79), (95, 148, 122), (19, 91, 64), (52, 57, 81), (67, 65, 56), (200, 212, 42)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
     
    if dot_count % 10 ==0: 
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()