import random
import time


class Guessing_game:
    def __init__(self):
        # Computer Choice
        self.C_player1 = None
        self.C_player2 = None

        # User name
        self.player1_name = None
        self.player2_name = None

        # number of guess user took
        self.num_guess_player1 = 0
        self.num_guess_player2 = 0

    @staticmethod
    def rules():
        print("\nRules of the game:")
        print("- In this game 2 plyer has to gusee number. ")
        time.sleep(1)
        print(
            "- Which-ever plyer is has less number of guess to find number that plyer is winner"
        )
        time.sleep(1)

    def manu(self):
        print(f"\nWelcome to this game")
        time.sleep(1)
        print(f'It\'s name is "THE PERFECT GUESS"')
        time.sleep(1)

        rule = (
            input(f"\nDo you wish to know rules of the game (Y,y/N,n) : ")
            .strip()
            .lower()
        )

        if rule == "y":
            self.rules()

        choice = input(f"\nDo you wish to Start Game (Y,y/N,n) : ").strip().lower()

        if choice == "y":
            self.start()
        else:
            self.exit()

    def start(self):
        print("\n----------------- Game is starting ----------------- ")
        self.C_player1 = random.randint(1, 100)
        self.C_player2 = random.randint(1, 100)
        self.f_player1()

    def f_player1(self):
        self.player1_name = input("\nPlayer 1 Enter Your name : ").capitalize().strip()
        geme_start = (
            input(
                f"PLayer 1 Name : {self.player1_name} \n\nAre you ready to play (Y,y/N,n) : "
            )
            .strip()
            .lower()
        )

        self.num_guess_player1 = self.logic(
            geme_start, self.C_player1, self.player1_name
        )
        self.f_player2()

    def f_player2(self):
        self.player2_name = input("\nPlayer 2 Enter Your name : ").capitalize().strip()
        geme_start = (
            input(
                f"PLayer 2 Name : {self.player2_name} \n\n\nAre you ready to play (Y,y/N,n) : "
            )
            .strip()
            .lower()
        )

        self.num_guess_player2 = self.logic(
            geme_start, self.C_player2, self.player2_name
        )
        self.winner()

    def logic(self, x, target_num, plyer_name):
        num_guess = 0
        if x == "y":
            print("\nWelcome New Plyer ", end="", flush=True)
            time.sleep(1)

            for i in range(random.randint(5, 15)):
                time.sleep(0.7)
                print(".", end="", flush=True)

            while True:
                while True:
                    try:
                        guess = int(input(f"\nPLyer {plyer_name} Enter Number : "))
                        break
                    except ValueError:
                        print("Enter Whole Number (Ex : 5 , 7, 8)")

                if (target_num) == guess:
                    print("you have guessed Right")
                    num_guess += 1
                    break

                elif (target_num) > guess:
                    num_guess += 1
                    print("Go higher")

                elif (target_num) < guess:
                    num_guess += 1
                    print("Go lower")

                else:
                    print("Error")

        else:
            self.exit()

        return num_guess

    def winner(self):

        print("\nNumber of guess :")
        time.sleep(3)

        print(f"\tPlayer 1 {self.player1_name} : {self.num_guess_player1}")
        time.sleep(3)

        print(f"\tPlayer 2 {self.player2_name} : {self.num_guess_player2}")

        if self.num_guess_player1 < self.num_guess_player2:
            print(f"\n{self.player1_name} is Winner")

        elif self.num_guess_player1 > self.num_guess_player2:
            print(f"\n{self.player2_name} is Winner")

        else:
            print("\nIt's Draw")

        reset = input(f"\nDo you play again (Y,y/N,n) : ").strip().lower()

        if reset == "y":
            self.start()
        else:
            self.exit()

    @staticmethod
    def exit():
        print("Exiting game ", end="", flush=True)
        time.sleep(1)
        for i in range(5):
            time.sleep(0.8)
            print(".", end="", flush=True)


number = Guessing_game()
number.manu()
