import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

let = None
oLet = None

class TicTacToe:

    def __init__(self):
        self.board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "
        }
        self.current_winner = None
        self.player = "X"
        self.oPlayer = "O"

        let = self.player
        oLet = self.oPlayer



    def print_board(self):
        print("\n" * 2)

        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]}")
        print(f"---|---|---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]}")
        print(f"---|---|---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]}")

    
    def print_numbers(self):
        print("\n" * 2)

        numbers = [[str(i + 1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in numbers:
            print(" " + " | ".join(row))
            if row != ["7", "8", "9"]:
                print(f"---|---|---")


    def insert_letter(self, letter, position):
        if self.space(position):
            self.board[position] = letter
            if self.win():
                self.current_winner = letter
            return True
        else:
            return False



    def win(self):
        for i in range(1, 4):
            if (self.board[i] == self.board[i + 3] and self.board[i + 3] == self.board[i + 6] and self.board[i] != " "):
                return self.board[i]

        for i in [1, 4, 7]:
            if (self.board[i] == self.board[i + 1] and self.board[i + 1] == self.board[i + 2] and self.board[i] != " "):
                return self.board[i]

        if (self.board[1] == self.board[5] and self.board[5] == self.board[9] and self.board[1] != " "):
            return self.board[i]

        if (self.board[3] == self.board[5] and self.board[5] == self.board[7] and self.board[3] != " "):
            return self.board[i]

        return False


    def draw(self):
        for key in self.board.keys():
            if self.space(key):
                return False
            
        return True


    def space(self, position):
        if self.board[position] == " ":
            return True
        else:
            return False

    
    def valid_moves(self):
        return [key for key in self.board.keys() if self.board[key] == " "]


    def num_valid_moves(self):
        return [self.board[key] for key in self.board.keys()].count(" ")


def play(game, xPlayer, oPlayer):
    game.print_board()
    letter = "X"
    while not game.draw():
        if letter == "X":
            square = xPlayer.get_move(game)
        else:
            square = oPlayer.get_move(game)

        if game.insert_letter(letter, square):
            
            game.print_board()
            print(letter + f" Hamlesini Yaptı ({square})")
            
            print("\n")

            if game.current_winner:
                print(letter, "Kazandı!")
                return letter

            letter = "O" if letter == "X" else "X"

        time.sleep(.6)

    print("Beraberlik :(")

if __name__ == "__main__":
    t = TicTacToe()
    xPlayer = None
    oPlayer = None
    with open("configGame1.txt", "r") as f:
        f = f.read().split(",")
        
        if f[0] == "HumanPlayer":
            xPlayer = HumanPlayer("X")
        elif f[0] == "RandomComputerPlayer":
            xPlayer = RandomComputerPlayer("X")
        elif f[0] == "SmartComputerPlayer":
            xPlayer = SmartComputerPlayer("X")
        else:
            print("Lütfen Config Dosyasından Adam Akıllı Seçim Yapım")

        if f[1] == "HumanPlayer":
            oPlayer = HumanPlayer("O")
        elif f[1] == "RandomComputerPlayer":
            oPlayer = RandomComputerPlayer("O")
        elif f[1] == "SmartComputerPlayer":
            oPlayer = SmartComputerPlayer("O")
        else:
            print("Lütfen Config Dosyasından Adam Akıllı Seçim Yapım")

        play(t, xPlayer, oPlayer)

while True:
    "Nothing"