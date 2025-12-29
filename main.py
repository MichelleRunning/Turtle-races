import random
from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)

# Ask user for their bet
user_bet = screen.textinput(
    title="Place your bets",
    prompt="Which turtle will win the race? Enter a color: "
)

# Turtle configuration
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
race_on = False

# Create turtles
for index in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[index])
    turtle.goto(x=-240, y=y_positions[index])
    all_turtles.append(turtle)

# Start race if user placed a bet
if user_bet:
    user_bet = user_bet.lower()
    race_on = True

# Race loop
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle won the race 🏆")
            else:
                print(f"You lose. The {winning_color} turtle won the race.")

            break

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
