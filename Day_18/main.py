import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
colors = ["blue", "chartreuse", "dark magenta", "linen", "dark gray", "cornflower blue", "gold"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for share_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(share_side_n)




# from turtle import Turtle
from random import randint

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# def square():
#     for _ in range(4):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(90)
#
# square()
#
# screen = Screen()
# screen.exitonclick()



