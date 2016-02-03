"BATTLESHIP"

import random
import os
import sys

class GameBattle(object):
    def __init__(self):
        self.board_player_one = []
        self.board_player_one_to_check = []
        self.board_player_two = []
        self.board_player_two_to_check = []

    def reset(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system("cls")

    def clear_lists(self):
        del self.board_player_one[:]
        del self.board_player_one_to_check[:]

    def press_enter(self):
        press = raw_input("\n\nPRESS --ENTER--   ")
        self.reset()
        self.menu()

    def generate_board_player_one_to_check(self):
        for l in range(0, 10):
            self.board_player_one_to_check.append(["-"] * 10)

    def print_board_player_one_to_check(self):
        print "BATTLESHIP"
        print ""
        for o in self.board_player_one_to_check:
            print "|" + "|".join(o) + "|" 

    def generate_board_player_one(self):
        for l in range(0, 10):
            self.board_player_one.append(["-"] * 10)

    def print_board_player_one(self):
        self.reset()
        num = ["1","2","3","4","5","6","7","8","9","10"]
        print " 1 2 3 4 5 6 7 8 9 10"
        for o in self.board_player_one:
            print "|" + "|".join(o) + "|"

    def generate_board_player_two_to_check(self):
        for l in range(0, 10):
            self.board_player_two_to_check.append(["-"] * 10)

    def print_board_player_two_to_check(self):
        print "BATTLESHIP"
        print ""
        for o in self.board_player_one_to_check:
            print "|" + "|".join(o) + "|" 

    def generate_board_player_two(self):
        for l in range(0, 10):
            self.board_player_two.append(["-"] * 10)

    def print_board_player_two(slef):
        self.reset()
        print "BATTLESHIP"
        print "Remember when you guess right the position of one part of the ship"
        print "will appear one of these symbols -A- -B- -C- -D- -E- -F-"
        print "when you do not guess right, will appear this symbol -X-"
        print "when you shoot to the bomb, will appear this symbol -#-"
        print "and you will win automatically"
        for o in self.board_player_two:
            print "|" + "|".join(o) + "|"

    def valid_insert_row_and_column_by_user(self):
        while True:
            try:
                insert_row = raw_input("\nINSERT ROW: ")
                insert_column = raw_input("INSERT COLUMN: ")
                insert_row = int(insert_row)
                insert_column = int(insert_column)
                return insert_row, insert_column
            except ValueError:
                self.reset()
                print "ONLY CAN INSERT NUMBERS PLEASE"
        return insert_row, insert_column

    def valid_position_bomb(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            row_bomb = random.randint(1, 10)
            column_bomb = random.randint(1, 10)
            bomb = True
            while bomb == True:
                if self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "-":
                    self.board_player_one_to_check[row_bomb-1][column_bomb-1] = "*"
                    return row_bomb, column_bomb
                    break
                elif self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "*":
                    row_bomb = random.randint(1, 10)
                    column_bomb = random.randint(1, 10)
                    bomb = True
        elif aleatory_or_no == "no aleatory one":
            print "INSERT YOUR COORDINATES TO PUT THE BOMB"
            row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
            bomb = True
            while bomb == True:
                if self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "-":
                    self.board_player_one_to_check[row_bomb-1][column_bomb-1] = "*"
                    return row_bomb, column_bomb
                    break
                elif self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "*":
                    print "THERE IS A SHIP IN THIS COODINATE"
                    row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                    bomb = True
        elif aleatory_or_no == "no aleatory two":
            print "Insert your coordinates to put the bomb\n"
            row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
            bomb = True
            while bomb2 == True:
                if self.board_player_two_to_check[row_bomb-1][column_bomb-1] == "-":
                    self.board_player_two_to_check[row_bomb-1][column_bomb-1] = "*"
                    return row_bomb, column_bomb
                    break
                elif self.board_player_two_to_check[row_bomb-1][column_bomb-1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                    bomb = True

    def valid_position_ship_two_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            row_ship_two_horizontal = random.randint(1,10)
            column_ship_two_horizontal = random.randint(1,9)
            ship2 = True
            while ship2 == True:
                if self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                    return row_ship_two_horizontal, column_ship_two_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                    row_ship_two_horizontal = random.randint(1,10)
                    column_ship_two_horizontal = random.randint(1,9)
                    ship2 = True
        elif aleatory_or_no == "no aleatory one":
            print "Insert your coordinates to put the ship"
            print "of two parts in horizontal orientation\n"
            row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
            ship2 = True
            while ship2 == True:
                if self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                    return row_ship_two_horizontal, column_ship_two_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
                    ship2 = True
        elif aleatory_or_no == "no aleatory two":
            print "Insert your coordinates to put the ship"
            print "of two parts in horizontal orientation\n"
            row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
            ship2 = True
            while ship2 == True:
                if self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                    self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                    self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                    return row_ship_two_horizontal, column_ship_two_horizontal
                    break
                elif self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
                    ship2 = True

    def valid_position_ship_two_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            row_ship_two_vertical = random.randint(1,9)
            column_ship_two_vertical = random.randint(1,10)
            ship2 = True
            while ship2 == True:
                if self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical] == "-":
                    self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                    return row_ship_two_vertical, column_ship_two_vertical
                    break
                elif self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                    row_ship_two_vertical = random.randint(1,9)
                    column_ship_two_vertical = random.randint(1,10)
                    ship2 = True
        elif aleatory_or_no == "no aleatory one":
            print "Insert your coordinates to put the ship"
            print "of two parts in vertical orientation\n"
            row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
            ship2 = True
            while ship2 == True:
                if self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical] == "-":
                    self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                    return row_ship_two_vertical, column_ship_two_vertical
                    break
                elif self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
                    ship2 = True
        elif aleatory_or_no == "no aleatory two":
            print "Insert your coordinates to put the ship"
            print "of two parts in vertical orientation\n"
            row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
            ship2 = True
            while ship2 == True:
                if self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical] == "-":
                    self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                    self.board_player_two_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                    return row_ship_two_vertical, column_ship_two_vertical
                    break
                elif self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
                    ship2 = True

    def valid_position_ship_three_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            row_ship_three_horizontal = random.randint(1,10)
            column_ship_three_horizontal = random.randint(1,8)
            ship3 = True
            while ship3 == True:
                if self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                    return row_ship_three_horizontal, column_ship_three_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                    row_ship_three_horizontal = random.randint(1,10)
                    column_ship_three_horizontal = random.randint(1,8)
                    ship3 = True
        elif aleatory_or_no == "no aleatory one":
            print "Insert your coordinates to put the ship"
            print "of three parts in horizontal orientation\n"
            row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
            ship3 = True
            while ship3 == True:
                if self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                    return row_ship_three_horizontal, column_ship_three_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
                    ship3 = True
        elif aleatory_or_no == "no aleatory two":
            print "Insert your coordinates to put the ship"
            print "of three parts in horizontal orientation\n"
            row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
            ship3 = True
            while ship3 == True:
                if self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                and self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":
                    self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                    self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                    self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                    return row_ship_three_horizontal, column_ship_three_horizontal
                    break
                elif self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                or self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
                    ship3 = True

    def valid_position_ship_three_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            row_ship_three_vertical = random.randint(1,8)
            column_ship_three_vertical = random.randint(1,10)
            ship3 = True
            while ship3 == True:
                if self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                and self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                    return row_ship_three_vertical, column_ship_three_vertical
                    break
                elif self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                or self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                    row_ship_three_vertical = random.randint(1,8)
                    column_ship_three_vertical = random.randint(1,10)
                    ship3 = True
        elif aleatory_or_no == "no aleatory one":
            print "Insert your coordinates to put the ship"
            print "of three parts in vertical orientation\n"
            row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
            ship3 = True
            while ship3 == True:
                if self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                and self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                    return row_ship_three_vertical, column_ship_three_vertical
                    break
                elif self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                or self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
                    ship3 = True
        elif aleatory_or_no == "no aleatory two":
            print "Insert your coordinates to put the ship"
            print "of three parts in vertical orientation\n"
            row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
            ship3 = True
            while ship3 == True:
                if self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                and self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                    self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                    self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                    self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                    return row_ship_three_vertical, column_ship_three_vertical
                    break
                elif self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                or self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
                    ship3 = True

    def valid_position_ship_four_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            row_ship_four_horizontal = random.randint(1,10)
            column_ship_four_horizontal = random.randint(1,7)
            ship4 = True
            while ship4 == True:
                if self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "-"\
                and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "-":
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "*" 
                    return row_ship_four_horizontal, column_ship_four_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
                or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":
                    row_ship_four_horizontal = random.randint(1,10)
                    column_ship_four_horizontal = random.randint(1,7)
                    ship4 = True
        elif aleatory_or_no == "no aleatory one":
            print "Insert your coordinates to put the ship"
            print "of four parts in horizontal orientation\n"
            row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
            ship4 = True
            while ship4 == True:
                if self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "-"\
                and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "-" and self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "-":
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "*"
                    self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "*" 
                    return row_ship_four_horizontal, column_ship_four_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
                or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_player_one_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
                    ship4 = True
        elif aleatory_or_no == "no aleatory two":
            print "Insert your coordinates to put the ship"
            print "of four parts in horizontal orientation\n"
            row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
            ship4 = True
            while ship4 == True:
                if self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "-"\
                and self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "-" and self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "-":
                    self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "*"
                    self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] = "*"
                    self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "*"
                    self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "*" 
                    return row_ship_four_horizontal, column_ship_four_horizontal
                    break
                elif self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal] == "*"\
                or self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "*" or self.board_player_two_to_check[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
                    ship4 = True

    def valid_position_ship_four_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            row_ship_four_vertical = random.randint(1,7)
            column_ship_four_vertical = random.randint(1,10)
            ship4 = True
            while ship4 == True:
                if self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "-"\
                and self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] = "*"
                    return row_ship_four_vertical, column_ship_four_vertical
                    break
                elif self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
                or self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":
                    row_ship_four_vertical = random.randint(1,7)
                    column_ship_four_vertical = random.randint(1,10)
                    ship4 = True
        elif aleatory_or_no == "no aleatory one":
            print "Insert your coordinates to put the ship"
            print "of four parts in vertical orientation\n"
            row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
            ship4 = True
            while ship4 == True:
                if self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "-"\
                and self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "-" and self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] = "*"
                    return row_ship_four_vertical, column_ship_four_vertical
                    break
                elif self.board_player_one_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
                or self.board_player_one_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_player_one_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
                    ship4 = True
        elif aleatory_or_no == "no aleatory two":
            print "Insert your coordinates to put the ship"
            print "of four parts in vertical orientation\n"
            row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
            ship4 = True
            while ship4 == True:
                if self.board_player_two_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "-" and self.board_player_two_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "-"\
                and self.board_player_two_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "-" and self.board_player_two_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "-":
                    self.board_player_two_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] = "*"
                    self.board_player_two_to_check[row_ship_four_vertical][column_ship_four_vertical-1] = "*"
                    self.board_player_two_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] = "*"
                    self.board_player_two_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] = "*"
                    return row_ship_four_vertical, column_ship_four_vertical
                    break
                elif self.board_player_two_to_check[row_ship_four_vertical-1][column_ship_four_vertical-1] == "*" or self.board_player_two_to_check[row_ship_four_vertical][column_ship_four_vertical-1] == "*"\
                or self.board_player_two_to_check[row_ship_four_vertical+1][column_ship_four_vertical-1] == "*" or self.board_player_two_to_check[row_ship_four_vertical+2][column_ship_four_vertical-1] == "*":
                    print "There is a ship in this coordinate\n"
                    row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
                    ship4 = True

class SinglePlayer(GameBattle):
    def valid_guess_given_by_user(self):
        while True:
            try:
                guess_row = raw_input("\nGUESS THE ROW: ")
                guess_row = int(guess_row)
                guess_column = raw_input("GUESS THE COLUMN: ")
                guess_column = int(guess_column)
                return guess_row, guess_column
            except ValueError:
                self.reset()
                print "ONLY CAN INSERT NUMBERS PLEASE"
        return guess_row, guess_column

    def player_alone(self):
        self.generate_board_player_one()
        row_bomb, column_bomb = self.valid_position_bomb("aleatory")
        row_ship_two_horizontal, column_ship_two_horizontal = self.valid_position_ship_two_horizontal("aleatory")
        row_ship_two_vertical, column_ship_two_vertical = self.valid_position_ship_two_vertical("aleatory")
        row_ship_three_horizontal, column_ship_three_horizontal = self. valid_position_ship_three_horizontal("aleatory")
        row_ship_three_vertical, column_ship_three_vertical = self.valid_position_ship_three_vertical("aleatory")
        row_ship_four_horizontal, column_ship_four_horizontal = self.valid_position_ship_four_horizontal("aleatory")
        row_ship_four_vertical, column_ship_four_vertical = self.valid_position_ship_four_vertical("aleatory")
        print "bomb"
        print row_bomb, column_bomb
        while True:
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
                self.print_board_player_one()
                print "YOU HAVE SHOT TO THE BOMB, AND YOU HAVE SUNK ALL THE SHIPS"
                print "YOU WIN"
                self.clear_lists()
                self.press_enter()
            else:
                if (guess_row < 1 or guess_row > 10) or (guess_column < 1 or guess_column > 10):
                    self.print_board_player_one()
                    print "It is not in the ocean\n\n"
                    
                elif self.board_player_one[guess_row-1][guess_column-1] == "X" or self.board_player_one[guess_row-1][guess_column-1] == "*":
                    self.print_board_player_one()
                    print "Already You have written those coordinates\n\n"
                    
                elif guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal\
                or guess_row == row_ship_two_horizontal and guess_column == column_ship_two_horizontal+1:
                    self.board_player_one[guess_row-1][guess_column-1] = "A"
                    self.print_board_player_one()
                elif guess_row == row_ship_two_vertical and guess_column == column_ship_two_vertical\
                or guess_row == row_ship_two_vertical+1 and guess_column == column_ship_two_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "B"
                    self.print_board_player_one()
                elif guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+1\
                or guess_row == row_ship_three_horizontal and guess_column == column_ship_three_horizontal+2:
                    self.board_player_one[guess_row-1][guess_column-1] = "C"
                    self.print_board_player_one()
                elif guess_row == row_ship_three_vertical and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+1 and guess_column == column_ship_three_vertical\
                or guess_row == row_ship_three_vertical+2 and guess_column == column_ship_three_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "D"
                    self.print_board_player_one()
                elif guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+1\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+2\
                or guess_row == row_ship_four_horizontal and guess_column == column_ship_four_horizontal+3:
                    self.board_player_one[guess_row-1][guess_column-1] = "E"
                    self.print_board_player_one()
                elif guess_row == row_ship_four_vertical and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+1 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+2 and guess_column == column_ship_four_vertical\
                or guess_row == row_ship_four_vertical+3 and guess_column == column_ship_four_vertical:
                    self.board_player_one[guess_row-1][guess_column-1] = "F"
                    self.print_board_player_one()
                else:
                    self.board_player_one[guess_row-1][guess_column-1] = "X"
                    self.print_board_player_one()
                    print "Try again\n\n"
                    
            if self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "A" and self.board_player_one[row_ship_two_horizontal-1][column_ship_two_horizontal] == "A"\
            and self.board_player_one[row_ship_two_vertical-1][column_ship_two_vertical-1] == "B" and self.board_player_one[row_ship_two_vertical][column_ship_two_vertical-1] == "B"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "C" and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal] == "C"\
            and self.board_player_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "C" and self.board_player_one[row_ship_three_vertical-1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_three_vertical][column_ship_three_vertical-1] == "D" and self.board_player_one[row_ship_three_vertical+1][column_ship_three_vertical-1] == "D"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal] == "E"\
            and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] == "E" and self.board_player_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] == "E"\
            and self.board_player_one[row_ship_four_vertical-1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical][column_ship_four_vertical-1] == "F"\
            and self.board_player_one[row_ship_four_vertical+1][column_ship_four_vertical-1] == "F" and self.board_player_one[row_ship_four_vertical+2][column_ship_four_vertical-1] == "F":
                self.print_board_player_one()
                print "\nYou win"
                self.clear_lists()
                self.press_enter()

class Menu(SinglePlayer):
    def menu_print(self):
        print "Welcome to Battleship"
        print "\n --1. SINGLE PLAYER"
        print "\n --2. TWO PLAYERS"
        print "\n --3. EXIT"

    def menu_option(self):
        while True:
            choose_user = raw_input(" - ")
            if choose_user == "1":
                self.reset()
                self.player_alone()
            elif choose_user == "2":
                pass
            elif choose_user == "3":
                self.reset()
                sys.exit()
            else:
                self.reset()
                print "INVALID OPTION\n"
                self.menu()

    def menu(self):
        self.reset()
        self.menu_print()
        self.menu_option()

MAIN = Menu()
MAIN.menu()