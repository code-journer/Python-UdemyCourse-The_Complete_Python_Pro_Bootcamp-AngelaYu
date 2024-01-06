"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 170: Turtle Challenge: Draw Different Shapes: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

"""

# Import required modules and give them aliases
import turtle as t

# Create turtle object
tim = t.Turtle()
# Create screen object
screen = t.Screen()

# Create a function to determine the angle to turn for each shape
# 360 degrees divided by number of sides to get angles
def calc_degrees(sides):
    return 360 / sides

# Set starting coordinates
xrange = 30
yrange = 120
tim.hideturtle()
tim.penup()
tim.goto(xrange, yrange)
tim.pendown()
tim.showturtle()

# --- Create shapes using a different color for each --- #
# Triangle 360 degrees/3 sides = 120; use yellow
tim.color("black")
for _ in range(3):
    tim.right(calc_degrees(3))
    tim.forward(80)

# Square 360 degrees/4 sides = 90; use blue
tim.color("blue")
for _ in range(4):
    tim.right(calc_degrees(4))
    tim.forward(80)

# Pentagon 360 degrees/5 = 72; use black
tim.color("lightblue4")
for _ in range(5):
    tim.right(calc_degrees(5))
    tim.forward(80)

# Hexagon 360 degrees/6 = 60; use green
tim.color("green")
for _ in range(6):
    tim.right(calc_degrees(6))
    tim.forward(80)

# Heptagon 360 degrees/7 = 51.42857142857143; use red
tim.color("red")
for _ in range(7):
    tim.right(calc_degrees(7))
    tim.forward(80)

# Octagon 360 degrees/8 = 45; use purple
tim.color("purple")
for _ in range(8):
    tim.right(calc_degrees(8))
    tim.forward(80)

# Octagon 360 degrees/9 = 40; use orange
tim.color("orange")
for _ in range(9):
    tim.right(calc_degrees(9))
    tim.forward(80)

# Decagon 360 degrees/10 = 36; use brown
tim.color("brown")
for _ in range(10):
    tim.right(calc_degrees(10))
    tim.forward(80)

# Click screen to dismiss
screen.exitonclick()