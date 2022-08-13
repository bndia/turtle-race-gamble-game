import turtle as t
from turtle import Screen
import random
from new_turtle import NewTurtle

colors = ["red", "orange", "yellow", "green", "purple"]



def create_turtle(num_of_turtles):
    turtles = []
    while len(turtles) < num_of_turtles:
        turtle_color = random.choice(colors)
        turtle = NewTurtle(t.Turtle("turtle"), turtle_color)
        print(turtle.the_turtle.color)
        turtles.append(turtle)
        colors.remove(turtle_color)
        turtles[len(turtles) - 1].the_turtle.color(turtle_color)
        turtles[len(turtles) - 1].the_turtle.penup()
        turtles[len(turtles) - 1].the_turtle.shapesize(2, 2, 3)
    return turtles

def check_bet(user_bet):
    pass




def start_race(turtles, screen_width, screen_height):
    i = 0
    winner = ""
    is_race_on = False
    y_position = len(turtles)*75/2
    screen = Screen()
    screen.setup(screen_width, screen_height)
    while i < len(turtles):
        turtles[i].the_turtle.goto(x=-(screen_width/2)+20, y=y_position)
        y_position -= 75
        i += 1
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in turtles:
            turtle.the_turtle.forward(random.randint(0, 10))
            turtle_position = turtle.the_turtle.xcor()
            finish_line = (screen_width/2)-35
            print(f"turtle {turtle.the_turtle_color} position: {turtle_position} / {finish_line}")
            if turtle_position >= finish_line:
                winner = turtle.the_turtle_color
                is_race_on = False
    if (user_bet.lower() == winner.lower()):
        print("You won!!!")
    else:
        print("You lost.")

    screen.exitonclick()
