"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 175: Hirst Painting Project Part 2 - Drawing the Dots

Notes:
Reqs: using turtle, develop a 10x10 row of spots, random colors, using
Dot size 1, spaced 50 paces apart
"""

# Import required modules and give them aliases
import turtle as t
import colorgram as cg
import random

# This function is used to return the color mode, what degree of color -- NOT TO SET IT
t.colormode(255)

# Extract 6 colors from an image.
colors = cg.extract('HirstDots.jpg', 24)  # Returns a list of colors

# rgb_colors = []
# # Access each of the colors
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# rgb_colors.remove((254, 253, 249))  # Removing white background color
# rgb_colors.remove((247, 254, 251))  # Removing white background color

# List of extracted colors white background excluded
color_list = [(248, 150, 92), (210, 65, 116), (45, 83, 182), (242, 131, 153), (252, 243, 248), (228, 224, 79), (35, 216, 190), (149, 55, 41), (38, 47, 158), (112, 214, 250), (86, 25, 32), (231, 242, 251), (55, 211, 189), (252, 218, 0), (165, 66, 101), (123, 175, 205), (243, 146, 155), (245, 148, 144), (135, 27, 37), (216, 66, 61), (138, 218, 205), (114, 115, 167)]

# Create a turtle object
tim = t.Turtle()
# Create object of screen to keep screen displayed
screen = t.Screen()

tim.pensize(20)
tim.speed("fastest")

xrange = -225
yrange = 225
paces = 50

for _ in range(10):
    tim.penup()
    tim.goto(xrange, yrange)
    tim.pendown()

    for count in range(10):
        random.shuffle(color_list)
        tim.color(random.choice(color_list))
        tim.circle(1)
        tim.fillcolor()
        tim.penup()
        tim.forward(paces)
        tim.pendown()

        if count == 9:
            tim.penup()
            yrange -= paces
            tim.pendown()

# Click screen to dismiss
screen.exitonclick()