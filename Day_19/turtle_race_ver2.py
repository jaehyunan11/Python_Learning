from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
# keyword function
screen.setup(width=500, height=400)
user1_name = screen.textinput(title="NIM", prompt="Name of first player: ")
user1_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n Red, Yellow, Green, Blue, Purple, Orange ")
user2_name = screen.textinput(title="NIM", prompt="Name of second player: ")
user2_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n Red, Yellow, Green, Blue, Purple, Orange ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed('normal')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user1_bet and user2_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user1_bet:
                print(f"{user1_name} won! The {winning_color} turtle is the winner!")
            elif winning_color == user2_bet:
                print(f"{user2_name} won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've both lost! The {winning_color} turtle is the winner!")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()