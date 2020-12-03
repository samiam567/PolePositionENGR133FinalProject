
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
import Playercar
import Computercar
import Racetrack
from math import sin,cos,pi
import pygame
import time
import threading


# runs the necessary functions and classes to run pole position


objectDraw = ObjectDraw(1000,800); #create objectDraw

useFirstPerson = input("Do you want to use first person mode? yes(y) or no(n)");
useFirstPerson = useFirstPerson.lower();

# if the user's answer starts with "y" then use first person
firstPerson = (useFirstPerson[0] == "y")

racecar = Playercar.Playercar(objectDraw,firstPerson); # create the playercar
cpu = Computercar.Computercar(objectDraw,firstPerson,racecar); # create the cpu
racetrack = Racetrack.Racetrack(objectDraw,racecar,firstPerson); # create the racetrack

cpu.setRacetrack(racetrack);

'''
add to objectdraw
'''
objectDraw.add(racetrack);
objectDraw.add(cpu);
objectDraw.add(racecar);


#set the background color
objectDraw.setBackgroundColor((0,255,0));

#start the game engine
objectDraw.start();

turnAmount = 0;


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
