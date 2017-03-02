import pygame
import sys
import os

from pygame.locals import *
from ScreenFeatures.date_time import *
from ControlFeatures.demo_control1 import *
from ControlFeatures.camera_test import *


screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()
pygame.init()
BLACK = (0,0,0)


def show_text(screen, text = "default", pos = (0,0), color = (255, 255, 255)):
    font = pygame.font.SysFont("Roboto", 50)
    s = font.render(text, 10, color)
    screen.blit(s, pos)
    


while 1:
    clock.tick(20)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE:
            pygame.display.quit()
            pygame.quit()
            sys.exit(0)
        elif event.key == K_UP:
            control_feature_1(screen)
        elif event.key == K_LEFT:
            camera_test()
    screen.fill(BLACK)
    
    pygame.display.set_caption("HELLO EinzHart!")
    
    show_text(screen, text = 'DEMO')
    show_text(screen, text = 'Press UP to trigger CTRL1', pos = (300, 500))
    show_text(screen, text = 'Press LEFT to trigger CAM_TEST', pos = (300, 570))
    show_text(screen, text = 'Press ESC to Quit', pos = (300, 640))
    show_date_time(screen)
    pygame.display.flip()
