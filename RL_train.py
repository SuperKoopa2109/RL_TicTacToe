from RL_tictactoe import TicTacToe
from RL_ttt_agent import TTT_Agent

if __name__ == '__main__':
    ttt_agent_x = TTT_Agent(player = 'x')
    ttt_agent_o = TTT_Agent(player = 'o')

    ttt_game = TicTacToe()
    
    for _ in range(10):
        finished = False
        i = 0
        while finished == False: 
            if ttt_game.get_curr_player() == 'x':
                action = ttt_agent_x.get_action()
            else:
                action = ttt_agent_o.get_action()
            
            reward = ttt_game.choose_action(action[0], action[1])

            i+=1
            if reward != 'playing':
                finished = True
                ttt_game.reset_game()
            elif i >= 5:
                break

