
import pygame
from math import sin, pi
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# This sets the name of the window
pygame.display.set_caption('CMSC 150 is cool')
 
clock = pygame.time.Clock()

# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("../assets/FBI Open Up.wav")
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
spinSpeed = 5;
rotation = 0;

player_image = pygame.image.load("../assets/racecar.png").convert();
imgSizeX = 200;
imgSizeY = 200;

player_image = pygame.transform.scale(player_image, (imgSizeX,imgSizeY));

player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
 
    # Copy image to screen:
    screen.fill(WHITE)
  #  screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
    
    displayImg = pygame.transform.rotate(player_image,rotation);
    displayImg = pygame.transform.scale(displayImg, (imgSizeX,imgSizeY));
    
    screen.blit(displayImg, [x-imgSizeX/2, y-imgSizeY/2])

    #rotate spinner
    
 #   rotation = rotation + spinSpeed;
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
