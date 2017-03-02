import time
import pygame
import sys
import os

def show_date_time(screen):
    current_time = time.struct_time(time.localtime())
    year = current_time.tm_year
    month = current_time.tm_mon

    if month == 1:
        month = 'Jan'
    elif month == 2:
        month = 'Feb'
    elif month == 3:
        month = 'Mar'
    elif month == 4:
        month = 'Apr'
    elif month == 5:
        month = 'May'
    elif month == 6:
        month = 'Jun'
    elif month == 7:
        month = 'Jul'
    elif month == 8:
        month = 'Aug'
    elif month == 9:
        month = 'Sep'
    elif month == 10:
        month = 'Oct'
    elif month == 11:
        month = 'Nov'
    elif month == 12:
        month = 'Dec'

    day = current_time.tm_mday
    hour = current_time.tm_hour
    minute = current_time.tm_min
    sec = current_time.tm_sec

    wday = current_time.tm_wday

    if wday == 0:
        wday = 'MON'
    elif wday == 1:
        wday = 'TUE'
    elif wday == 2:
        wday = 'WED'
    elif wday == 3:
        wday = 'THU';
    elif wday == 4:
        wday = 'FRI'
    elif wday == 5:
        wday = 'SAT'
    elif wday == 6:
        wday = 'SUN'

    
    date = wday + ', ' + month + ',{day},{year}'.format(day = day, year = year)
    datefont = pygame.font.SysFont("Roboto", 70)
    dateDisp = datefont.render(date, 10, (255, 255, 255))
    screen.blit(dateDisp, (500, 0))

    clk = '%02d:%02d:%02d'% (hour, minute, sec)
    clkfont = pygame.font.SysFont("Roboto", 100)
    clkDisp = clkfont.render(clk, 10, (255, 255, 255))
    screen.blit(clkDisp, (650, 80))
    


