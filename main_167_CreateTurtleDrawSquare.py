"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 167 & 168: Using Turtle class to create a turtle object, give it color and shape, and move it on a screen.

"""

# Import required modules and give them aliases
import turtle as t

# Create turtle object
tim = t.Turtle()
# Create screen object
screen = t.Screen()

# Give shape to turtle
tim.shape("turtle")
# Give turtle color
tim.color("DarkOliveGreen3")
# Set tutle speed
tim.speed(2)

# Set starting coordinates
xrange = -100
yrange = 130

# Move the turtle and draw a square
tim.hideturtle()
tim.penup()
tim.goto(xrange, yrange)
tim.pendown()
tim.showturtle()
for _ in range(4):
    tim.forward(200)
    tim.right(90)

# Create object of screen to keep screen displayed
screen.exitonclick()
