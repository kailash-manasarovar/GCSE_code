import time
import random
import sys
from random import randint

# these are the only global variables in the code, we access them by redefining them as global in the functions
pname1 = ""
pname2 = ""


def signin():
    enter = 0
    tries = 0
    while enter == 0:
        file = open("user_accounts.txt", "r")
        name = input("please enter username:")
        password = input('Please enter password:')
        for line in file:
            data = line.split(",")
        if name == data[0] and password == data[1]:
            print("You have now logged into the system. Welcome", name,
                  "!")
            rolls = 0
            enter = 1 + enter
        elif tries == 3:
            print("Ops, you have entered the password wrong too many times.")
            print("You have been locked out for 10 minutes")
            time.sleep(600)
            tries = 0
        else:
            print("\nThis is an incorrect username or password please try again")
            tries = 1 + tries

# players Usernames
def set_usernames():
    global pname1
    global pname2
    print('\n')
    pname1 = input("\nWhat does player 1 want to be called?")
    pname2 = input("\nWhat does player 2 want to be called?")
    print("welcome", pname1, ",and welcome", pname2, ",to the two player dice game")

# players selections
def select_option():
    # select an option
    print("\n")
    print("please select an option.")
    print("1: Enter the game")
    print("2: Rules")
    print("3: Exit")
    opt = input("What would you like to do, please select a number:")

    while int(opt) < 1 or int(opt) > 4:
        print("That is not a valid option.")
        print("Please enter a number between 1 and 4:")
        opt = input()

    # game rules

    if opt == "2":
        print("\nRules")
        print(
            "The dice game is a very simple game to understand: Two players take turns to roll two dices. They both roll the dice twice over 5 rounds. whoever has the highest even number at the end of the rounds wins. If both players have the same score at the end of the 5 rounds, they will each roll one more dice and whoever has the highest score after this will be the winner")

    # exit the game
    elif opt == "3":
        time.sleep(0.3)
        print("\n")
        print("now exiting the game")
        sys.exit()

    # This is the game code

    elif opt == "1":

        time.sleep(0.3)
    print("Hello players!")
    play_game()


# game loops
def play_game():
    rounds = 0
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    odd = [3, 5, 7, 9, 11, 13, 15, 17]
    rolling = 0
    rolls = 0
    p1go = 0
    p2go = 0

    while rounds < 5:
        while rolling == 0:
            p1 = input("\nPlayer 1 press r to roll.")
            if p1 == "r":
                p1roll1 = random.randint(1, 6)
                p1roll2 = random.randint(1, 6)
                p1roll3 = p1roll1 + p1roll2
                print("Dice 1 rolled a", p1roll1, ".")
                print("Dice 2 rolled a", p1roll2, ".")
                print("Player 1 your roll was a", p1roll3, ".")
                rolling = 1

        while rolls == 0:
            if p1roll1 == p1roll2:
                print("You got a double. You get one more roll.")
                double = random.randint(1, 6)
                p1roll3 = p1roll3 + double
                print("The double dice rolled a", double, ".")
                print("You got", p1roll3, ".")

            # Rolls an odd

            if p1roll3 in odd:
                p1go = p1go + p1roll3 - 5
                print(
                    "You rolled a odd number 5 points have been removed from your score.  You now have",
                    p1go, "points.")
                rolls = 1
                droll = 0
                rolling = 0
            elif p1go in [3, 5]:
                print(
                    "You rolled a odd number 5 points have been removed from your score. You now have",
                    p1go, "points.")
                rolls = 1
                droll = 0
                rolling = 0
            elif p1roll3 in even:
                p1go = p1go + p1roll3 + 10
                print(
                    "You rolled a even number 10 points have been added to your score. You now have",
                    p1go, "points.")
                rolls = 1
                droll = 0
                rolling = 0

        while rolling == 0:
            p2 = input("\nPlayer 2 press r to roll.")
            if p2 == "r":
                p2roll1 = random.randint(1, 6)
                p2roll2 = random.randint(1, 6)
                p2roll3 = p2roll1 + p2roll2
                print("Dice 1 rolled a", p2roll1, ".")
                print("Dice 2 rolled a", p2roll2, ".")
                print("Player 2 your roll was a", p2roll3, ".")
                rolling = 1

        while droll == 0:
            if p2roll1 == p2roll2:
                print("You got a double. You get one more roll.")
                double = random.randint(1, 6)
                p2roll3 = p2roll3 + double
                print("The double dice rolled a", double, ".")
                print("You got", p2roll3, ".")

            # Roll and odd

            if p2roll3 in odd:
                p2go = p2go + p2roll3 - 5
                print("You rolled a odd number 5 points have been removed from your score. You now have", p2go, "points.")
                rounds = rounds + 1
                droll = 1
                rolls = 0
                rollings = 0
            elif p2go in [3, 5]:
                print("You rolled a odd number 5 points have been removed from your score. You now have", p2go, "points.")
                rounds = rounds + 1
                droll = 1
                rolls = 0
                rolling = 0
            elif p2roll3 in even:
                p2go = p2go + p2roll3 + 10
                print("You rolled a even number 10 points have been added to your score. You now have", p2go, "points.")
                rounds = rounds + 1
                droll = 1
                rolls = 0
                rolling = 0
    check_scores(p1go, p2go)


# If the score is the same at the end
def check_scores(player1_score, player2_score):
    if player1_score == player2_score:
        p1 = input("Player 1 press r to roll")
        if p1 == "r":
            p1roll1 = random.randint(1, 6)
            p1roll2 = random.randint(1, 6)
            p1roll3 = p1roll1 + p1roll2
            print("Dice 1 rolled a", p1roll1, ".")
            print("Dice 2 rolled a", p1roll2, ".")
            print("Player 1 your roll was a", p1roll3, ".")
        p2 = input("Player 1 press r to roll")
        if p2 == "r":
            p2roll1 = random.randint(1, 6)
            p2roll2 = random.randint(1, 6)
            p2roll3 = p2roll1 + p2roll2
            print("Dice 1 rolled a", p2roll1, ".")
            print("Dice 2 rolled a", p2roll2, ".")
            print("Player 1 your roll was a", p2roll3, ".")
    print_final_scores(player1_score, player2_score)

# Final Scores
def print_final_scores(player1_score, player2_score):
    global pname1
    global pname2
    print("\nThe scores have been added up and")
    time.sleep(2)
    print('\n')
    print(pname1, "got", player1_score, ".")
    print(pname2, "got", player2_score, ".")


# run the game
signin()
set_usernames()
select_option()
play_game()