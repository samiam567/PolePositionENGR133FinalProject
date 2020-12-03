
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
from game_engine.raytrace import raytrace;
import Racecar
import pygame

# a racecar controlled by the computer
'''
class members:
racecarSpeed - float - how fast the racecar should be going
racetrack - Racetrack - the racetrack we will be driving on  ;   for figuring out if we are on the track and CPU driving
racetrackSet - boolean - whether we have set a racetrack yet
racecarAcceleration - float - how fast we accelerate (how big the engine is)
sensorLength - float - the max distance we will probe in raytracing
sensorAngle - float - the angle from the front that the angled rays are for CPU driving
prevError - float - the error from the last PID loop
kP - float - the porportionallity constant for the PID controller
kD - float - the derivative constant for the PID controller
'''


class Computercar(Racecar.Racecar):
    def __init__(self,objectDraw,isFirstPerson,playercar):
        racecar_source = "assets/racecar.png"

        #these control the size of the car
        if isFirstPerson:
            diagonalMultiplier = 0.00015;
        else:
            diagonalMultiplier = 0.000075;

        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;

        diagonal = sqrt(screenXSize**2 + screenYSize**2);
        scale = diagonal*diagonalMultiplier;

        super(Computercar,self).__init__(objectDraw,isFirstPerson,scale,racecar_source);

        self.rotatePicture(90);
        
        #set psrameters and settings for the car
        if isFirstPerson:
            self.setCamera(playercar);
            self.racecarAcceleration = 0.5;
            self.kP = 0.2;
            self.kD = 0.3;
            self.racecarSpeed = 13;
            self.sensorLength = 100;
        else:
            self.racecarAcceleration = 0.1;
            self.kP = 0.3;
            self.kD = 0.3;
            self.racecarSpeed = 10;
            self.sensorLength = 50;

        #settings and parameters
        self.sensorAngle = 45;
        


        #PID variables
        self.prevError = 1;

        
    def update(self):
        super(Computercar,self).update();

        '''
        run the PD controller
        '''
        self.AICarControl();

        '''
        drive the car
        '''

        #calculate the angle the car is at
        raceCarAngle = pi*(-90+self.getRotation())/180;

        # set our speed to the target speed in the direction we are facing 
        self.setSpeed((self.racecarSpeed*cos(raceCarAngle),self.racecarSpeed*sin(raceCarAngle)));


        '''
        check if we are off the track
        '''
        if (self.racetrackSet):

            if (not self.racetrack.isOnTrack(self.xPosition,self.yPosition)):
                print("CPU is off the track!");
            else:
                print("");




    def AICarControl(self):
        position = 0;
        pError = 0;

        position = self.getPosition();
        forwardAngle = -90 + self.getRotation();

        '''
        get sensor readings
        '''

        #front right angle sensor
        frontRightAngleDist = raytrace(position,forwardAngle+self.sensorAngle,self.sensorLength,self.racetrack.isOnTrack,False);


        #front left angle sensor 
        frontLeftAngleDist = raytrace(position,forwardAngle-self.sensorAngle,self.sensorLength,self.racetrack.isOnTrack,False);
        
        #left sensor
        leftDist = raytrace(position,forwardAngle-90,self.sensorLength,self.racetrack.isOnTrack,False);
        
        #right sensor
        rightDist = raytrace(position,forwardAngle+90,self.sensorLength,self.racetrack.isOnTrack,False);
        
        #our relative position on the track
        position = frontRightAngleDist+rightDist-leftDist-frontLeftAngleDist;
        error = position;

        # calculate the PID calculation 
        PIDOutput = self.kP*error + self.kD * (error-self.prevError);

        # output the steering
        self.setAngularVelocity(PIDOutput);
        
        self.prevError = error;


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
