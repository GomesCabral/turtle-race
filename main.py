from turtle import Turtle, Screen
import random


my_screen = Screen()
is_race_on = False
all_turtles = []

#SCREEN SIZE
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "green", "orange", "yellow", "blue", "purple"]
y_positions = [-60, -30, 0, 30, 60, 90]


#CREATE 6 TURTLES WITH DIFFERENT COLORS AND POSITIONS
for turtle in range(0, 6):
    heni = Turtle("turtle")
    heni.penup()
    heni.color(random.choice(colors))
    heni.goto(x=-240, y=y_positions[turtle])
    all_turtles.append(heni)

#CHECK IF THE USER COLOR EXIST
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've Won! {winner} turtle is the winner!")
            else:
              print(f"You've Lost! {winner} turtle is the winner!")  

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



my_screen.exitonclick()