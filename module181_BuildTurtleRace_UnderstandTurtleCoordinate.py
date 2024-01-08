"""
Title: Section 19: Day 19 Intermediate - Instances, State and Higher Order Functions
Description: More Turtle Graphics, Event Listeners, State and Multiple Instances
Author: Eric Cantrell
Date: January 7, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 181: Understanding the Turtle Coordinate System
   Outcome: Build a Turtle Race

"""

# Import required libraries
from turtle import Turtle, Screen
import random

# Create Screen object
screen = Screen()

# Set initial screen size
screen.setup(500, 400)

# List of turtle names
turt_name = ["lightning", "tim", "twister", "jinx", "ace", "pokey", "speedy"]
# List of turtle colors
colors = ["blue", "green", "brown", "black", "purple", "yellow", "orange"]
turts = []

# Starting coordinates of first turtle
x_coord = -235
y_coord = 150

is_race_on = False
user_bet = screen.textinput(title="Place your bet!", prompt="       Select the turtle to win.\n\nEnter your color: ")

# Create 7 turtles each with a different color
for i in range(len(turt_name)):
    t = Turtle(shape="turtle")  # Create a new turtle
    turts.append(t)
    t.name = turt_name[i]  # Assign the name from the list
    t.color(colors[i])  # Set color based on index
    t.penup()
    t.goto(x_coord, y_coord)
    y_coord -= 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turts:
        distance = random.randint(0,10)  # 10 inclusive
        turtle.forward(distance)
        if turtle.xcor() > 220:
            winner_name = turtle.name
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} - \"{winner_name}\" wins the race and you have won the bet!")
            else:
                print(f"{winning_color} - \"{winner_name}\" wins the race! Sorry, you lost the bet.")
            is_race_on = False

screen.exitonclick()  # Keep screen displayed until clicked on

def main():
    if __name__ == '__main__':
        main()