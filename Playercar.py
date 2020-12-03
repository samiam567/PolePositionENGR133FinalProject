
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Final Project
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
===============================================================================
'''
from math import sqrt,cos,sin,pi
from game_engine.RelativeSprite import RelativeSprite
import Racecar
import pygame

# a racecar controlled by the player
'''
class members:
turnAmount - float - the current turn of the wheels ; how much the car will turn this frame
racecarSpeed - float - how fast the racecar should be going
racetrack - Racetrack - the racetrack we will be driving on  ;   for figuring out if we are on the track and CPU driving
racetrackSet - boolean - whether we have set a racetrack yet
racecarAcceleration - float - how fast we accelerate (how big the engine is)
racecarTurnSpeed - float - how fast we turn initially
racecarTurnAcceleration - float - how much more we turn each frame (accelerative turning)

'''


class Playercar(Racecar.Racecar):
    def __init__(self,objectDraw,isFirstPerson):
        racecar_source = "assets/racecar2.png";

        #these control the size of the car
        if isFirstPerson:
            diagonalMultiplier = 0.00003;
        else:
            diagonalMultiplier = 0.000015;

        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;

        diagonal = sqrt(screenXSize**2 + screenYSize**2);
        scale = diagonal*diagonalMultiplier;
        
        super(Playercar,self).__init__(objectDraw,isFirstPerson,scale,racecar_source);

        

        #set psrameters and settings for the car
        if isFirstPerson:
            self.setCamera(self);
            self.racecarAcceleration = 0.5;
            self.racecarTurnSpeed = 2;
            self.racecarTurnAcceleration = 0.33;
        else:
            self.racecarAcceleration = 0.16;
            self.racecarTurnSpeed = 4;
            self.racecarTurnAcceleration = 0.43;

        self.racecarSpeed = 0;

        
    def update(self):
        super(Playercar,self).update();

        '''
        drive the car according to user input
        '''

        # get the keys that the user has pressed
        keysPressed = self.objectDraw.getKeysPressed();

        #calculate the angle the car is at
        raceCarAngle = pi*(-90+self.getRotation())/180;


        # acclerate if the user presses "w"
        if (keysPressed[pygame.K_w]):
            self.racecarSpeed += self.racecarAcceleration;
        elif(keysPressed[pygame.K_s]):
            self.racecarSpeed -= self.racecarAcceleration;

        # set our speed to the target speed in the direction we are facing 
        self.setSpeed((self.racecarSpeed*cos(raceCarAngle),self.racecarSpeed*sin(raceCarAngle)));


        # turn if the user presses "a" or "d"
        if (keysPressed[pygame.K_a]):
            self.setAngularVelocity(-self.turnAmount);
            self.turnAmount+=self.racecarTurnAcceleration; # turn faster the longer we are turning
        elif (keysPressed[pygame.K_d]):
            self.setAngularVelocity(self.turnAmount);
            self.turnAmount+=self.racecarTurnAcceleration; # turn faster the longer we are turning

        else: # if we aren't pressing anything don't turn, set the turn speed back to the base speed
            self.setAngularVelocity(0);
            self.turnAmount = self.racecarTurnSpeed;


        '''
        check if we are off the track
        '''
        if (self.racetrackSet):

            if (not self.racetrack.isOnTrack(self.xPosition,self.yPosition)):
                print("We are off the track!");
            else:
                print("");
                
        









'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
