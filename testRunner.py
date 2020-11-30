
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''

from game_engine.ObjectDraw import ObjectDraw
from game_engine.RelativeSprite import RelativeSprite
from game_engine.Sprite import Sprite
from math import sin,cos,pi
import pygame
import time
import threading

# a test runner to test the engine



            
objectDraw = ObjectDraw(800,600); #create objectDraw



car = Sprite("racecar",100,100,1,"assets/racecar.png");

car.setAngularVelocity(1);

    
'''
add to objectdraw
'''

objectDraw.add(car);


#start the game engine
objectDraw.start();


while(not objectDraw.done):
    
    objectDraw.run(); # run the game engine stuff


   








'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
