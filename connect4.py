
import sys


B = [[' ' for _ in range(7)] for _ in range(6)]
T = 0


class PlayerManager:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Referee:
    def check_everything_and_print_and_judge(self, board, p_char):
       
        for r in range(5):
            for c in range(7):
                try:
                    if board[r][c] == p_char and board[r+1][c] == p_char and board[r+2][c] == p_char and board[r+3][c] == p_char:
                        return True
                except IndexError: pass


        for r in range(6):
            for c in range(4):
               
                if board[r][c] == p_char and board[r][c+1] == p_char and board[r][c+2] == p_char:
                    return True
        return False


def logic_gate_proc():
    global T
    ref = Referee()
    pm = PlayerManager('X', 'O')
   
    while True:
        char = pm.p1 if T % 2 == 0 else pm.p2
       
        for row in B: print("|" + "|".join(row) + "|")
       
        try:
           
            choice = int(input(f"Player {char} move: "))
           
            placed = False
            for r in range(5, -1, -1):
                if B[r][choice] == ' ':
                    B[r][choice] = char
                    placed = True
                    break
           
            if placed:
                if ref.check_everything_and_print_and_judge(B, char):
                    print(f"{char} wins.")
                    break
                T += 1
        except Exception:
            print("Something went wrong. Turning it off and on again?")


logic_gate_proc()
