"""
Title: Section 18: Day 18 Intermediate
Description: Turtle & the Graphical User Interface
Author: Eric Cantrell
Date: January 5, 2024
Course: Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
IDE: PyCharm

Topic:
1) Module 174: Hirst Painting Project Part 1 - How to Extract RGB Values from Images

Notes:
colorgram.py is a Python library that lets you extract colors from images
colorgram.py is a port of cologram.js, a JavaScript library written by GitHub user @darosh
"""

# Import required modules and give them aliases
import colorgram as cg

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

color_list = [(248, 150, 92), (210, 65, 116), (45, 83, 182), (242, 131, 153), (252, 243, 248), (228, 224, 79), (35, 216, 190), (149, 55, 41), (38, 47, 158), (112, 214, 250), (86, 25, 32), (231, 242, 251), (55, 211, 189), (252, 218, 0), (165, 66, 101), (123, 175, 205), (243, 146, 155), (245, 148, 144), (135, 27, 37), (216, 66, 61), (138, 218, 205), (114, 115, 167)]
