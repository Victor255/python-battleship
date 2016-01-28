"Battleship"

import random
import os
import sys

class SinglePlayer(object):
    def __init__(self):
        self.board = []
        self.board_to_check = []

    def clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system("cls")

    def clear_lists(self):
        del self.board[:]
        del self.board_to_check[:]

    def press_enter(self):
        press = raw_input("\n\nPRESS ENTER PLEASE ")
        self.clear()
        self.menu()

    def generate_board_to_check(self):
        for lis in range(0, 10):
            self.board_to_check.append(["O"] * 10)

    def generate_board(self):
        for lista in range(0, 10):
            self.board.append(["O"] * 10)

    def print_board(self):
        for o in self.board:
            print " ".join(o)

    def valid_row_and_column_given_by_user(self):
        while True:
            try:
                guess_row = raw_input("\nGuess the row: ")
                guess_row = int(guess_row)
                guess_column = raw_input("Guess the column: ")
                guess_column = int(guess_column)
                return guess_row, guess_column
            except ValueError:
                self.clear()
                print "Only can insert integer numbers"
        return guess_row, guess_column

    def message(self):
        print "You have shot to a part of the ship"

    def valid_position_bomb(self):
        self.generate_board_to_check()
        row_bomb = random.randint(1, 10)
        column_bomb = random.randint(1, 10)
        bomb = True
        while bomb == True:
            if self.board_to_check[row_bomb-1][column_bomb-1] == "O":
                self.board_to_check[row_bomb-1][column_bomb-1] = "*"
                return row_bomb, column_bomb
                break
            elif self.board_to_check[row_bomb-1][column_bomb-1] == "*":
                row_bomb = random.randint(1, 10)
                column_bomb = random.randint(1, 10)
                bomb = True

    def valid_position_ship_two_horizontal(self):
        self.generate_board_to_check()
        row_ship_two_horizontal = random.randint(1,9)
        column_ship_two_horizontal = random.randint(1,9)
        ship2 = True
        while ship2 == True:
            if self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "O" and self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "O":
                self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                return row_ship_two_horizontal, column_ship_two_horizontal
                break
            elif self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                row_ship_two_horizontal = random.randint(1,9)
                column_ship_two_horizontal = random.randint(1,9)
                ship2 = True

    def valid_position_ship_two_vertical(self):
        self.generate_board_to_check()
        row_ship_two_vertical = random.randint(1,9)
        column_ship_two_vertical = random.randint(1,9)
        ship2 = True
        while ship2 == True:
            if self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "O" and self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical] == "O":
                self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                self.board_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                return row_ship_two_vertical, column_ship_two_vertical
                break
            elif self.board_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                row_ship_two_vertical = random.randint(1,9)
                column_ship_two_vertical = random.randint(1,9)
                ship2 = True
        return row_ship_two_vertical, column_ship_two_vertical

    def valid_position_ship_three_horizontal(self):
        self.generate_board_to_check()
        row_ship_three_horizontal = random.randint(1,8)
        column_ship_three_horizontal = random.randint(1,8)
        ship3 = True
        while ship3 == True:
            if self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "O" and self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "O"\
            and self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "O":
                self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                return row_ship_three_horizontal, column_ship_three_horizontal
                break
            elif self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
            or self.board_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                row_ship_three_horizontal = random.randint(1,8)
                column_ship_three_horizontal = random.randint(1,8)
                ship3 = True

    def valid_position_ship_three_vertical(self):
        self.generate_board_to_check()
        row_ship_three_vertical = random.randint(1,8)
        column_ship_three_vertical = random.randint(1,8)
        ship3 = True
        while ship3 == True:
            if self.board_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "O" and self.board_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "O"\
            and self.board_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "O":
                self.board_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                self.board_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                self.board_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                return row_ship_three_vertical, column_ship_three_vertical
                break
            elif self.board_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
            or self.board_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                row_ship_three_vertical = random.randint(1,8)
                column_ship_three_vertical = random.randint(1,8)
                ship3 = True

    def valid_position_ship_four_horizontal(self):
        self.generate_board_to_check()
        row_ship_four_horizontal = random.randint(1,7)
        column_ship_four_horizontal = random.randint(1,7)
        ship4 = True
        while ship4 == True:
            if self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "O" and self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "O"\
            and self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "O" and self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "O":
                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "*"
                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] = "*"
                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "*"
                self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "*" 
                return row_ship_four_horizontal, column_ship_four_horizontal
                break
            elif self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
            or self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":
                row_ship_four_horizontal = random.randint(1,7)
                column_ship_four_horizontal = random.randint(1,7)
                ship4 = True

    def valid_position_ship_four_vertical(self):
        self.generate_board_to_check()
        row_ship_four_vertical = random.randint(1,7)
        column_ship_four_vertical = random.randint(1,7)
        ship4 = True
        while ship4 == True:
            if self.board_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "O" and self.board_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "O"\
            and self.board_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "O" and self.board_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "O":
                self.board_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] = "*"
                self.board_to_check[row_ship_four_vertical][column_ship_four_vertical-1] = "*"
                self.board_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] = "*"
                self.board_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] = "*"
                return row_ship_four_vertical, column_ship_four_vertical
                break
            elif self.board_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
            or self.board_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":
                row_ship_four_vertical = random.randint(1,7)
                column_ship_four_vertical = random.randint(1,7)
                ship4 = True

    def guess_ship_user(self, guess_row, guess_column, row_bomb, column_bomb):
        self.generate_board_to_check()
        if guess_row == row_bomb and guess_column == column_bomb:
            self.board[guess_row-1][guess_column-1] = "#"
            self.clear()
            return True

    def ask_to_the_user(self):
        self.generate_board_to_check()
        self.generate_board()
        row_bomb, column_bomb = self.valid_position_bomb()
        row_ship_two_horizontal, column_ship_two_horizontal = self.valid_position_ship_two_horizontal()
        row_ship_two_vertical, column_ship_two_vertical = self.valid_position_ship_two_vertical()
        row_ship_three_horizontal, column_ship_three_horizontal = self. valid_position_ship_three_horizontal()
        row_ship_three_vertical, column_ship_three_vertical = self.valid_position_ship_three_vertical()
        row_ship_four_horizontal, column_ship_four_horizontal = self.valid_position_ship_four_horizontal()
        row_ship_four_vertical, column_ship_four_vertical = self.valid_position_ship_four_vertical()
        print "bomb"
        print row_bomb, column_bomb
        while True:
            guess_row, guess_column = self.valid_row_and_column_given_by_user()
            if guess_row == row_bomb and guess_column == column_bomb:
                self.board[guess_row-1][guess_column-1] = "#"
                self.clear()
                self.print_board()
                print "You have shot to the bomb, and You have sunk all the ships"
                print "You win"
                self.clear_lists()
                self.press_enter()
            else:
                if guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal+1\
                and guess_row == row_ship_two_vertical and guess_column == column_ship_two_vertical and guess_row == row_ship_two_vertical+1 and guess_column == column_ship_two_vertical\
                and guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal and guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+1\
                and guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+2 and guess_row == row_ship_three_vertical and guess_column == column_ship_three_vertical\
                and guess_row == row_ship_three_vertical+1 and guess_column == column_ship_three_vertical and guess_row == row_ship_three_vertical+2 and guess_column == column_ship_three_vertical\
                and guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal and guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+1\
                and guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+2 and guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+3\
                and guess_row == row_ship_four_vertical and guess_column == column_ship_four_vertical and guess_row == row_ship_four_vertical+1 and guess_column == column_ship_four_vertical\
                and guess_row == row_ship_four_vertical+2 and guess_column == column_ship_four_vertical and guess_row == row_ship_four_vertical+3 and guess_column == column_ship_four_vertical:
                    self.clear()
                    self.print_board()
                    print "You win"
                    self.clear_lists()
                    self.press_enter()
                else:
                    if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                        self.clear()
                        print "It is not in the ocean\n\n"
                        self.print_board()
                    elif self.board[guess_row-1][guess_column-1] == "X":
                        self.clear()
                        print "Already You have written those coordinates\n\n"
                        self.print_board()
                    elif "*" in self.board_to_check[guess_row-1][guess_column-1]:
                        self.board[guess_row-1][guess_column-1] = "*"
                        self.clear()
                        self.print_board()
                    else:
                        self.board[guess_row-1][guess_column-1] = "X"
                        self.clear()
                        print "Try again\n\n"
                        self.print_board()

    def menu_print(self):
        print "WELCOME TO BATTLESHIP"
        print "--1. SINGLE PLAYER"
        print "--2. TWO PLAYERS"
        print "--3. EXIT"

    def menu_option(self):
        while True:
            answer = raw_input("\n -- ")
            if answer == "1":
                self.clear()
                self.ask_to_the_user()
            elif answer == "2":
                pass
            elif answer == "3":
                self.clear()
                sys.exit()
            else:
                self.clear()
                print "INVALID OPITON"
                self.menu()

    def menu(self):
        self.clear()
        self.menu_print()
        self.menu_option()

MAIN = SinglePlayer()
MAIN.menu()
