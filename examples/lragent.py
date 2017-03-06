import time
import numpy as np
import sys
import csv
import pygame
from ple.games.flappybird import FlappyBird
from ple import PLE



game = FlappyBird()
nb_frames = 15000
data=np.genfromtxt('weights.csv',delimiter=',',dtype=float)
weights=np.matrix(data[0:9])
bias=data[9]
p = PLE(game, fps=30, display_screen=True)
p.init()


class lrAgent():
    """
           lr picks based on the weights
    """
    def __init__(self, actions):
        self.actions = actions

    def pickAction(self, reward, obs):
	time.sleep(.15)	
        state=game.getGameState()
        playerY=state["player_y"]
        nextTopY=state["next_pipe_top_y"]
        nextBottomY=state["next_pipe_bottom_y"]
        nextDistance=state["next_pipe_dist_to_player"]
        nnextTopY=state["next_next_pipe_top_y"]
        nnextBottomY=state["next_next_pipe_bottom_y"]
        nnextDistance=state["next_next_pipe_dist_to_player"]
        result=0
        flap_states=np.matrix([119,result,playerY,nextTopY,nextBottomY,nextDistance,nnextTopY,nnextBottomY,nnextDistance])
        nflap_states=np.matrix([0,result,playerY,nextTopY,nextBottomY,nextDistance,nnextTopY,nnextBottomY,nnextDistance])
        fr= np.dot(weights,flap_states.transpose())
        nfr=np.dot(weights,nflap_states.transpose())
        print fr,nfr
        if fr>nfr:
            return 119
        else:
            return None
        



agent = lrAgent(p.getActionSet())
reward = 0.0
for i in range(nb_frames):
      
   if p.game_over():
         p.reset_game() 
   
   observation = p.getScreenRGB()
   action = agent.pickAction(reward, observation)
   reward = p.act(action)
   state = game.getGameState()
   player_y = state["player_y"]
   distance = state["next_pipe_dist_to_player"]
   pipe_x = state["next_pipe_x"]

   
pygame.display.quit()

pygame.quit()
sys.exit()
