# Graphich Circle
from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(360):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.9)
    right(5)
    forward(3)
done()