"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 171: Turtle Challenge: Draw a Random Walk

"""

# Import required modules and give them aliases
import turtle as t
from random import choice

# Create turtle object
tim = t.Turtle()
# Create screen object
screen = t.Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turn_choice = [90, 180, 270, 360]

# Set starting coordinates
xrange = -20
yrange = 50
tim.hideturtle()
tim.penup()
tim.goto(xrange, yrange)
tim.pendown()
tim.showturtle()

# Draw Random walk
for i in range(100):
    color = choice(colours)  # Random colors
    tim.color(color)
    tim.pensize(10) # Thicker line color
    tim.speed(0)
    tim.right(choice(turn_choice))
    tim.fd(20)

# Click screen to dismiss
screen.exitonclick()