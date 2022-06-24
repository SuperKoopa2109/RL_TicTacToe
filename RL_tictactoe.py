# importing the required libraries
import pygame as pg
import sys
import time
from pygame.locals import *
# import RL_tictactoe as rlttt

class TicTacToe():
    def __init__(self, starting_player:str = 'x', reward: object = None) -> None:
        # declaring the global variables

        # for storing the 'x' or 'o'
        # value as character
        self.XO = starting_player

        # storing the winner's value at
        # any instant of code
        self.winner = None

        # to check if the game is a draw
        self.draw = None

        # setting up a 3 * 3 board in canvas
        self.board = [[None]*3, [None]*3, [None]*3]

        if reward == None:
            reward = {'win': 1, 'draw': 0, 'lose': -1, 'playing': None}
        
        self.reward = reward

    def get_curr_player(self):
        return self.XO

    def check_win(self):
        
        reward = 'playing'

        # checking for winning rows
        for row in range(0, 3):
            if((self.board[row][0] == self.board[row][1] == self.board[row][2]) and (self.board [row][0] is not None)):
                self.winner = self.board[row][0]
                reward = 'win'
                break

        # checking for winning columns
        for col in range(0, 3):
            if((self.board[0][col] == self.board[1][col] == self.board[2][col]) and (self.board[0][col] is not None)):
                self.winner = self.board[0][col]
                reward = 'win'
                break

        # check for diagonal winners
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[0][0] is not None):
            
            # game won diagonally left to right
            self.winner = self.board[0][0]
            
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2] is not None):
            
            # game won diagonally right to left
            self.winner = self.board[0][2]

        if(all([all(row) for row in self.board]) and self.winner is None ):
            self.draw = True

        




    def drawXO(self, row, col):
            
        # setting up the required board
        # value to display
        self.board[row-1][col-1] = self.XO
        
        if(self.XO == 'x'):
            
            # pasting x_img over the screen
            # at a coordinate position of
            # (pos_y, posx) defined in the
            # above code
            self.XO = 'o'
        
        else:
            self.XO = 'x'

    def choose_action(self, row, col):
        self.drawXO(row, col)
        return self.check_win()

    def reset_game(self):
        
        self.XO = 'x'
        self.draw = False
        self.winner = None
        self.board = [[None]*3, [None]*3, [None]*3]

    def run_game(self):
        while(True):
            if ( pg.key.get_pressed()[pg.K_q] == True):
                rlttt.get_state()
            if ( pg.key.get_pressed()[pg.K_DOWN] == True ):
                user_click()

                if( winner or draw):
                    reset_game()
            for event in pg.event.get():

                if event.type == QUIT:
                    pg.quit()
                    sys.exit()


