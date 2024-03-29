
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''
import pygame
import sys
from threading import Thread
from game_engine.Sprite import Sprite;
from game_engine.GameEngineToolbox import checkType;
from game_engine.GameObject import GameObject;

# Controller for the game engine. Updates and draws the objects on a Pygame window
'''
Class members:
screenSizeX - int - x size of the screen
screenSizeY - int - y size of the screeb
WHITE - tuple - represents the color white
BLACK - tuple - represents the color black
screen - pygame.surface - the screen we are using to put objects on
clock - Clock - the pygame clock. We will use this to set delays
done - boolean - whether the engine is done running yet. Setting this to false will stop the engine
objects - list[GameObject] (manually enforced) - a list of object for the engine to 
tickSpeed - int - analogous to frames per second. (1/wait time inbetween frames)
keysPressed - list[boolean] - the keys that are currently pressed down as fetched by pygame.key.get_pressed()
backgroundColor - tuple - the background color for the screen. Painted before all other objects
'''

class ObjectDraw():
    
    #initializes the objectdraw
    def __init__(self,screenSizeX, screenSizeY):

        #make sure types check out and assign screen size class members
        checkType(screenSizeX,int,"screenSizeX must be an int");
        checkType(screenSizeY,int,"screenSizeY must be an int");
        self.screenSizeX = screenSizeX;
        self.screenSizeY = screenSizeY;
        
        #define colors
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)

        #initialize pygame
        pygame.init();

        self.screen = pygame.display.set_mode([screenSizeX, screenSizeY]) # get the screen

        pygame.display.set_caption("Lil' game engine -- programmed by Alec Pannunzio"); #set the title of our display
        
        self.clock = pygame.time.Clock(); # get the clock

        
        #set up variables

        self.objects = []; # create the objects list

        self.done = True;

        self.tickSpeed = 60;

        self.keysPressed = [];

        self.backgroundColor = self.WHITE;

    # sets tickSpeed
    def setTickSpeed(self,newTick):
        checkType(newTick,int,"tickSpeed must be an integer");
        self.tickSpeed = newTick;

    #sets the background color
    def setBackgroundColor(self,newColor):
        checkType(newColor,tuple,"backgroundColor must be a tuple");
        self.backgroundColor = newColor;
    
    # will start the game engine  
    def start(self):
        if (self.done): #make sure we aren't already running
            self.done = False;
        else:
            print("engine already running");

            
    # will pause the game engine
    def pause(self):
        self.done = True;

    #will stop the game engine
    def stop(self):
        print("stopping");
        self.done = True;
        pygame.quit();

    #should only be called by start(), runs the game engine loop
    def run(self):
        if (True):
            #set keysPressed
            self.keysPressed = pygame.key.get_pressed();

            # handle pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("shutting down");
                    #shut 'er down
                    done = True;
                    pygame.display.quit();
                    pygame.quit();
                    sys.exit();
                    return;
                elif event.type == pygame.MOUSEBUTTONDOWN: # when the mouse is clicked
                    pass;
            
           
            
            #update the objects
            for current_object in self.objects:
                current_object.update();
            
            # draw background
            self.screen.fill(self.backgroundColor)

            #paint the objects
            for current_object in self.objects:
                current_object.paint(self.screen);


            pygame.display.flip(); #push the updates to the display
            
            self.clock.tick(self.tickSpeed); # delay for a bit inbetween frames

    # will add the gameObject to the game engine to be run
    def add(self,gameObject):
        assert issubclass(gameObject.__class__, GameObject); # make sure the object we are adding is a child of GameObject
        self.objects.append(gameObject);

    #returns the keys that the user has pressed
    def getKeysPressed(self):
        return self.keysPressed;

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
