import pygame
from sys import exit

#Calling pygame, initiates it
pygame.init()

#Create the window
#Width, Height
screen = pygame.display.set_mode((800,400))
#Set title
pygame.display.set_caption("Running")

#Clock Object to help control frame rate
clock = pygame.time.Clock()

#Create surface with plain color
color_surface = pygame.Surface((100, 200))

#Adding color
color_surface.fill('Red')



#Game will run in the while loop
while (True):
    # Checking for all events
    for event in pygame.event.get():
        # If the vent type is quit, then it will close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            # Will end all code instantly
            exit()

    #Attach new surfaces with display surface
    # Arguemnts: surface, position
    screen.blit(color_surface, (0,0))

    #Draw all our elements
    # Update everything
    pygame.display.update()

    # 60 (frames) times per second
    clock.tick(60)