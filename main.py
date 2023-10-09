from colorgram import extract
from turtle import Turtle, Screen
from random import choice
display =Screen()
display.colormode(255)

color = extract("image.jpg", 10)
for i in range(len(color)):
    color[i] = tuple([color[i].rgb[0], color[i].rgb[1], color[i].rgb[2]])
print(color)

tim = Turtle()
tim.shape("turtle")
tim.hideturtle()
tim.speed(100)
tim.penup()
for lines in range(10):
    tim.setposition(x=-150, y=(-150+30*lines))
    for dots in range(10):
        tim.dot(15, choice(color))
        tim.forward(30)



display.exitonclick()



