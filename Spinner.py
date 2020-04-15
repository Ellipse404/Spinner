# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:56:31 2020

@author: BHASKAR NEOGI
"""

import turtle
from random import randint as rn

spin = turtle.Turtle()
roller = turtle.Screen()
roller.bgpic("bgimg2.gif")

colors = ["white","yellow","brown","red","orchid4","blue","royalblue1","green","seagreen4","orange","dodgerblue4","pink","violet","grey","cyan"]
for i in range (16) : col = rn(0,16)

spin.pencolor( colors[ col] )
spin.pensize(6)
spin.speed(200)

def Spinner(spin,match):
    spin.fd(match)
    spin.rt(60)
    Spinner(spin,match -4)

Spinner(spin,10)

spin.hideturtle()
turtle.exitonclick()
turtle.done()

mainloop()
