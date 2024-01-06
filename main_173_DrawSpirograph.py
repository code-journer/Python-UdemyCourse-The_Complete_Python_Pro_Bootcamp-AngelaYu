"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 173: Turtle Challenge 5: Draw a Spirograph

"""

# Import required modules and give them aliases
import turtle as t
from random_color_generator import RandomColorGenerator

# Create turtle object
tim = t.Turtle()
# Create screen object
screen = t.Screen()

# This function is used to return the color mode, what degree of color -- NOT TO SET IT
t.colormode(255)

# Create a Spirograph pattern
num_circles = 120  # Number of circles to draw
angle_increment = 3  # Angle increment between circles
radius = 100  # Radius of the main circle
speed = "fastest"

# Create Spirograph
for i in range(num_circles):
    tim.speed(speed)  # Faster walk
    tim.color(RandomColorGenerator.random_color_generator())
    tim.circle(radius)
    tim.right(angle_increment)

# Click screen to dismiss
screen.exitonclick()