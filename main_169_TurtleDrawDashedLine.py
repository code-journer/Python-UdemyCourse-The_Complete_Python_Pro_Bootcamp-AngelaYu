"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 169: Turtle Challenge: Draw a dashed line

"""
# Import required modules
import turtle as t

# Create turtle object
tim = t.Turtle()
# Create screen object
screen = t.Screen()
# Set tutle speed
tim.speed("slowest")
# Set starting coordinates
xrange = -200
yrange = 40

# Draw a dashed line
tim.hideturtle()
tim.penup()
tim.goto(xrange, yrange)
tim.pendown()
tim.showturtle()

for _ in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Click screen to dismiss
screen.exitonclick()
