import sys
from random import randint
from random import choice
from time import sleep
import turtle

window = turtle.Screen()
window.setup(width=800, height=800)
window.title("Turtle Race!")

# create Turtle objects to draw stuff on screen
# NOTE: these will NOT be the turtles that race!
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

# change the color
t1.color("white")

# take the pen off of the page to prevent the turtle from being able to draw
t1.penup()

# hide the turtle object
t1.ht()


def game_menu():
    """Draws the game menu.

    The menu pops up when the Player starts the game AND after they lose all their money
    """

    t1.clear()
    t2.clear()
    t3.clear()

    turtle.bgcolor("black")

    t1.setpos(-250, 300)
    t1.write("Turtle Race Betting: ", font=("Arial", 50, "bold"))

    t1.setpos(-160, -200)
    t1.write("press SPACE to play...", font=("Arial", 30, "bold"))

    t1.setpos(-160, -300)
    t1.write("press ESCAPE to quit...", font=("Arial", 30, "bold"))

    t1.setpos(-30, 100)

    t1.shape("turtle")
    t1.color("forest green")
    t1.shapesize(10, 10, 10)
    t1.st()

    turtle.listen() # listen for user events

    turtle.onkey(run, 'space')
    turtle.onkey(close, 'Escape')

    turtle.mainloop()


def close():
    """Closes the program

    NOTE: This only happens if the user presses the ESCAPE key when prompted to
    """
    sys.exit()


def run():
    """Runs the bulk of the program

    NOTE: this only happens if the user presses the SpaceBar when prompted to
    """

    # clear the turtle object's drawings from before
    t1.clear()

    # hide the turtle object and decrease its size
    t1.shapesize(1.0, 1.0, 1)
    t1.ht()

    turtle.bgcolor("forest green")

    # Change the color
    t1.color("chocolate")

    # 0 is the fastest speed
    t1.speed(0)

    # take the pen off the page so the turtle does not draw when it is moving position
    t1.penup()

    # DIRT
    t1.setpos(-300, -280)
    t1.begin_fill()
    t1.pendown()

    for i in range(2):
        t1.forward(650)
        t1.left(90)
        t1.forward(400)
        t1.left(90)

    t1.end_fill()
    t1.penup()

    # FINISH LINE
    gap_size = 20
    t1.shape("square")
    t1.penup()

    # white squares (COLUMN 1)
    t1.color("white")
    for i in range(10):
        t1.goto(320, 110 - (i * gap_size * 2))
        t1.stamp()

    # white squares (COLUMN 2)
    for i in range(10):
        t1.goto(320 + gap_size, (110 - gap_size) - (i * gap_size * 2))
        t1.stamp()

    # black squares (COLUMN 1)
    t1.color("black")
    for i in range(10):
        t1.goto(320, (110 - gap_size) - (i * gap_size * 2))
        t1.stamp()

    # black squares (COLUMN 2)
    for i in range(10):
        t1.goto(320 + gap_size, 110 - (i * gap_size * 2))
        t1.stamp()

    # change color back to white
    t1.color("white")

    # Money to spend
    money = 5000

    # customize second turtle object
    t2.color("white")
    t2.speed(0)
    t2.ht()
    t2.penup()

    # Display cash to spend
    t1.setpos(-375, 350)
    t1.write("Money left: ", font=("Arial", 20, "underline"))
    t2.setpos(-260, 350)
    t2.write("${}".format(money), font=("Arial", 20, "bold"))

    # First-Place Choice and Bet
    t1.setpos(150, 350)
    t1.write("First-Place Choice: ", font=("Arial", 20, "underline"))
    t1.setpos(200, 300)
    t1.write("Bet: ", font=("Arial", 20, "underline"))

    # Write the numbers that correspond to each turtle
    t1.setpos(-325, 80)
    t1.write("1", font=("Arial", 30, "bold"))

    t1.setpos(-325, 30)
    t1.write("2", font=("Arial", 30, "bold"))

    t1.setpos(-325, -20)
    t1.write("3", font=("Arial", 30, "bold"))

    t1.setpos(-325, -70)
    t1.write("4", font=("Arial", 30, "bold"))

    t1.setpos(-325, -120)
    t1.write("5", font=("Arial", 30, "bold"))

    t1.setpos(-325, -170)
    t1.write("6", font=("Arial", 30, "bold"))

    t1.setpos(-325, -220)
    t1.write("7", font=("Arial", 30, "bold"))

    t1.setpos(-325, -270)
    t1.write("8", font=("Arial", 30, "bold"))

    t1.setpos(-390, 120)
    t1.write("Odds:", font=("Arial", 20, "underline"))

    # Create the turtle objects for the race

    # Turtle 1
    turtle_1 = turtle.Turtle()
    turtle_1.ht()
    turtle_1.shape("turtle")
    turtle_1.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_1.penup()
    turtle_1.goto(-280, 100)

    # Turtle 2
    turtle_2 = turtle.Turtle()
    turtle_2.ht()
    turtle_2.shape("turtle")
    turtle_2.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_2.penup()
    turtle_2.goto(-280, 50)

    # Turtle 3
    turtle_3 = turtle.Turtle()
    turtle_3.ht()
    turtle_3.shape("turtle")
    turtle_3.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_3.penup()
    turtle_3.goto(-280, 0)

    # Turtle 4
    turtle_4 = turtle.Turtle()
    turtle_4.ht()
    turtle_4.shape("turtle")
    turtle_4.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_4.penup()
    turtle_4.goto(-280, -50)

    # Turtle 5
    turtle_5 = turtle.Turtle()
    turtle_5.ht()
    turtle_5.shape("turtle")
    turtle_5.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_5.penup()
    turtle_5.goto(-280, -100)

    # Turtle 6
    turtle_6 = turtle.Turtle()
    turtle_6.ht()
    turtle_6.shape("turtle")
    turtle_6.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_6.penup()
    turtle_6.goto(-280, -150)

    # Turtle 7
    turtle_7 = turtle.Turtle()
    turtle_7.ht()
    turtle_7.shape("turtle")
    turtle_7.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_7.penup()
    turtle_7.goto(-280, -200)

    # Turtle 8
    turtle_8 = turtle.Turtle()
    turtle_8.ht()
    turtle_8.shape("turtle")
    turtle_8.shapesize(stretch_len=1.25, stretch_wid=1.25)
    turtle_8.penup()
    turtle_8.goto(-280, -250)

    turtle_list = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8]

    for t in turtle_list:
        t.speed(0.49)

    waiting = True

    while waiting:
        while money > 0:

            # Turtle colors to cycle through
            color_list = ["white", "gray", "black", "blue", "deep sky blue", "cyan", "teal", "aquamarine", "green",
                          "lime",
                          "olive", "yellow", "orange", "red", "purple", "magenta", "blue violet", "indigo"]

            # assign random colors to each turtle
            color_1 = choice(color_list)
            turtle_1.color(color_1)
            turtle_1.st()
            color_list.remove(color_1)

            color_2 = choice(color_list)
            turtle_2.color(color_2)
            turtle_2.st()
            color_list.remove(color_2)

            color_3 = choice(color_list)
            turtle_3.color(color_3)
            turtle_3.st()
            color_list.remove(color_3)

            color_4 = choice(color_list)
            turtle_4.color(color_4)
            turtle_4.st()
            color_list.remove(color_4)

            color_5 = choice(color_list)
            turtle_5.color(color_5)
            turtle_5.st()
            color_list.remove(color_5)

            color_6 = choice(color_list)
            turtle_6.color(color_6)
            turtle_6.st()
            color_list.remove(color_6)

            color_7 = choice(color_list)
            turtle_7.color(color_7)
            turtle_7.st()
            color_list.remove(color_7)

            color_8 = choice(color_list)
            turtle_8.color(color_8)
            turtle_8.st()
            color_list.remove(color_8)

            # contains the payouts for each turtle
            payout_list = []

            # contains the wagers for each turtle
            wager_list = []

            # Give the betting odds for each turtle
            starting_y_coordinate = 85
            for i in range(8):
                payout = randint(1, 3)
                wager = randint(1, 3)

                # simplify payout-wager fraction if both numbers are the same
                if (payout == 2 and wager == 2) or (payout == 3 and wager == 3):
                    payout = 1
                    wager = 1

                payout_list.append(payout)
                wager_list.append(wager)

                t2.setpos(-375, starting_y_coordinate - (i * 50))
                t2.write("{}-{}".format(payout, wager), font=("Arial", 20, "bold"))

            index = 0
            winner = "UNDECIDED"
            turtle_list = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7,
                           turtle_8]

            # First-Place Choice
            first_place = input("Enter the number of your choice for 1st place: ")

            valid_inputs = ["1", "2", "3", "4", "5", "6", "7", "8"]

            while first_place not in valid_inputs:
                print("Invalid choice.")
                first_place = input("Enter the number of your choice for 1st place: ")

            t2.setpos(350, 350)
            t2.write("#{}".format(first_place), font=("Arial", 20, "bold"))

            # Betting
            bet = float(input("How much money would you like to bet on this turtle? "))

            while bet <= 0 or bet > money:
                print("Invalid amount.")
                bet = float(input("How much money would you like to bet on this turtle? "))

            # round the bet to 2 decimal places
            bet = round(bet, 2)

            t2.setpos(250, 300)
            t2.write("${}".format(bet), font=("Arial", 20, "bold"))

            # customize third Turtle object
            t3.color("white")
            t3.speed(0)
            t3.ht()
            t3.penup()

            # pause before racing and print countdown on screen
            seconds = 3
            while seconds > 0:
                t3.setpos(-50, 180)
                t3.write("{}...".format(seconds), font=("Arial", 50, "bold"))
                sleep(1)
                seconds -= 1
                t3.clear()

            t3.setpos(-100, 180)
            t3.write("Race!".format(seconds), font=("Arial", 50, "bold"))

            num = 30

            finish = 320

            # move the turtles
            while turtle_1.xcor() < finish and turtle_2.xcor() < finish and turtle_3.xcor() < finish \
                    and turtle_4.xcor() < finish and turtle_5.xcor() < finish and turtle_6.xcor() < finish \
                    and turtle_7.xcor() < finish and turtle_8.xcor() < finish:
                turtle_1.forward((wager_list[0] / payout_list[0] + randint(1, num)))
                turtle_2.forward((wager_list[1] / payout_list[1] + randint(1, num)))
                turtle_3.forward((wager_list[2] / payout_list[2] + randint(1, num)))
                turtle_4.forward((wager_list[3] / payout_list[3] + randint(1, num)))
                turtle_5.forward((wager_list[4] / payout_list[4] + randint(1, num)))
                turtle_6.forward((wager_list[5] / payout_list[5] + randint(1, num)))
                turtle_7.forward((wager_list[6] / payout_list[6] + randint(1, num)))
                turtle_8.forward((wager_list[7] / payout_list[7] + randint(1, num)))

            # Used to determine the winner
            if turtle_1.xcor() >= finish:
                index = 0
                winner = color_1
            elif turtle_2.xcor() >= finish:
                index = 1
                winner = color_2
            elif turtle_3.xcor() >= finish:
                index = 2
                winner = color_3
            elif turtle_4.xcor() >= finish:
                index = 3
                winner = color_4
            elif turtle_5.xcor() >= finish:
                index = 4
                winner = color_5
            elif turtle_6.xcor() >= finish:
                index = 5
                winner = color_6
            elif turtle_7.xcor() >= finish:
                index = 6
                winner = color_7
            elif turtle_8.xcor() >= finish:
                index = 7
                winner = color_8

            # Clear the "RACE!" message from before
            t3.clear()

            # Display the winner
            t3.setpos(-150, 180)
            t3.write("The {} turtle wins!".format(winner), font=("Arial", 30, "italic"))

            # celebration of the winner
            for i in range(72):
                turtle_list[index].right(5)
                turtle_list[index].shapesize(stretch_wid=2, stretch_len=2)

            turtle_list[index].shapesize(stretch_wid=1.25, stretch_len=1.25)

            # Remove first place choice, bet, and money
            t2.clear()

            # Remove the winner banner
            t3.clear()

            # calculate how much money the player wins or loses
            if index + 1 == int(first_place):
                profit = bet * (payout_list[index] / wager_list[index])
                profit = round(profit, 2)
                money += profit
                money = round(money, 2)
                t3.setpos(-125, 180)
                t3.write("You won ${}!".format(profit), font=("Arial", 30, "bold"))
                sleep(3)
                t3.clear()

            else:
                money -= bet
                money = round(money, 2)
                t3.setpos(-125, 180)
                t3.write("You lost ${}.".format(bet), font=("Arial", 30, "bold"))
                sleep(3)
                t3.clear()

            # Display cash remaining
            t2.setpos(-260, 350)
            t2.write("${}".format(money), font=("Arial", 20, "bold"))

            # Move the turtles back to their starting positions
            turtle_1.ht()
            turtle_1.goto(-280, 100)

            turtle_2.ht()
            turtle_2.goto(-280, 50)

            turtle_3.ht()
            turtle_3.goto(-280, 0)

            turtle_4.ht()
            turtle_4.goto(-280, -50)

            turtle_5.ht()
            turtle_5.goto(-280, -100)

            turtle_6.ht()
            turtle_6.goto(-280, -150)

            turtle_7.ht()
            turtle_7.goto(-280, -200)

            turtle_8.ht()
            turtle_8.goto(-280, -250)

        t3.setpos(-150, 180)
        t3.write("GAME OVER!", font=("Arial", 50, "bold"))

        sleep(3)

        game_menu()

        # prevents the window from being closed if the user loses all of their money
        turtle.done()


game_menu() # initiates the program



