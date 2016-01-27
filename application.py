"BATTLESHIP"

import random
import os
import sys
import time

class GameBattle(object):
    def __init__(self):
        self.board_player_one = []
        self.board_player_one_to_check = []

    def clear():
        if os.name == ("posix"):
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system("cls")

    def clean_list(self):
        del self.board_player_one[:]
        del self.board_player_one_to_check[:]

    #---------------------------------------------------
    def generate_board_player_one_to_check(self):
        for l in range(0, 10):
            self.board_player_one_to_check.append(["-"] * 10)

    def print_board_player_one_to_check(self):
        for o in self.board_player_one_to_check:
            print "|" + "|".join(o) + "|"

    #---------------------------------------------------
    def generate_board_player_one(self):
        for l in range(0, 10):
            self.board_player_one.append(["-"] * 10)

    def print_board_player_one(self):
        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.board_player_one:
            print "|" + "|".join(o) + "|" + str(number)
            number +=1

    #----------------------------------------------------
class SinglePlayer(GameBattle):    

    def valid_guess_given_by_user(self):
        while True:
            try:
                guess_row = raw_input("Guess The Row: ")
                guess_row = int(guess_row)
                guess_column = raw_input("Guess The Column: ")
                guess_column = int(guess_column)
                return guess_row, guess_column
            except ValueError:
                self.clear()
                print "Only Can Insert Numbers"
        return guess_row, guess_column

    def player_alone(self):
        self.generate_board_player_one_to_check()
        self.generate_board_player_one()
        row_bomb, column_bomb = self.valid_position_bomb("aleatory")
        row_ship_two_horizontal, column_ship_two_horizontal = self.valid_position_ship_two_horizontal("aleatory")
        row_ship_two_vertical, column_ship_two_vertical = self.valid_position_ship_two_vertical("aleatory")
        row_ship_three_horizontal, column_ship_three_horizontal = self. valid_position_ship_three_horizontal("aleatory")
        row_ship_three_vertical, column_ship_three_vertical = self.valid_position_ship_three_vertical("aleatory")
        row_ship_four_horizontal, column_ship_four_horizontal = self.valid_position_ship_four_horizontal("aleatory")
        row_ship_four_vertical, column_ship_four_vertical = self.valid_position_ship_four_vertical("aleatory")
        """print "BOMB"
        print row_bomb, column_bomb
        print "SHIP OF TWO H"
        print row_ship_two_horizontal, column_ship_two_horizontal
        print "SHIP OF TWO V"
        print row_ship_two_vertical, column_ship_two_vertical
        print "SHIP OF THREE H"
        print row_ship_three_horizontal, column_ship_three_horizontal
        print "SHIP OF THREE V"
        print row_ship_three_vertical, column_ship_three_vertical
        print "SHIP OF FOUR H"
        print row_ship_four_horizontal, column_ship_four_horizontal
        print "SHIP OF FOUR V"
        print row_ship_four_vertical, column_ship_four_vertical
        time.sleep(2)
        self.clear()"""
        life = 0
        while life <= 10:
            self.print_players("1")
            self.print_board_player_one()
            guess_row, guess_column = self.valid_guess_given_by_user()
            if guess_row == row_bomb and guess_column == column_bomb:
                self.board_player_one[guess_row-1][guess_column-1] = "#"
                self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "A"
                self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal] = "A"
                self.board_player_one[row_ship_two_vertical-1][column_ship_two_vertical-1] = "B"
                self.board_player_one[row_ship_two_vertical][column_ship_two_vertical-1] = "B"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "C"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal] = "C"
                self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "C"
                self.board_player_one[row_ship_three_vertical-1][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_three_vertical][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_three_vertical+1][column_ship_three_vertical-1] = "D"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "E"
                self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "E"
                self.board_player_one[row_ship_four_vertical-1][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical+1][column_ship_four_vertical-1] = "F"
                self.board_player_one[row_ship_four_vertical+2][column_ship_four_vertical-1] = "F"
                self.clear()
                time.sleep(2)
                self.print_players("1w")
                self.print_board_player_one()
                raw_input("PRES ENTER")
                self.clean_list()
                self.clear()
                time.sleep(1)
                self.play_again_alone()
            else:
                if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                    self.clear()
                    time.sleep(2)
                    print "IT IS NOT IN THE OCEAN"
                    life +=1
                    print "YOU STILL HAVE %d LIVES, COME ON, YOU CAN SINK THE SHIPS" % (10-life)
                elif self.board_player_one[guess_row-1][guess_column-1] == "X" or self.board_player_one[guess_row-1][guess_column-1] == "A"\
                or self.board_player_one[guess_row-1][guess_column-1] == "B" or self.board_player_one[guess_row-1][guess_column-1] == "C"\
                or self.board_player_one[guess_row-1][guess_column-1] == "D" or self.board_player_one[guess_row-1][guess_column-1] == "E"\
                or self.board_player_one[guess_row-1][guess_column-1] == "F":
                    self.reset()
                    time.sleep(2)
                    print"ALREADY YOU HAVE WRITTEN THOSE COODINATES"
                    life +=1
                    print "YOU STILL HAVE %d LVIES, COME ON, YOU CAN SNICK THE SHIPS" % (10-life)
                elif guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal\
                or guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal+1:
                    self.board_player_one[guess_row-1][guess_column-1] = "A"
                    self.reset()
                    time.sleep(1)
                elif guess_row == row_ship_two_vertical and guess_column == column_ship_two_vertical\
                or guess_row == row_ship_two_vertical+1 and guess_column == column_ship_two_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "B"
                    self.reset()
                    time.sleep(1)
                elif guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+1\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+2:
                    self.board_player_one[guess_row-1][guess_column-1] = "C"
                    self.reset()
                    time.sleep(1)
                elif guess_row == row_ship_three_vertical and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+1 and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+2 and guess_column == column_ship_three_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "D"
                    self.reset()
                    time.sleep(1)
                elif guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+1\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+2\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+3:
                    self.board_player_one[guess_row-1][guess_column-1] = "E"
                    self.reset()
                    time.sleep(1)
                elif guess_row == row_ship_four_vertical and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+1 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+2 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+3 and guess_column == column_ship_four_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "F"
                    self.reset()
                    time.sleep(1)
                else:
                    self.board_player_one[guess_row-1][guess_column-1] = "X"
                    self.reset()
                    time.sleep(1)
                    print "TRY AGAIN"
                    life+=1
                    print "YOU STILL HAVE %d LIVES, COME ON, YOU CAN SNICK THE SHIPS" % (10-life)
            if self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "A" and self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal] == "A"\
            and self.board_player_one[row_ship_two_vertical-1][column_ship_two_vertical-1] == "B" and self.board_player_one[row_ship_two_vertical][column_ship_two_vertical-1] == "B"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "C" and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal] == "C"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "C" and self.board_player_one[row_ship_three_vertical-1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_three_vertical][column_ship_three_vertical-1] == "D" and self.board_player_one[row_ship_three_vertical+1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal] == "E"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "E"\
            and self.board_player_one[row_ship_four_vertical-1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical][column_ship_four_vertical-1] == "F"\
            and self.board_player_one[row_ship_four_vertical+1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical+2][column_ship_four_vertical-1] == "F":
                self.clear()
                time.sleep(2)
                print "YOU HAVE SUNK ALL THE SHIPS"
                self.print_players("1w")
                self.print_board_player_one()
                raw_input("PRESS ENTER")
                self.clean_list()
                self.clean_list()
                time.sleep(2)
                self.play_again_alone()
            if life == 10:
                self.clear()
                time.sleep(2)
                print """
__   _____  _   _   _    ___  ___ ___ 
\ \ / / _ \| | | | | |  / _ \/ __| __|
 \ V / (_) | |_| | | |_| (_) \__ \ _| 
  |_| \___/ \___/  |____\___/|___/___|
                                      """
                raw_input("PRESS ENTER")
                self.clear()
                time.sleep(2)
                self.play_again_alone()

    def play_again_alone(self):
        while True:
            time.sleep(2)
            choose_user = raw_input("Do You Want To Play Again Y/N")
            choose_user = choose_user.lower()
            if choose_user == "Y" or choose_user == "y":
                self.clean_list()
                self.clear()
                time.sleep(1)
                self.player_alone()
            elif choose_user == "N" or choose_user =="n":
                self.clean_list()
                time.sleep(2)
                self.clear()
                self.menu()
            else:
                self.clear()
                time.sleep(2)
                print "Only Can Write Y/N"


    def menu_print(self):
        print "WELCOME TO BATTLESHIP"
        print "1. SINGLE PLAYER"
        print "2. TWO PLAYERS"
        print "3. INSTRUCTIONS"
        print "4. EXIT"

    def menu_option(self):
        while True:
            choose_user = raw_input(" - ")
            if choose_user ==  "1":
                self.clear()
                self.player_alone()
            if choose_user == "4":
                self.clear()
                sys.exit()
            else:
                self.reset()
                print "Invalid Option"
                self.menu()

    def menu(self):
        self.menu_print()
        self.menu_option()

MAIN.menu()
