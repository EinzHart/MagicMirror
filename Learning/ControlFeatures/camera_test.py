import picamera
import pygame
import numpy as np

from pygame.locals import *

def camera_test():
    camera = picamera.PiCamera()
    camera.hflip = True
    camera.resolution= (720, 540)
    image = np.zeros((540, 720, 3), dtype = np.uint8)
    camera.start_preview()
    camera.annotate_text = 'CAM_TEST\nPress RIGHT to return'
    while 1:
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
            if event.key == K_RIGHT:
                camera.stop_preview()
                camera.close()
                return
            elif event.key == K_SPACE:
                camera.annotate_text = ''
                camera.capture('foo.jpg')                
                camera.annotate_text = 'SCREENSHOT\nPress RIGHT to return'        
        
         
    
