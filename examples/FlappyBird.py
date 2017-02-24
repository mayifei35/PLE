import time
import numpy as np
import sys
import pygame
from ple.games.flappybird import FlappyBird
from ple import PLE
#from ple.games.flappybird._init_ import self.player.height


game = FlappyBird()
nb_frames = 15000
counter = 0
previousState = None
num = 0
top_y = 0
bottom_y = 0


p = PLE(game, fps=30, display_screen=True)
p.init()


class NaiveAgent():
    """
            This is our naive agent. It picks actions at random!
    """
    def __init__(self, actions):
        self.actions = actions

    def pickAction(self, reward, obs):
	time.sleep(.15)	
	if self.shouldFlap() == True:
	   return 119
	else:
	   return None

    def shouldFlap(self):
	global counter
	global previousState
	global num
	global top_y
	global bottom_y
	state = game.getGameState()
	distance = state["next_pipe_dist_to_player"]
	next_pipe_top_y = state["next_pipe_top_y"]
	player_pos_y = state["player_y"] + 30
	next_pipe_bottom_y = state["next_pipe_bottom_y"]
	player_v = state["player_vel"]
	#nxt_pipe_top_x = previousState["next_pipe]
	pipe_gap = next_pipe_bottom_y - next_pipe_top_y
	
	
	if (distance == 3.0) or (distance <= 143.0 and distance >= 127.0):  
	   if distance == 3.0: 
	      top_y = next_pipe_top_y
	      bottom_y = next_pipe_bottom_y 
	      if top_y + 5 < player_pos_y:
	         if bottom_y - 8 < player_pos_y:
		    return True
	      return False  
	   else:
	      if top_y + 5 < player_pos_y:
	         if bottom_y - 8 < player_pos_y:
		    return True
	      return False  
	   #previousState = state
           
	   
	else:	
	  if next_pipe_top_y + 5 < player_pos_y:
 	    if next_pipe_bottom_y - 8 < player_pos_y:
               return True

	  return False




agent = NaiveAgent(p.getActionSet())
print p.getActionSet()
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
   width = state["next_pipe_width"]
   #player_x = state["player_x"]
   pipe_x = state["next_pipe_x"]
   #dist = previousState["next_pipe_dist_to_player"]

   print distance
   print width
   #print player_x
   print pipe_x
   #print player_y
   #print action


pygame.display.quit()

pygame.quit()
sys.exit()
