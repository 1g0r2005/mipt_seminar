import pygame
from pygame.draw import *

pygame.init()

FPS = 30
d = 0.5
scr_x = 794*d
scr_y = 1123*d
screen = pygame.display.set_mode((scr_x,scr_y))
screen.fill((255,255,255))

rect(screen,(102,255,255),(0,0,scr_x,scr_y/2))
line(screen,(0,0,0),(0,scr_y/2),(scr_x,scr_y/2))
#bear
ellipse(screen,(210,210,210),(133*d,425*d,177*d,95*d))
ellipse(screen,(0,0,0),(133*d,425*d,177*d,95*d),width=1)

ellipse(screen,(210,210,210),(6*d,486*d,257*d,467*d))
ellipse(screen,(0,0,0),(6*d,486*d,257*d,467*d),width=1)

ellipse(screen,(210,210,210),(215*d,593*d,115*d,49*d))
ellipse(screen,(0,0,0),(215*d,593*d,115*d,49*d),width=1)

ellipse(screen,(210,210,210),(142*d,808*d,190*d,155*d))
ellipse(screen,(0,0,0),(142*d,808*d,190*d,155*d),width=1)

ellipse(screen,(210,210,210),(256*d,929*d,140*d,50*d))
ellipse(screen,(0,0,0),(256*d,929*d,140*d,50*d),width=1)

circle(screen,(0,0,0),(213*d,455*d),5)
circle(screen,(0,0,0),(308*d,458*d),5)

#
ellipse(screen,(76,76,76),(445*d,779*d,311*d,105*d))
ellipse(screen,(0,0,0),(445*d,779*d,311*d,105*d),width=1)

ellipse(screen,(22,80,68),(477*d,814*d,240*d,66*d))
ellipse(screen,(0,0,0),(477*d,814*d,240*d,66*d),width=1)

#
circle(screen,(245,245,245),(481*d,193*d),57//4)
circle(screen,(161,249,228),(481*d,193*d),285/2,width=45//2)
pygame.display.update()


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

