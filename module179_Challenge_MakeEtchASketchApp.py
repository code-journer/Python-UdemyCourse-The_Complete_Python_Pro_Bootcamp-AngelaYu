"""
Title: Section 19: Day 19 Intermediate - Instances, State and Higher Order Functions
Description: More Turtle Graphics, Event Listeners, State and Multiple Instances
Author: Eric Cantrell
Date: January 7, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 179: Challenge: Make an Etch-A-Sketch App

Notes: Higher order function is essentially is the act of passing one function as an argument into another
When passing in a function as an argument do not add ()
"""
# Import required libraries
from turtle import Turtle, Screen

# Create Turtle object
tim = Turtle()
# Create Screen object
screen = Screen()


def move_forward():
    tim.forward(100)


def move_backward():
    tim.backward(100)


def circle_counter_clockwise():
    tim.circle(100)  # Positive radius


def circle_clockwise():
    tim.circle(-100)  # Negative radius


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
# Event listeners - onkey
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="k", fun=circle_counter_clockwise)
screen.onkey(key="c", fun=circle_clockwise)
screen.onkey(key="q", fun=clear_screen)

screen.exitonclick()  # Keep screen displayed until clicked on


def main():
    if __name__ == '__main__':
        main()