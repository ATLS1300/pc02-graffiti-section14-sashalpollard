#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Sasha Pollard
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

art = turtle.Turtle() #initializes turtle

turtle.Screen()

#Jeffery Beach-zos!!!

# Draws sun in the sky - circle requirement
art.pencolor("")
art.pensize(10)
art.setx(200)
art.sety(200)
art.begin_fill()
art.pencolor("YELLOW")
rad = 80
art.circle(rad)
yell = "YELLOW"
art.fillcolor(yell)
art.end_fill()

#Draws the water that jeff is swimming in - polygon requirement
art.pencolor("")
art.pensize(1)
art.setx(-300)
art.sety(-300)
art.begin_fill()
art.pencolor("BLUE")
art.forward(-80) 
art.left(90)
art.forward(90) 
art.left(90) 
art.forward(-780) 
art.left(90) 
art.forward(90) 
art.left(90) 
blu = "BLUE"
art.fillcolor(blu)
art.end_fill()

# Line for Jeff's hat - line requirement
art.pencolor("")
art.pensize(15)
art.setx(-110)
art.sety(200)
art.pencolor("TAN")
art.forward(170) 

# semicircle for Jeff's Hat
art.pencolor("")
art.pensize(5)
art.setx(25)
art.sety(200)
art.begin_fill()
art.pencolor("TAN")
art.left(90)
art.circle(50,180)
tan = "TAN"
art.fillcolor(tan)
art.end_fill()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
