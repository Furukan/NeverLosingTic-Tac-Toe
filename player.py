import random
import math

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid = False
        value = None
        while not valid:
            val = input(f"Sırada {self.letter} Var. Seçimini Yap : ")
            try:
                val = int(val)
                if val not in game.valid_moves():
                    raise ValueError
                valid = True
                value = val
            except ValueError:
                print("Lütfen Düzgün Sayı Seç.")

        return value



class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        value = random.choice(game.valid_moves())
        return value



class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        return self.minimax(game, self.letter)["position"]

    def minimax(self, state, player):
        mPlayer = self.letter
        oPlayer = "X" if player == "O" else  "O"
        if state.current_winner == oPlayer:
            return {
                "position": None,
                "score": 1 * (state.num_valid_moves() + 1) if oPlayer == mPlayer else -1 * (state.num_valid_moves() + 1)
            }
        
        elif state.draw():
            return {
                "position": None,
                "score": 0
            }

        if player == mPlayer:
            best = {
                "position": None,
                "score": -math.inf
            }
        else:
            best = {
                "position": None,
                "score": math.inf
            }
        
        if state.num_valid_moves() == 9:
            return {
                "position": random.choice(state.valid_moves()),
                "score": math.inf
            }

        
        for possibleMove in state.valid_moves():
            state.insert_letter(player, possibleMove)
            sScore = self.minimax(state, oPlayer)

            state.board[possibleMove] = " "
            state.current_winner = None
            sScore["position"] = possibleMove

            if player == mPlayer:
                if sScore["score"] > best["score"]:
                    best = sScore
            else:
                if sScore["score"] < best["score"]:
                    best = sScore

        return best