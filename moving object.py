'''
如何設計給定初始方向會自己移動，碰到邊緣會彈回
by Ching-Shoei Chiang
'''
import random, pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('object moving')
WHITE = (255, 255, 255)

circleImg = pygame.image.load('circle64.png')
circlex = circley = 400
dirx = 2
diry = 1
step = 10

while True:
    for event in pygame.event.get():
        if event.type == QUIT:                                                    
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
    if circley>736 or circley<0:
        diry = -1 * diry
    if circlex>736 or circlex<0:
        dirx = -1 * dirx
    circlex = circlex + dirx*step
    circley = circley + diry*step
    screen.blit(circleImg, (circlex, circley))
    
    screen.fill(WHITE)
    screen.blit(circleImg, (circlex, circley))         
    pygame.display.update()

    fpsClock.tick(FPS)
