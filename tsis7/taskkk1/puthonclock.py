#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock.
#Use Mickey's right hand as minutes arrow and left - as seconds.
import datetime
import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((829, 836))
sec = pygame.image.load("habd2.PNG")
min = pygame.image.load("hand1.PNG")
back = pygame.image.load("IMG_9937.jpg")
pygame.display.set_caption("mickey clock")
sec2 = pygame.transform.scale(sec, (546, 140))
min2 = pygame.transform.scale(min, (410, 180))
clock = pygame.time.Clock()

def transformed(surface, image, topleft, angle):
    rotated = pygame.transform.rotate(image, angle)
    rectg = rotated.get_rect(center = image.get_rect(topleft = topleft).center)
    surface.blit(rotated, rectg)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back, (0, 0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second
    transformed(screen, sec2, (135, 345), second* -6)
    transformed(screen, min2, (190, 320), minute* -6)
    pygame.display.flip()
    clock.tick(60)


