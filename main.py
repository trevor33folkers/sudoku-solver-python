import pygame

#color variables
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

#screen object
screen = pygame.display.set_mode((800,800))

#fill screen
screen.fill(white)

#update display
pygame.display.flip()

running = True

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False