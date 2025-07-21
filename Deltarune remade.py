import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Deltarune in a nutshell")

#Set the font and da text (yippi)
font = pygame.font.SysFont(None, 48) 
text = font.render("PEAK", True, (0, 0, 0)) 

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(text, (100, 25))    

    pygame.display.flip()            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
