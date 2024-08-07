"""
Snake, Water, Gun Game

Description:
This program simulates the classic "Snake, Water, Gun" game, a variation of Rock, Paper, Scissors.
- Snake vs. Water: Snake drinks the water, hence wins.
- Water vs. Gun: The gun will drown in water, hence a point for water.
- Gun vs. Snake: Gun will kill the snake and win.

The user will play against the computer, which randomly chooses its option. The game will prompt the user to play again after each round and can display the rules if needed.

Author: Mishra Sandip (https://github.com/sandip3/)
Date: 25 - July - 2024
"""

# Dear maintainer:

# Once you are done trying to 'optimize' this routine, and have realized what a terrible mistake that was, please increment the following counter as a warning to the next guy:

# total_hours_wasted_here = 0

import random


def game_menu():
    play_choice = input("\nDo you want to PLay Game (Y/N) : ").strip().lower()

    if play_choice == "y":
        game_start()

    elif play_choice == "n":
        game_stop()

    else:
        print("\nInvalid choice")
        game_menu()


def game_start():

    print("\nInitializing Game .....")
    print("......")
    print("Done")
    print('Starting "Snake, Water, Gun" Game .... ')

    game_hint()
    game_play()


def game_stop():
    print("\nExiting Game ......")
    print("......")
    print("Done")


def game_hint():

    game_rules = (
        input("\nDo you wish to know the Rules of game (Y/N) : ").strip().lower()
    )

    if game_rules == "y":
        print("\nRules of the Game :")
        print("\t1. Snake vs. Water: Snake drinks the water hence wins.")
        print(
            "\t2. Water vs. Gun: The gun will drown in water, hence a point for water."
        )
        print("\t3. Gun vs. Snake: Gun will kill the snake and win.")
        print("")

    elif game_rules != "n":
        print("\nInvalid Choice")
        return


def game_play():

    print("\nPlease choose from the follwing options: ")
    print("1. Snake")
    print("2. Water")
    print("3. Gun")

    choice = {1: "Snake", 2: "Water", 3: "Gun"}

    player_choice = int(input("\nPlease select from above option (1/2/3) : "))
    computer_choise = int((random.random() * 3) + 1)

    if player_choice == 1 or player_choice == 2 or player_choice == 3:
        print(f"\nYou have choose : {choice[player_choice]}")
        print(f"Computer has choose : {choice[computer_choise]}")
        if player_choice == computer_choise:
            print("\nit's Draw")
        elif (
            (player_choice == 1 and computer_choise == 2)
            or (player_choice == 2 and computer_choise == 3)
            or (player_choice == 3 and computer_choise == 1)
        ):
            print('\nYou have "WON"')
        elif (
            (computer_choise == 1 and player_choice == 2)
            or (computer_choise == 2 and player_choice == 3)
            or (computer_choise == 3 and player_choice == 1)
        ):
            print('\nYou have "LOST"')
        else:
            print("\nInvalid Choice")
            game_play()
    else:
        print("\nInvalid Choice")
        game_play()

    game_reset()


def game_reset():

    game_reset = input("Do you wish to play again? (Y/N):").strip().lower()

    if game_reset == "y":
        game_play()

    elif game_reset == "n":
        game_stop()
    else:
        print("\nInvalid Choice")
        game_reset()


# Game starting Point
game_menu()
