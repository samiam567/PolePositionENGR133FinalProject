
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
from edgeDetection.Input_Output import inputImage
from edgeDetection.Grayscale import grayscale
import pygame

# the racetrack that the car drives on. Also can tell the racecar if it is off the track and where the track edges are 
'''
class members:
racetrackEdges - pygame.surface - the edge-detected image showing the edges of the racetrack in white
racetrackRoad - pygame.surface - image containing the road in black and the rest in white
'''

racetrack_source = "assets/racetrack3.png"; #the filepath for the racetrack image
racetrackEdges_source = "assets/racetrack3Edges.png";
racetackRoad_source = "assets/racetrack3Road.png";

class Racetrack(RelativeSprite):
    def __init__(self,objectDraw,racecar,isFirstPerson):
        screenXSize = objectDraw.screenSizeX;
        screenYSize = objectDraw.screenSizeY;
        diagonal = sqrt(screenXSize**2 + screenYSize**2);

        # load in the edges and road images
        self.racetrackEdges = pygame.image.load(racetrackEdges_source).convert();
        self.racetrackEdges.set_colorkey((0,0,0));
        self.racetrackRoad = pygame.image.load(racetackRoad_source).convert();
        self.racetrackRoad.set_colorkey((0,0,0));

        

        
        #these control the size of the car
        if isFirstPerson:
            diagonalMultiplier = 0.002;
        else:
            diagonalMultiplier = 0.001;
            
        super(Racetrack,self).__init__("racetrack", screenXSize/2,screenYSize/2,diagonal*diagonalMultiplier,racetrack_source,objectDraw);

        if isFirstPerson:
            self.setCamera(racecar);
        #    self.img = pygame.transform.rotate(self.img,90);
        
        racecar.setRacetrack(self);

    # returns true if the passed coordinate is on the track
    def isOnTrack(self,x,y):

        #calcululate the indices in the picture array for the passed coordinate
        xPixelPos = int((x-self.xPosition+self.xSize/2)/self.imgScale);
        yPixelPos = int((y-self.yPosition+self.ySize/2)/self.imgScale);

        try:
            color = self.racetrackRoad.get_at((xPixelPos,yPixelPos)); # get the color at that pixel position
            
            brightness = 0.2126 * color.r + 0.7152 * color.g + 0.0722 * color.b; # convert to brightness
            print(brightness);
            return brightness < 200; # return whether that brightness is  dark enough to be the road (picture values are either 0 for on track or 254.999... for off track)
        except IndexError:
            print("off picture");
            return True;

            
            #return False;
            
    # returns true if the passed coordinate is the edge of the track
    def isTrackEdge(self,x,y):
        
        #calcululate the indices in the picture array for the passed coordinate
        xPixelPos = int((x-self.xPosition+self.xSize/2)/self.imgScale);
        yPixelPos = int((y-self.yPosition+self.ySize/2)/self.imgScale);

        color = self.racetrackEdges.get_at((xPixelPos,yPixelPos)); # get the color at that pixel position
        
        brightness = 0.2126 * color.r + 0.7152 * color.g + 0.0722 * color.b; # convert to brightness

        return brightness < 200; # return whether that brightness is  dark enough to be the road (picture values are either 0 for on track or 254.999... for off track)



'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
