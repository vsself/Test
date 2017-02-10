import curses
from wxPython._wx import false
from test.test_decimal import directory
from robotide.editor.dialoghelps import row

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))

class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.highscore = 0
        self.score = 0
        self.reset()
    def reset(self):
        # get the high score
        # reset the current score
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        # enter two num
    def if_win(self):
        if self.win_value <= self.score:
            return True
        else: return False
    def if_gameover(self):
        if (not can_move()) and self.score < self.win_value:
            return True
        else: return False
    def can_move(self, directory):
        def can_move_left(row):
            flag = False
            for i in range(len(row)-1):
                if row[i] == 0 and row[i+1] != 0:
                    flag = True
                    break
                if row[i] != 0 and row[i] == row[i+1]:
                    flag = True
                    break        
            return flag
        

def main(stdscr):
    def init():
        #draw the picture again
        return 'Game'
    def game():
        #wait the action
        if win:
            return 'Win'
        if gameover:
            return 'Gameover'
        return 'Game'
    def win():
        #draw the picture
        #wait the action 
        if restart:
            return 'Init'
    def gameover():
        #draw the picture
        #wait the action
        if restart:
            return 'Init'
    states_dict = {'Game': game, 'Init': init, 'Win': win, 'Gameover': gameover}
    state = 'Init'
    while state != 'Exit':
        state = states_dict[state]()
        
