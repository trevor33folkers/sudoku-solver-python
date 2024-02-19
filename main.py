import pygame

#color variables
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

#screen object
screen = pygame.display.set_mode((1000,800))

#fill screen
screen.fill(white)

#update display
pygame.display.flip()

running = True

#draw grid function
def drawGrid():
    for i in range(0, 10):
        if (i%3 == 0):
            pygame.draw.line(screen, black, (40+80*i, 40), (40+80*i, 760), 4)
            pygame.draw.line(screen, black, (40, 40 + 80*i), (760, 40 + 80*i), 4)
        else: 
            pygame.draw.line(screen, black, (40+80*i, 40), (40+80*i, 760), 2)
            pygame.draw.line(screen, black, (40, 40 + 80*i), (760, 40 + 80*i), 2)
    pygame.display.update()

        

#main loop
while running:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()