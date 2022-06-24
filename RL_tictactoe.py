import tictactoe as ttt
import itertools
import numpy as np
import pygame as pg
import sys
import time
from pygame.locals import *

# this is used to track time
CLOCK = pg.time.Clock()
fps = 30

A = np.array([a for a in itertools.product(range(3), range(3))])

def get_state():
	print(ttt.board)
    #for row in range(0, 3):
    #    for col in range(0,3):
    #        board[row, cwol]
        
def pass_action():
    if ttt.winner == None:
        board = np.array(ttt.board)
        flattened_board = board.flatten()
        action_space = A[ flattened_board == None ]
        choice = np.random.randint(action_space.shape[0], size = 1)
        row, col = action_space[choice][0] + 1
        print('chosen action: (', row, col, ')')
        ttt.drawXO(row, col)
        ttt.check_win()
    else:
        print('Game already over')





ttt.game_initiating_window()

while(True):
	# if ( pg.key.get_pressed()[pg.K_q] == True):
	# 	get_state()
	# if ( pg.key.get_pressed()[pg.K_w] == True):
	# 	pass_action()
	# if ( pg.key.get_pressed()[pg.K_DOWN] == True ):
	# 	ttt.user_click()

	# 	if( ttt.winner or ttt.draw):
	# 		ttt.reset_game()
	for event in pg.event.get():

		if event.type == QUIT:
			pg.quit()
			sys.exit()
        
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_w:
				get_state()
			elif event.key == pg.K_q:
				pass_action()
			elif event.key == pg.K_DOWN:
				ttt.user_click()
				if( ttt.winner or ttt.draw):
					ttt.reset_game()


		# elif event.type == pg.K_DOWN: # is MOUSEBUTTONDOWN:
		#	user_click()

		#	if(winner or draw):
		#		reset_game()

	pg.display.update()
	CLOCK.tick(fps)
