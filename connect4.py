ROWS = 6
COLUMNS = 7 
import sys

B = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
T = 0


class PlayerManager:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Referee:
    def check_direction(self, board, r, c, dr, dc, player):
        try: 
            return all(
                board[r + i*dr][c + i*dc] == player
                for i in range(4)
             )
        except IndexError:
             return False

    def check_win(self, board, player):

        for r in range(ROWS):
            for c in range(COLUMNS):

                if self.check_direction(board, r, c, 1, 0, player):
                    return True

                if self.check_direction(board, r, c, 0, 1, player):
                    return True

                if self.check_direction(board, r, c, 1, 1, player):
                    return True
                if self.check_direction(board, r, c, 1, -1, player):
                    return True
        
        return False

def print_board():
    for row in B:
        print("|" + "|".join(row) + "|")


def place_piece(board, column, player):

    for r in range(ROWS - 1, -1, -1):
        if board[r][column] == ' ':
            board[r][column] = player
            return True

    return False


def logic_gate_proc():
    global T
    ref = Referee()
    pm = PlayerManager('X', 'O')
   
    while True:
        char = pm.p1 if T % 2 == 0 else pm.p2
       
        print_board()
       
        try:
           
            choice = int(input(f"Player {char} move: "))
           
            if choice < 0 or choice >= COLUMNS:
               print("Invalid column")
               continue
           
            if place_piece(B, choice, char):

               if ref.check_win(B, char):
                   print(f"{char} wins!")
                   break
                   
               T += 1
        except ValueError:
            print("Please enter a valid number")
           

logic_gate_proc()
