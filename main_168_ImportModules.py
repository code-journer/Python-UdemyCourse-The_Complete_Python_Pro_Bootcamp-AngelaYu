"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 168: Importing Modules, Installing Packages, and Working with Aliases

Notes:
Avoid: Can import everything from a module, eg, 'from turtle import *' - can use everything in module
keword = from; module/package name = turtle; keyword = import; class in module/package: Turtle
Con of including everything - it leaves one confused on what is performing an action, for ex.

Before importing a module, if not part of the standard Python library, I must install it first.
"""

# Import Turtle and use an alias
import turtle as t

# Create an object of Turtle
tim = t.Turtle()
# Create object of screen to keep screen displayed
screen = t.Screen()

# Click screen to dismiss
screen.exitonclick()