
import datetime
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((829, 836))
secoond = pygame.image.load("habd2.PNG")
minnuute = pygame.image.load("hand1.PNG")
screeeen = pygame.image.load("IMG_9937.jpg")
pygame.display.set_caption("mickey clock")
second2 = pygame.transform.scale(secoond, (546, 140))
minute2 = pygame.transform.scale(minnuute, (410, 180))
clock = pygame.time.Clock()

def timeline(surface, image, topleft, angle):
    rotated = pygame.transform.rotate(image, angle)
    rectg = rotated.get_rect(center = image.get_rect(topleft = topleft).center)
    surface.blit(rotated, rectg)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(screeeen, (0, 0))
    time = datetime.datetime.now()
    minuteok = time.minute
    secondok = time.second
    timeline(screen, second2, (135, 345), secondok* -6)
    timeline(screen, minute2, (190, 320), minuteok* -6)
    pygame.display.flip()
    clock.tick(60)


