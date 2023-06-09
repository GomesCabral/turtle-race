from turtle import Turtle, Screen
import random


my_screen = Screen()


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






my_screen.exitonclick()