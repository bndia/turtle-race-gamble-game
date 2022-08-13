import the_game


valid_input = False

while not valid_input:
    num_of_turtles = int(input("Choose between 2 to 5 turtles to join the race: "))
    if 2 <= num_of_turtles <= 5:
        valid_input = True
    else:
        input("You must choose a number between 2 and 5, OK?")

the_turtles = the_game.create_turtle(num_of_turtles)
the_game.start_race(the_turtles, screen_width=800, screen_height=800)

