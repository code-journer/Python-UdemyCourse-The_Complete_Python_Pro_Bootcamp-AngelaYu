"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 172: Python Tuples and How to Generate Random RGB Colours

Notes:
Tuple is a data type in Python, e.g. (1, 3, 8)
ordered, immutable, access using square brackets and index (like lists)
"""

# Import required modules and give them aliases
import turtle as t
from random import choice
from random_color_generator import RandomColorGenerator

# Create turtle object
tim = t.Turtle()
# Create screen object
screen = t.Screen()

# This function is used to return the color mode, what degree of color -- NOT TO SET IT
t.colormode(255)

# List used for random turn
turn_choice = [90, 180, 270, 360]

# Draw Random walk using RBG
for i in range(100):
    tim.color(RandomColorGenerator.random_color_generator())
    tim.pensize(10)  # Thicker line color
    tim.speed(10)  # Faster walk
    tim.right(choice(turn_choice))
    tim.fd(40)

# Click screen to dismiss
screen.exitonclick()
