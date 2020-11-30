
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
import pygame

# it's a racecar! (Vroom vroom) -  basically just sets up the RelativeSprites to be used as a racecar
# note: must call setRaceTrack() for track awareness to work
'''
class members:
raceCarImg - pygame.Surface - the image of a racecar to be used for the sprite
racecarAcceleration - float - how fast we accelerate (how big the engine is)
racecarTurnSpeed - float - how fast we turn initially
raceCarTurnAcceleration - float - how much more we turn each frame (accelerative turning)
turnAmount - float - the current turn of the wheels ; how much the car will turn this frame
racecarSpeed - float - how fast the racecar should be going
racetrack - Racetrack - the racetrack we will be driving on  ;   for figuring out if we are on the track and CPU driving
racetrackSet - boolean - whether we have set a racetrack yet
'''

racecar_source = "assets/racecar2.png";
class Racecar(RelativeSprite):
    def __init__(self,objectDraw,isFirstPerson):
        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;
        diagonal = sqrt(screenXSize**2 + screenYSize**2);

        #these control the size of the car
        if isFirstPerson:
            diagonalMultiplier = 0.00005;
        else:
            diagonalMultiplier = 0.00001;
            
        super(Racecar,self).__init__("racecar", screenXSize/2,screenYSize/2,diagonal*diagonalMultiplier,racecar_source,objectDraw);

        #set psrameters and settings for the car
        if isFirstPerson:
            self.setCamera(self);
            self.setRotation(00);
            self.setZeroRotation(-90);
            self.racecarAcceleration = 0.5;
            self.racecarTurnSpeed = 4;
            self.racecarTurnAcceleration = 0.33;
        else:
            self.img = pygame.transform.rotate(self.img,0);
            self.racecarAcceleration = 0.1;
            self.racecarTurnSpeed = 3;
            self.racecarTurnAcceleration = 0.23;

        self.turnAmount = 0;
        self.racecarSpeed = 0;
        self.racetrack = None;
        self.racetrackSet = False;

    # sets the racetrack and allows track awareness to work
    def setRacetrack(self, racetrack):
        self.racetrack = racetrack;
        self.racetrackSet = True;


    def paint(self,screen):
        super(Racecar,self).paint(screen);
        pygame.draw.circle(screen,(0,255,255),(self.xPosition,self.yPosition),4);
        
    def update(self):
        super(Racecar,self).update();

        '''
        drive the car according to user input
        '''

        # get the keys that the user has pressed
        keysPressed = self.objectDraw.getKeysPressed();

        #calculate the angle the car is at
        raceCarAngle = pi*(self.getRotation())/180;


        # acclerate if the user presses "w"
        if (keysPressed[pygame.K_w]):
            self.racecarSpeed += self.racecarAcceleration;
        elif(keysPressed[pygame.K_s]):
            self.racecarSpeed -= self.racecarAcceleration;

        # set our speed to the target speed in the direction we are facing 
        self.setSpeed((-self.racecarSpeed*cos(raceCarAngle),-self.racecarSpeed*sin(raceCarAngle)));


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
                
        









'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
