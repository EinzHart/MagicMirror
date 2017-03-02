import pygame
import sys
from pygame.locals import *

BLACK = (0,0,0)

def show_text(screen, text = "default", pos = (0,0), color = (255, 255, 255)):
    font = pygame.font.SysFont("Roboto", 50)
    s = font.render(text, 10, color)
    screen.blit(s, pos)
    

def control_feature_1(screen):
    posX = posY = 0
    while 1:
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
            if event.key == K_DOWN:
                return
        screen.fill(BLACK)

        pygame.display.set_caption('CTRL1')

        show_text(screen, text = 'CTRL1 DEMO', pos = (posX, posY))
        show_text(screen, text = 'press DOWN to return', pos =(300, 500)) 
        pygame.display.flip()
        posX = (posX+4) % 1024
        posY = (posY+3) % 768
        
        
                
