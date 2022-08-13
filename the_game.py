import turtle as t
from turtle import Screen
import random

colors = ["red", "orange", "yellow", "green", "purple"]


def create_turtle(num_of_turtles):
    turtles = []
    while len(turtles) < num_of_turtles:
        turtle_color = random.choice(colors)
        turtle = t.Turtle("turtle")
        turtles.append(turtle)
        colors.remove(turtle_color)
        turtles[len(turtles) - 1].color(turtle_color)
        turtles[len(turtles) - 1].penup()
        turtles[len(turtles) - 1].shapesize(2, 2, 3)
    return turtles


def check_bet(user_bet, winner):
    if user_bet.lower() == winner.lower():
        print("You won!!!")
    else:
        print("You lost.")
    print(f"The winner is the {winner} turtle")


def start_race(turtles, screen_width, screen_height):
    i = 0
    winner = ""
    is_race_on = False
    y_position = len(turtles) * 75 / 2
    screen = Screen()
    screen.setup(screen_width, screen_height)
    while i < len(turtles):
        turtles[i].goto(x=-(screen_width / 2) + 20, y=y_position)
        y_position -= 75
        i += 1
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            turtle_position = turtle.xcor()
            finish_line = (screen_width / 2) - 35
            current_turtle_color = turtle.pencolor()
            print(f"turtle {current_turtle_color} position: {turtle_position} / {finish_line}")
            if turtle_position >= finish_line:
                winner = turtle.pencolor()
                is_race_on = False
    check_bet(user_bet, winner)

    screen.exitonclick()
