"BATTLESHIP"

import random
import os
import sys
import time

class GameBattle(object):
    def __init__(self):
        self.board_player_one = []
        self.board_player_one_to_check = []

        self.board_player_two = []
        self.board_player_two_to_check = []

        self.show_board_one = []
        self.show_board_two = []

    def clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system("cls")

    def clean_lists(self):
        del self.board_player_one[:]
        del self.board_player_one_to_check[:]
        del self.board_player_two[:]
        del self.board_player_two_to_check[:]
        del self.show_board_one[:]
        del self.show_board_two[:]

    def generate_board_player_one_to_check(self):
        for l in range(0, 10):
            self.board_player_one_to_check.append(["-"] * 10)

    def print_board_player_one_to_check(self):

        for o in self.board_player_one_to_check:
            print "|" + "|".join(o) + "|"

    def generate_board_player_one(self):
        for l in range(0, 10):
            self.board_player_one.append(["-"] * 10)

    def print_board_player_one(self):
        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.board_player_one:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

    def generate_board_player_two_to_check(self):
        for l in range(0, 10):
            self.board_player_two_to_check.append(["-"] * 10)

    def print_board_player_two_to_check(self):
        for o in self.board_player_one_to_check:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

    def generate_board_player_two(self):
        for l in range(0, 10):
            self.board_player_two.append(["-"] * 10)

    def print_board_player_two(self):

        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.board_player_two:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

    def generate_show_board_one(self):
        for l in range(0, 10):
            self.show_board_one.append(["-"]*10)

    def print_show_board_one(self):
        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.show_board_one:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

    def generate_show_board_two(self):
        for l in range(0, 10):
            self.show_board_two.append(["-"]*10)

    def print_show_board_two(self):
        print " 1 2 3 4 5 6 7 8 9 10"
        number = 1
        for o in self.show_board_two:
            print "|" + "|".join(o) + "|" + str(number)
            number+=1

    def show_players(self, player):
        if player == "1":
            print """
 ______ _____   _______ ___ ___ _______ ______      ____   
|   __ \     |_|   _   |   |   |    ___|   __ \    |_   |  
|    __/       |       |\     /|    ___|      <     _|  |_ 
|___|  |_______|___|___| |___| |_______|___|__|    |______|  \n"""

        elif player == "2":
            print """
 ______ _____   _______ ___ ___ _______ ______      ______ 
|   __ \     |_|   _   |   |   |    ___|   __ \    |__    |
|    __/       |       |\     /|    ___|      <    |    __|
|___|  |_______|___|___| |___| |_______|___|__|    |______|   
                                            \n"""
        elif player == "1w":
            print """
 ______ _____   _______ ___ ___ _______ ______      ____        ________ _______ _______ 
|   __ \     |_|   _   |   |   |    ___|   __ \    |_   |      |  |  |  |_     _|    |  |
|    __/       |       |\     /|    ___|      <     _|  |_     |  |  |  |_|   |_|       |
|___|  |_______|___|___| |___| |_______|___|__|    |______|    |________|_______|__|____|
                                                                                            
"""
        elif player == "2w":
            print """
 ______ _____   _______ ___ ___ _______ ______      ______      ________ _______ _______ 
|   __ \     |_|   _   |   |   |    ___|   __ \    |__    |    |  |  |  |_     _|    |  |
|    __/       |       |\     /|    ___|      <    |    __|    |  |  |  |_|   |_|       |
|___|  |_______|___|___| |___| |_______|___|__|    |______|    |________|_______|__|____|  
                                                                       """
        elif player == "b1":
            print "\n   BOARD PLAYER  1"
        elif player == "b2":
            print "\n   BOARD PLAYER  2"

    def show_board_one_or_two(self, board):
        if board == "1":
            self.clear()
            self.show_players("b1")
            self.print_show_board_one()
        elif board == "2":
            self.clear()
            self.show_players("b2")
            self.print_show_board_two()

    def valid_insert_row_and_column_by_user(self):
        while True:
            try:
                insert_row = raw_input("\nINSERT ROW: ")
                insert_row = int(insert_row)
                insert_column = raw_input("INSERT COLUMN: ")
                insert_column = int(insert_column)
                return insert_row, insert_column
            except ValueError:
                self.clear()
                print "ONLY CAN INSERT NUMBERS"
        return insert_row, insert_column

    def position_bomb(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            bomb = True
            while bomb == True:
                row_bomb = random.randint(1, 10)
                column_bomb = random.randint(1, 10)
                if self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "-":
                    self.board_player_one_to_check[row_bomb-1][column_bomb-1] = "*"
                    return row_bomb, column_bomb
                    break
                elif self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "*":
                    bomb = True
        elif aleatory_or_no == "no aleatory one":
            print "\nINSERT THE COORDINATES WHERE THE BOMB WILL GO"
            bomb = True
            while bomb == True:
                row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                if row_bomb > 10 or row_bomb < 1 or column_bomb > 10 or row_bomb <1:
                    self.show_board_one_or_two("1")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    bomb = True
                else:
                    if self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "-":
                        self.board_player_one_to_check[row_bomb-1][column_bomb-1] = "*"
                        return row_bomb, column_bomb
                        break
                    elif self.board_player_one_to_check[row_bomb-1][column_bomb-1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        bomb = True
        elif aleatory_or_no == "no aleatory two":
            print "\nINSERT THE COORDINATES WHERE THE BOMB WILL GO"
            bomb = True
            while bomb == True:
                row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                if row_bomb > 10 or row_bomb < 1 or column_bomb > 10 or row_bomb <1:
                    self.show_board_one_or_two("2")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    bomb = True
                else:
                    if self.board_player_two_to_check[row_bomb-1][column_bomb-1] == "-":
                        self.board_player_two_to_check[row_bomb-1][column_bomb-1] = "*"
                        return row_bomb, column_bomb
                        break
                    elif self.board_player_two_to_check[row_bomb-1][column_bomb-1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        row_bomb, column_bomb = self.valid_insert_row_and_column_by_user()
                        bomb = True

    def ship_two_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            ship2 = True
            while ship2 == True:
                row_ship_two_horizontal = random.randint(1,10)
                column_ship_two_horizontal = random.randint(1,9)
                if self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                    return row_ship_two_horizontal, column_ship_two_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                    ship2 = True
        elif aleatory_or_no == "no aleatory one":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF TWO PARTS IN HORIZONTAL ORIENTATION\n"
            ship2 = True
            while ship2 == True:
                row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_two_horizontal < 1 or row_ship_two_horizontal > 10 or column_ship_two_horizontal < 1 or column_ship_two_horizontal > 9:
                    self.show_board_one_or_two("1")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship2 = True
                else:
                    if self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                        self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                        self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                        return row_ship_two_horizontal, column_ship_two_horizontal
                        break
                    elif self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                        self.show_board_one_or_two("1")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship2 = True
        elif aleatory_or_no == "no aleatory two":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF TWO PARTS IN HORIZONTAL ORIENTATION\n"
            ship2 = True
            while ship2 == True:
                row_ship_two_horizontal, column_ship_two_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_two_horizontal < 1 or row_ship_two_horizontal > 10 or column_ship_two_horizontal < 1 or column_ship_two_horizontal > 9:
                    self.show_board_one_or_two("2")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship2 = True
                else:
                    if self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "-":
                        self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "*"
                        self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] = "*"
                        return row_ship_two_horizontal, column_ship_two_horizontal
                        break
                    elif self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_two_horizontal-1][column_ship_two_horizontal] == "*":
                        self.show_board_one_or_two("2")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship2 = True

    def ship_two_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            ship2 = True
            while ship2 == True:
                row_ship_two_vertical = random.randint(1,9)
                column_ship_two_vertical = random.randint(1,10)
                if self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                    return row_ship_two_vertical, column_ship_two_vertical
                    break
                elif self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                    ship2 = True
        elif aleatory_or_no == "no aleatory one":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF TWO PARTS IN VERTICAL ORIENTATION\n"
            ship2 = True
            while ship2 == True:
                row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_two_vertical < 1 or row_ship_two_vertical > 9 or column_ship_two_vertical < 1 or column_ship_two_vertical > 10:
                    self.show_board_one_or_two("1")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship2 = True
                else:
                    if self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "-":
                        self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                        return row_ship_two_vertical, column_ship_two_vertical
                        break
                    elif self.board_player_one_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship2 = True
        elif aleatory_or_no == "no aleatory two":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF TWO PARTS IN VERTICAL ORIENTATION\n"
            ship2 = True
            while ship2 == True:
                row_ship_two_vertical, column_ship_two_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_two_vertical < 1 or row_ship_two_vertical > 9 or column_ship_two_vertical < 1 or column_ship_two_vertical > 10:
                    self.show_board_one_or_two("2")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship2 = True
                else:
                    if self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "-" and self.board_player_two_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "-":
                        self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_two_vertical][column_ship_two_vertical-1] = "*"
                        return row_ship_two_vertical, column_ship_two_vertical
                        break
                    elif self.board_player_two_to_check[row_ship_two_vertical-1][column_ship_two_vertical-1] == "*" or self.board_player_one_to_check[row_ship_two_vertical][column_ship_two_vertical-1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship2 = True

    def ship_three_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            ship3 = True
            while ship3 == True:
                row_ship_three_horizontal = random.randint(1,10)
                column_ship_three_horizontal = random.randint(1,8)
                if self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                    self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                    return row_ship_three_horizontal, column_ship_three_horizontal
                    break
                elif self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                    ship3 = True
        elif aleatory_or_no == "no aleatory one":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF THREE PARTS IN HORIZONTAL ORIENTATION\n"
            ship3 = True
            while ship3 == True:
                row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_three_horizontal < 1 or row_ship_three_horizontal > 10 or column_ship_three_horizontal < 1 or column_ship_three_horizontal > 8:
                    self.show_board_one_or_two("1")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship3 = True
                else:
                    if self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                    and self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":
                        self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                        self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                        self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                        return row_ship_three_horizontal, column_ship_three_horizontal
                        break
                    elif self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                    or self.board_player_one_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship3 = True
        elif aleatory_or_no == "no aleatory two":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF THREE PARTS IN HORIZONTAL ORIENTATION\n"
            ship3 = True
            while ship3 == True:
                row_ship_three_horizontal, column_ship_three_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_three_horizontal < 1 or row_ship_three_horizontal > 10 or column_ship_three_horizontal < 1 or column_ship_three_horizontal > 8:
                    self.show_board_one_or_two("2")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship3 = True
                else:
                    if self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "-" and self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "-"\
                    and self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "-":
                        self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "*"
                        self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] = "*"
                        self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "*"
                        return row_ship_three_horizontal, column_ship_three_horizontal
                        break
                    elif self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal-1] == "*" or self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal] == "*"\
                    or self.board_player_two_to_check[row_ship_three_horizontal-1][column_ship_three_horizontal+1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship3 = True

    def ship_three_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            ship3 = True
            while ship3 == True:
                row_ship_three_vertical = random.randint(1,8)
                column_ship_three_vertical = random.randint(1,10)
                if self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                and self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                    self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                    self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                    return row_ship_three_vertical, column_ship_three_vertical
                    break
                elif self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                or self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                    ship3 = True
        elif aleatory_or_no == "no aleatory one":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF THREE PARTS IN VERTICAL ORIENTATION\n"
            ship3 = True
            while ship3 == True:
                row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_three_vertical < 1 or row_ship_three_vertical > 8 or column_ship_three_vertical < 1 or column_ship_three_vertical > 10:
                    self.show_board_one_or_two("1")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship3 = True
                else:
                    if self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                    and self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                        self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                        self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                        return row_ship_three_vertical, column_ship_three_vertical
                        break
                    elif self.board_player_one_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_one_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                    or self.board_player_one_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                        self.show_board_one_or_two("1")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship3 = True
        elif aleatory_or_no == "no aleatory two":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF THREE PARTS IN VERTICAL ORIENTATION\n"
            ship3 = True
            while ship3 == True:
                row_ship_three_vertical, column_ship_three_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_three_vertical < 1 or row_ship_three_vertical > 8 or column_ship_three_vertical < 1 or column_ship_three_vertical > 10:
                    self.show_board_one_or_two("2")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship3 = True
                else:
                    if self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "-" and self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "-"\
                    and self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "-":
                        self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] = "*"
                        self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] = "*"
                        return row_ship_three_vertical, column_ship_three_vertical
                        break
                    elif self.board_player_two_to_check[row_ship_three_vertical-1][column_ship_three_vertical-1] == "*" or self.board_player_two_to_check[row_ship_three_vertical][column_ship_three_vertical-1] == "*"\
                    or self.board_player_two_to_check[row_ship_three_vertical+1][column_ship_three_vertical-1] == "*":
                        self.show_board_one_or_two("2")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship3 = True

    def ship_four_horizontal(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            ship4 = True
            while ship4 == True:
                row_ship_four_horizontal = random.randint(1,10)
                column_ship_four_horizontal = random.randint(1,7)
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
                    ship4 = True
        elif aleatory_or_no == "no aleatory one":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF FOUR PARTS IN HORIZONTAL ORIENTATION\n"
            ship4 = True
            while ship4 == True:
                row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_four_horizontal < 1 or row_ship_four_horizontal > 10 or  column_ship_four_horizontal < 1 or column_ship_four_horizontal > 7:
                    self.show_board_one_or_two("1")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship4 = True
                else:
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
                        self.show_board_one_or_two("1")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship4 = True
        elif aleatory_or_no == "no aleatory two":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF FOUR PARTS IN HORIZONTRAL ORIENTATION\n"
            ship4 = True
            while ship4 == True:
                row_ship_four_horizontal, column_ship_four_horizontal = self.valid_insert_row_and_column_by_user()
                if row_ship_four_horizontal < 1 or row_ship_four_horizontal > 10 or  column_ship_four_horizontal < 1 or column_ship_four_horizontal > 7:
                    self.show_board_one_or_two("2")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship4 = True
                else:
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
                        self.show_board_one_or_two("2")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship4 = True

    def ship_four_vertical(self, aleatory_or_no):
        self.generate_board_player_one_to_check()
        self.generate_board_player_two_to_check()
        if aleatory_or_no == "aleatory":
            ship4 = True
            while ship4 == True:
                row_ship_four_vertical = random.randint(1,7)
                column_ship_four_vertical = random.randint(1,10)
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
                    ship4 = True
        elif aleatory_or_no == "no aleatory one":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF FOUR PARTS IN VERTICAL ORIENTATION\n"
            ship4 = True
            while ship4 == True:
                row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_four_vertical < 1 or row_ship_four_vertical > 7 or column_ship_four_vertical < 1 or column_ship_four_vertical > 10:
                    self.show_board_one_or_two("1")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship4 = True
                else:
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
                        self.show_board_one_or_two("1")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship4 = True
        elif aleatory_or_no == "no aleatory two":
            print "\nINSERT YOUR COORDINATES TO PUT THE SHIP OF FOUR PARTS IN VERTICAL ORIENTATION\n"
            ship4 = True
            while ship4 == True:
                row_ship_four_vertical, column_ship_four_vertical = self.valid_insert_row_and_column_by_user()
                if row_ship_four_vertical < 1 or row_ship_four_vertical > 7 or column_ship_four_vertical < 1 or column_ship_four_vertical > 10:
                    self.show_board_one_or_two("2")
                    print "\nTHIS SHIP LEAVES OF THE OCEAN, INSERT OTHER COORDINATES PLEASE"
                    ship4 = True
                else:
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
                        self.show_board_one_or_two("2")
                        print "\nTHERE IS A SHIP IN THIS COORDINATE\n"
                        ship4 = True

class SinglePlayer(GameBattle):
    def alone_the_user(self):
        while True:
            try:
                row = raw_input("\nGUESS THE ROW: ")
                row = int(row)
                column = raw_input("GUESS THE COLUMN: ")
                column = int(column)
                return row, column
            except ValueError:
                self.clear()
                print "ONLY CAN INSERT NUMBERS"
        return row, column

    def player_alone(self):
        self.generate_board_player_one_to_check()
        self.generate_board_player_one()
        row_bomb, column_bomb = self.position_bomb("aleatory")
        row_ship_two_horizontal, column_ship_two_horizontal = self.ship_two_horizontal("aleatory")
        row_ship_two_vertical, column_ship_two_vertical = self.ship_two_vertical("aleatory")
        row_ship_three_horizontal, column_ship_three_horizontal = self. ship_three_horizontal("aleatory")
        row_ship_three_vertical, column_ship_three_vertical = self.ship_three_vertical("aleatory")
        row_ship_four_horizontal, column_ship_four_horizontal = self.ship_four_horizontal("aleatory")
        row_ship_four_vertical, column_ship_four_vertical = self.ship_four_vertical("aleatory")
        print "bomb"
        print row_bomb, column_bomb
        """print "\nship of two h"
        print row_ship_two_horizontal, column_ship_two_horizontal
        print "\nship of two v"
        print row_ship_two_vertical, column_ship_two_vertical
        print "\nship of three h"
        print row_ship_three_horizontal, column_ship_three_horizontal
        print "\nship of three v"
        print row_ship_three_vertical, column_ship_three_vertical
        print "\nship of four h"
        print row_ship_four_horizontal, column_ship_four_horizontal
        print "\nship of four v"
        print row_ship_four_vertical, column_ship_four_vertical"""
        self.clear()
        life = 0
        while life <= 13:
            self.show_players("1")
            self.print_board_player_one()
            row, column = self.alone_the_user()
            if row == row_bomb and column == column_bomb:
                self.board_player_one[row-1][column-1] = "#"
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
                print "CONGRATULATIONS YOU SHOT TO THE BOMB, THE SHIPS HAVE SUNK\n"
                self.show_players("1w")
                self.print_board_player_one()
                raw_input("\nPress ENTER")
                self.clean_lists()
                self.clear()
                self.play_again()
            else:
                if (row < 1 or row > 13) or (column < 1 or column > 13):
                    self.clear()
                    print "IT IS NOT IN THE OCEAN\n\n"
                    life +=1
                    print "You still have %d lives, Come on, you can sink the ships" % (13-life)

                elif self.board_player_one[row-1][column-1] == "X" or self.board_player_one[row-1][column-1] == "A"\
                or self.board_player_one[row-1][column-1] == "B" or self.board_player_one[row-1][column-1] == "C"\
                or self.board_player_one[row-1][column-1] == "D" or self.board_player_one[row-1][column-1] == "E"\
                or self.board_player_one[row-1][column-1] == "F":
                    self.clear()
                    print "ALREADY YOU HAVE WRITTEN THOSE COORDINATES\n"
                    life +=1
                    print "You still have %d lives, Come on, you can sink the ships" % (13-life)
                elif row == row_ship_two_horizontal and column == column_ship_two_horizontal\
                or row == row_ship_two_horizontal and column == column_ship_two_horizontal+1:
                    self.board_player_one[row-1][column-1] = "A"
                    self.clear()
                elif row == row_ship_two_vertical and column == column_ship_two_vertical\
                or row == row_ship_two_vertical+1 and column == column_ship_two_vertical:
                    self.board_player_one[row-1][column-1] = "B"
                    self.clear()
                elif row == row_ship_three_horizontal and column == column_ship_three_horizontal\
                or row == row_ship_three_horizontal and column == column_ship_three_horizontal+1\
                or row == row_ship_three_horizontal and column == column_ship_three_horizontal+2:
                    self.board_player_one[row-1][column-1] = "C"
                    self.clear()
                elif row == row_ship_three_vertical and column == column_ship_three_vertical\
                or row == row_ship_three_vertical+1 and column == column_ship_three_vertical\
                or row == row_ship_three_vertical+2 and column == column_ship_three_vertical:
                    self.board_player_one[row-1][column-1] = "D"
                    self.clear()
                elif row == row_ship_four_horizontal and column == column_ship_four_horizontal\
                or row == row_ship_four_horizontal and column == column_ship_four_horizontal+1\
                or row == row_ship_four_horizontal and column == column_ship_four_horizontal+2\
                or row == row_ship_four_horizontal and column == column_ship_four_horizontal+3:
                    self.board_player_one[row-1][column-1] = "E"
                    self.clear()
                elif row == row_ship_four_vertical and column == column_ship_four_vertical\
                or row == row_ship_four_vertical+1 and column == column_ship_four_vertical\
                or row == row_ship_four_vertical+2 and column == column_ship_four_vertical\
                or row == row_ship_four_vertical+3 and column == column_ship_four_vertical:
                    self.board_player_one[row-1][column-1] = "F"
                    self.clear()
                else:
                    self.board_player_one[row-1][column-1] = "X"
                    self.clear()
                    print "TRY AGAIN\n"
                    life+=1
                    print "YOU STILL HAVE %d LIVES, COME ON, YOU CAN SINK THE SHIPS\n" % (13-life)
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
                time.sleep(1)
                print "YOU HAVE SUNK ALL SHIPS\n"
                self.show_players("1w")
                self.print_board_player_one()
                raw_input("\nPress ENTER")
                self.clean_lists()
                self.clear()
                self.play_again()
            if life == 13:
                self.clear()
                print """
 ___ ___ _______ _______      _____   _______ _______ _______ 
|   |   |       |   |   |    |     |_|       |     __|    ___|
 \     /|   -   |   |   |    |       |   -   |__     |    ___|
  |___| |_______|_______|    |_______|_______|_______|_______|
                                      """
                raw_input("\nPress ENTER ")
                self.clear()
                self.play_again()

    def play_again(self):
        while True:
            option_user = raw_input("DO YOU WANT TO PLAY AGAIN y/n:  ")
            option_user = option_user.lower()
            if option_user == "y":
                self.clean_lists()
                self.clear()
                self.player_alone()
            elif option_user == "n":
                self.clean_lists()
                self.clear()
                self.menu()
            else:
                self.clear()
                print "ONLY CAN WRITE y/n \n"

class MultiPlayer(SinglePlayer):
    def place_ships_players(self):
        self.generate_board_player_one()
        self.generate_show_board_one()
        self.show_players("b1")
        self.print_show_board_one()
        row_bomb, column_bomb = self.position_bomb("no aleatory one")
        self.clear()
        self.show_board_one[row_bomb-1][column_bomb-1] = "#"
        self.show_players("b1")
        self.print_show_board_one()
        row_ship_two_horizontal, column_ship_two_horizontal = self.ship_two_horizontal("no aleatory one")
        self.clear()
        self.show_board_one[row_ship_two_horizontal-1][column_ship_two_horizontal-1] = "A"
        self.show_board_one[row_ship_two_horizontal-1][column_ship_two_horizontal] = "A"
        self.show_players("b1")
        self.print_show_board_one()
        row_ship_two_vertical, column_ship_two_vertical = self.ship_two_vertical("no aleatory one")
        self.clear()
        self.show_board_one[row_ship_two_vertical-1][column_ship_two_vertical-1] = "B"
        self.show_board_one[row_ship_two_vertical][column_ship_two_vertical-1] = "B"
        self.show_players("b1")
        self.print_show_board_one()
        row_ship_three_horizontal, column_ship_three_horizontal = self. ship_three_horizontal("no aleatory one")
        self.clear()
        self.show_board_one[row_ship_three_horizontal-1][column_ship_three_horizontal-1] = "C"
        self.show_board_one[row_ship_three_horizontal-1][column_ship_three_horizontal] = "C"
        self.show_board_one[row_ship_three_horizontal-1][column_ship_three_horizontal+1] = "C"
        self.show_players("b1")
        self.print_show_board_one()
        row_ship_three_vertical, column_ship_three_vertical = self.ship_three_vertical("no aleatory one")
        self.clear()
        self.show_board_one[row_ship_three_vertical-1][column_ship_three_vertical-1] = "D"
        self.show_board_one[row_ship_three_vertical][column_ship_three_vertical-1] = "D"
        self.show_board_one[row_ship_three_vertical+1][column_ship_three_vertical-1] = "D"
        self.show_players("b1")
        self.print_show_board_one()
        row_ship_four_horizontal, column_ship_four_horizontal = self.ship_four_horizontal("no aleatory one")
        self.clear()
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal-1] = "E"
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal] = "E"
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal+1] = "E"
        self.show_board_one[row_ship_four_horizontal-1][column_ship_four_horizontal+2] = "E"
        self.show_players("b1")
        self.print_show_board_one()
        row_ship_four_vertical, column_ship_four_vertical = self.ship_four_vertical("no aleatory one")
        self.clear()
        self.show_board_one[row_ship_four_vertical-1][column_ship_four_vertical-1] = "F"
        self.show_board_one[row_ship_four_vertical][column_ship_four_vertical-1] = "F"
        self.show_board_one[row_ship_four_vertical+1][column_ship_four_vertical-1] = "F"
        self.show_board_one[row_ship_four_vertical+2][column_ship_four_vertical-1] = "F"
        self.show_players("b1")
        self.print_show_board_one()
        self.clear()
        print "NOW THE PLAYER TWO MUST PUT HIS SHIPS\n"
        raw_input("Press ENTER")
        self.clear()
        self.generate_board_player_two()
        self.generate_show_board_two()
        self.show_players("b2")
        self.print_show_board_two()
        row_bomb2, column_bomb2 = self.position_bomb("no aleatory two")
        self.clear()
        self.show_board_two[row_bomb2-1][column_bomb2-1] = "#"
        self.show_players("b2")
        self.print_show_board_two()
        row_ship_two_horizontal2, column_ship_two_horizontal2 = self.ship_two_horizontal("no aleatory two")
        self.clear()
        self.show_board_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2-1] = "A"
        self.show_board_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2] = "A"
        self.show_players("b2")
        self.print_show_board_two()
        
        row_ship_two_vertical2, column_ship_two_vertical2 = self.ship_two_vertical("no aleatory two")
        self.clear()
        self.show_board_two[row_ship_two_vertical2-1][column_ship_two_vertical2-1] = "B"
        self.show_board_two[row_ship_two_vertical2][column_ship_two_vertical2-1] = "B"
        self.show_players("b2")
        self.print_show_board_two()
        row_ship_three_horizontal2, column_ship_three_horizontal2 = self. ship_three_horizontal("no aleatory two")
        self.clear()
        self.show_board_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2-1] = "C"
        self.show_board_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2] = "C"
        self.show_board_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2+1] = "C"
        self.show_players("b2")
        self.print_show_board_two()
        row_ship_three_vertical2, column_ship_three_vertical2 = self.ship_three_vertical("no aleatory two")
        self.clear()
        self.show_board_two[row_ship_three_vertical2-1][column_ship_three_vertical2-1] = "D"
        self.show_board_two[row_ship_three_vertical2][column_ship_three_vertical2-1] = "D"
        self.show_board_two[row_ship_three_vertical2+1][column_ship_three_vertical2-1] = "D"
        self.show_players("b2")
        self.print_show_board_two()
        row_ship_four_horizontal2, column_ship_four_horizontal2 = self.ship_four_horizontal("no aleatory two")
        self.clear()
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2-1] = "E"
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2] = "E"
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+1] = "E"
        self.show_board_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+2] = "E"
        self.show_players("b2")
        self.print_show_board_two()
        row_ship_four_vertical2, column_ship_four_vertical2 = self.ship_four_vertical("no aleatory two")
        self.clear()
        self.show_board_two[row_ship_four_vertical2-1][column_ship_four_vertical2-1] = "F"
        self.show_board_two[row_ship_four_vertical2][column_ship_four_vertical2-1] = "F"
        self.show_board_two[row_ship_four_vertical2+1][column_ship_four_vertical2-1] = "F"
        self.show_board_two[row_ship_four_vertical2+2][column_ship_four_vertical2-1] = "F"
        self.show_players("b2")
        self.print_show_board_two()
        self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

    def player_one(self, row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2):
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
            self.show_players("2w")
            self.print_board_player_one()
            raw_input("\nPress ENTER ")
            self.clean_lists()
            self.clear()
            self.multi_play_again()
        else:
            self.clear()
            pass
        print "YOUR TURN PLAYER 1"
        ask = raw_input("\nDO YOU WANT TO SEE YOUR BOARD y/n  ")
        ask = ask.lower()
        self.clear()
        if ask == "y":
            print "\nHERE YOU WILL SEE THE SHOTS OF PLAYER 2\n"
            self.print_board_player_one()
            raw_input("\nPress ENTER ")
            self.clear()
        else:
            self.clear()
            pass
        while True:
            self.show_players("1")
            self.print_board_player_two()
            row, column = self.alone_the_user()
            if row == row_bomb2 and column == column_bomb2:
                self.board_player_two[row-1][column-1] = "#"
                self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2-1] = "A"
                self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2] = "A"
                self.board_player_two[row_ship_two_vertical2-1][column_ship_two_vertical2-1] = "B"
                self.board_player_two[row_ship_two_vertical2][column_ship_two_vertical2-1] = "B"
                self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2-1] = "C"
                self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2] = "C"
                self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2+1] = "C"
                self.board_player_two[row_ship_three_vertical2-1][column_ship_three_vertical2-1] = "D"
                self.board_player_two[row_ship_three_vertical2][column_ship_three_vertical2-1] = "D"
                self.board_player_two[row_ship_three_vertical2+1][column_ship_three_vertical2-1] = "D"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2-1] = "E"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2] = "E"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+1] = "E"
                self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+2] = "E"
                self.board_player_two[row_ship_four_vertical2-1][column_ship_four_vertical2-1] = "F"
                self.board_player_two[row_ship_four_vertical2][column_ship_four_vertical2-1] = "F"
                self.board_player_two[row_ship_four_vertical2+1][column_ship_four_vertical2-1] = "F"
                self.board_player_two[row_ship_four_vertical2+2][column_ship_four_vertical2-1] = "F"
                self.clear()
                print "CONGRATULATIONS YOU SHOT TO THE BOMB, THE SHIPS HAVE SUNK\n"
                self.show_players("1w")
                self.print_board_player_two()
                raw_input("\nPress ENTER")
                self.clean_lists()
                self.clear()
                self.multi_play_again()
            else:
                if (row < 1 or row > 10) or (column < 1 or column > 10):
                    self.clear()
                    print "IT IS NOT IN THE OCEAN\n"

                elif self.board_player_two[row-1][column-1] == "X" or self.board_player_two[row-1][column-1] == "A"\
                or self.board_player_two[row-1][column-1] == "B" or self.board_player_two[row-1][column-1] == "C"\
                or self.board_player_two[row-1][column-1] == "D" or self.board_player_two[row-1][column-1] == "E"\
                or self.board_player_two[row-1][column-1] == "F":
                    self.clear()
                    print "ALREADY YOU HAVE WRITTEN THOSE COORDINATES\n"
                elif row == row_ship_two_horizontal2 and column == column_ship_two_horizontal2\
                or row == row_ship_two_horizontal2 and column == column_ship_two_horizontal2+1:
                    self.board_player_two[row-1][column-1] = "A"
                    self.clear()
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b2")
                    self.print_board_player_two()
                    raw_input("\nPress ENTER ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)
                elif row == row_ship_two_vertical2 and column == column_ship_two_vertical2\
                or row == row_ship_two_vertical2+1 and column == column_ship_two_vertical2:
                    self.board_player_two[row-1][column-1] = "B"
                    self.clear()
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b2")
                    self.print_board_player_two()
                    raw_input("\nPress ENTER ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)
                elif row == row_ship_three_horizontal2 and column == column_ship_three_horizontal2\
                or row == row_ship_three_horizontal2 and column == column_ship_three_horizontal2+1\
                or row == row_ship_three_horizontal2 and column == column_ship_three_horizontal2+2:
                    self.board_player_two[row-1][column-1] = "C"
                    self.clear()
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b2")
                    self.print_board_player_two()
                    raw_input("Press ENTER ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_three_vertical2 and column == column_ship_three_vertical2\
                or row == row_ship_three_vertical2+1 and column == column_ship_three_vertical2\
                or row == row_ship_three_vertical2+2 and column == column_ship_three_vertical2:
                    self.board_player_two[row-1][column-1] = "D"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b2")
                    self.print_board_player_two()
                    raw_input("Press ENTER ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_four_horizontal2 and column == column_ship_four_horizontal2\
                or row == row_ship_four_horizontal2 and column == column_ship_four_horizontal2+1\
                or row == row_ship_four_horizontal2 and column == column_ship_four_horizontal2+2\
                or row == row_ship_four_horizontal2 and column == column_ship_four_horizontal2+3:
                    self.board_player_two[row-1][column-1] = "E"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b2")
                    self.print_board_player_two()
                    raw_input("Press ENTER ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_four_vertical2 and column == column_ship_four_vertical2\
                or row == row_ship_four_vertical2+1 and column == column_ship_four_vertical2\
                or row == row_ship_four_vertical2+2 and column == column_ship_four_vertical2\
                or row == row_ship_four_vertical2+3 and column == column_ship_four_vertical2:
                    self.board_player_two[row-1][column-1] = "F"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b2")
                    self.print_board_player_two()
                    raw_input("Press ENTER ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                else:
                    self.board_player_two[row-1][column-1] = "X"
                    self.clear()
                    time.sleep(1)
                    print "You have failed"
                    self.show_players("b2")
                    self.print_board_player_two()
                    raw_input("Press ENTER ")
                    self.player_number_two(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

    def player_number_two(self, row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2):


        if self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2-1] == "A" and self.board_player_two[row_ship_two_horizontal2-1][column_ship_two_horizontal2] == "A"\
            and self.board_player_two[row_ship_two_vertical2-1][column_ship_two_vertical2-1] == "B" and self.board_player_two[row_ship_two_vertical2][column_ship_two_vertical2-1] == "B"\
            and self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2-1] == "C" and self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2] == "C"\
            and self.board_player_two[row_ship_three_horizontal2-1][column_ship_three_horizontal2+1] == "C" and self.board_player_two[row_ship_three_vertical2-1][column_ship_three_vertical2-1] == "D"\
            and self.board_player_two[row_ship_three_vertical2][column_ship_three_vertical2-1] == "D" and self.board_player_two[row_ship_three_vertical2+1][column_ship_three_vertical2-1] == "D"\
            and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2-1] == "E" and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2] == "E"\
            and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+1] == "E" and self.board_player_two[row_ship_four_horizontal2-1][column_ship_four_horizontal2+2] == "E"\
            and self.board_player_two[row_ship_four_vertical2-1][column_ship_four_vertical2-1] == "F" and self.board_player_two[row_ship_four_vertical2][column_ship_four_vertical2-1] == "F"\
            and self.board_player_two[row_ship_four_vertical2+1][column_ship_four_vertical2-1] == "F" and self.board_player_two[row_ship_four_vertical2+2][column_ship_four_vertical2-1] == "F":
            self.clear()
            time.sleep(1)
            self.show_players("1w")
            self.print_board_player_two()
            raw_input("Press ENTER")
            self.clean_lists()
            self.clear()
            time.sleep(1)
            self.multi_play_again()
        else:
            self.clear()
            time.sleep(1)
            pass

        print "... Your turn. PLAYER 2 ..."

        ask = raw_input("\nDo you want to see your board?  y/n  ")
        ask = ask.lower()
        self.clear()
        time.sleep(1)

        if ask == "y":
            print "\nHere you will see the shots of PLAYER 1\n"
            self.print_board_player_two()
            raw_input("Press ENTER ")
            self.clear()
            time.sleep(1)
        else:
            self.clear()
            time.sleep(1)
            pass

        while True:
            self.show_players("2")
            self.print_board_player_one()
            row, column = self.alone_the_user()

            if row == row_bomb and column == column_bomb:
                self.board_player_one[row-1][column-1] = "#"
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
                time.sleep(1)
                print "CONGRATULATIONS YOU SHOT TO THE BOMB, THE SHIPS HAVE SUNK\n"
                self.show_players("2w")
                self.print_board_player_one()
                raw_input("\nPress ENTER ")
                self.clean_lists()
                self.clear()
                time.sleep(1)
                self.multi_play_again()
            else:
                if (row < 1 or row > 10) or (column < 1 or column > 10):
                    self.clear()
                    time.sleep(1)
                    print "IT IS NOT IN THE OCEAN\n\n"

                elif self.board_player_one[row-1][column-1] == "X" or self.board_player_one[row-1][column-1] == "A"\
                or self.board_player_one[row-1][column-1] == "B" or self.board_player_one[row-1][column-1] == "C"\
                or self.board_player_one[row-1][column-1] == "D" or self.board_player_one[row-1][column-1] == "E"\
                or self.board_player_one[row-1][column-1] == "F":
                    self.clear()
                    time.sleep(1)
                    print "ALREADY YOU HAVE WRITTEN THOSE COORDINATES\n\n"

                elif row == row_ship_two_horizontal and column == column_ship_two_horizontal\
                or row == row_ship_two_horizontal and column == column_ship_two_horizontal+1:
                    self.board_player_one[row-1][column-1] = "A"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b1")
                    self.print_board_player_one()
                    raw_input("Press ENTER ")
                    self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_two_vertical and column == column_ship_two_vertical\
                or row == row_ship_two_vertical+1 and column == column_ship_two_vertical:
                    self.board_player_one[row-1][column-1] = "B"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b1")
                    self.print_board_player_one()
                    raw_input("Press ENTER ")
                    self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_three_horizontal and column == column_ship_three_horizontal\
                or row == row_ship_three_horizontal and column == column_ship_three_horizontal+1\
                or row == row_ship_three_horizontal and column == column_ship_three_horizontal+2:
                    self.board_player_one[row-1][column-1] = "C"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b1")
                    self.print_board_player_one()
                    raw_input("Press ENTER ")
                    self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_three_vertical and column == column_ship_three_vertical\
                or row == row_ship_three_vertical+1 and column == column_ship_three_vertical\
                or row == row_ship_three_vertical+2 and column == column_ship_three_vertical:
                    self.board_player_one[row-1][column-1] = "D"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b1")
                    self.print_board_player_one()
                    raw_input("Press ENTER ")
                    self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_four_horizontal and column == column_ship_four_horizontal\
                or row == row_ship_four_horizontal and column == column_ship_four_horizontal+1\
                or row == row_ship_four_horizontal and column == column_ship_four_horizontal+2\
                or row == row_ship_four_horizontal and column == column_ship_four_horizontal+3:
                    self.board_player_one[row-1][column-1] = "E"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b1")
                    self.print_board_player_one()
                    raw_input("Press ENTER ")
                    self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                elif row == row_ship_four_vertical and column == column_ship_four_vertical\
                or row == row_ship_four_vertical+1 and column == column_ship_four_vertical\
                or row == row_ship_four_vertical+2 and column == column_ship_four_vertical\
                or row == row_ship_four_vertical+3 and column == column_ship_four_vertical:
                    self.board_player_one[row-1][column-1] = "F"
                    self.clear()
                    time.sleep(1)
                    print "YOU HAVE SHOT TO A PART OF ONE SHIP"
                    self.show_players("b1")
                    self.print_board_player_one()
                    raw_input("Press ENTER ")
                    self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

                else:
                    self.board_player_one[row-1][column-1] = "X"
                    self.clear()
                    time.sleep(1)
                    print "You have failed"
                    self.show_players("b1")
                    self.print_board_player_one()
                    raw_input("Press ENTER ")
                    self.player_one(row_bomb, column_bomb, row_ship_two_horizontal, column_ship_two_horizontal,\
        row_ship_two_vertical, column_ship_two_vertical, row_ship_three_horizontal, column_ship_three_horizontal,\
        row_ship_three_vertical, column_ship_three_vertical, row_ship_four_horizontal, column_ship_four_horizontal,\
        row_ship_four_vertical, column_ship_four_vertical,\
        row_bomb2, column_bomb2, row_ship_two_horizontal2, column_ship_two_horizontal2,\
        row_ship_two_vertical2, column_ship_two_vertical2, row_ship_three_horizontal2, column_ship_three_horizontal2,\
        row_ship_three_vertical2, column_ship_three_vertical2, row_ship_four_horizontal2, column_ship_four_horizontal2,\
        row_ship_four_vertical2, column_ship_four_vertical2)

    def multi_play_again(self):
        while True:
            time.sleep(1)
            option_user = raw_input("DO YOU WANT TO PLAY AGAIN y/n:  ")
            option_user = option_user.lower()

            if option_user == "y":
                self.clean_lists()
                self.clear()
                time.sleep(1)
                self.place_ships_players()
            elif option_user == "n":
                self.clean_lists()
                time.sleep(1)
                self.clear()
                self.menu()
            else:
                self.clear()
                time.sleep(1)
                print "Only can write -y- or -n- \n"

    def instructions(self):
        print "---------------------INSTRUCTIONS-------------------"
        print "----SINGLE PLAYER:----"
        print "\nWHEN YOU GUESS RIGHT THE POSITION OF ONE PART OF THE SHIP"
        print "WILL APPEAR ONE OF THESE SYMBOLS |A|, |B|, |C|, |D|, |E|, |F|"
        print "WHEN YOU DO NOT GUESS RIGHT, WILL APPEAR THIS SYMBOL |X|"
        print "WHEN YOU SHOOT TO THE BOMB, WILL APPEAR THIS SYMBOL |#|"
        print "AND YOU WILL WIN AUTOMATICALLY"
        print "YOU HAVE 10 LIVES"

        print "\n----MULTI PLAYER:-----"
        print "\nWHEN ONE OF YOU GUESS RIGHT THE POSITION OF ONE PART OF THE SHIP"
        print "WILL APPEAR ONE OF THESE SYMBOLS |A|, |B|, |C|, |D|, |E|, |F|"
        print "WHEN ONE OF YOU DO NOT GUESS RIGHT, WILL APPEAR THIS SYMBOL|X|"
        print "WHEN ONE OF YOU SHOOT TO THE BOMB, WILL APPEAR THIS SYMBOL |#|"
        print "AND ONE OF YOU WILL WIN AUTOMATICALLY"
        raw_input("\nPress ENTER to return the menu")
        self.clear()
        self.menu()
        
    def menu_print(self):
        print "WELCOME TO BATTLESHIP"
        print "\n --1. SINGLE PLAYER"
        print "\n --2. TWO PLAYERS"
        print "\n --3. INSTRUCTIONS"
        print "\n --4. EXIT"

    def menu_option(self):
        while True:
            option_user = raw_input(" \n-- ")
            if option_user == "1":
                self.clear()
                self.player_alone()
            elif option_user == "2":
                self.clear()
                self.place_ships_players()
            elif option_user == "3":
                self.clear()
                self.instructions()
            elif option_user == "4":
                self.clear()
                sys.exit()
            else:
                self.clear()
                print "INVALID OPTION"
                self.menu()

    def menu(self):
        self.clear()
        self.menu_print()
        self.menu_option()

MAIN = MultiPlayer()
MAIN.menu()