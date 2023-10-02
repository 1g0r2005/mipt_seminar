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

#солнце
circle(screen,(161,249,228),(481*d,193*d),285/2,width=45//2)
polygon(screen,(161,249,228),([195*d,173*d],[763*d,185*d],[761*d,217*d],[195*d,207*d]))
polygon(screen,(161,249,228),([441*d,461*d],[468*d,461*d],[503*d,0],[463*d,0]))
circle(screen,(245,245,245),(481*d,193*d),57//4)
#прорубь
ellipse(screen,(76,76,76),(445*d,779*d,311*d,105*d))
ellipse(screen,(0,0,0),(445*d,779*d,311*d,105*d),width=1)

ellipse(screen,(22,80,68),(477*d,814*d,240*d,66*d))
ellipse(screen,(0,0,0),(477*d,814*d,240*d,66*d),width=1)
#удочка
line(screen,(0,0,0),[633*d,335*d],[642*d,834*d])
lines(screen,(0,0,0),False,[[633*d,335*d],[563*d,384*d],[409*d,506*d],[321*d,592*d],[316*d,599*d],[292*d,640*d],[265*d,696*d]],4)
#медведь
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

aalines(screen,(0,0,0),False,[[199*d,491*d],[255*d,491*d],[274*d,490*d],[291*d,487*d],[297*d,485*d],[303*d,484*d]])

polygon(screen,(210,210,210),([159*d,452*d],[164*d,451*d],[172*d,443*d],[177*d,436*d],[173*d,430*d],[165*d,426*d],[157*d,426*d],[152*d,428*d],[148*d,434*d],[147*d,438*d],[150*d,446*d]))
polygon(screen,(0,0,0),([159*d,452*d],[164*d,451*d],[172*d,443*d],[177*d,436*d],[173*d,430*d],[165*d,426*d],[157*d,426*d],[152*d,428*d],[148*d,434*d],[147*d,438*d],[150*d,446*d]),1)

#рыба попытка в произвольную рыбу

def fish(x0,y0,d=0.5):#606,974
    circle(screen,(121,121,242),((x0+54)*d,(y0-12)*d),10)
    circle(screen,(126,132,140),((x0+56)*d,(y0-9)*d),4)
    print(x0,y0)
    print((x0+46)//2,(y0-15)//2,(x0+53)//2,(y0-10)//2)
    ellipse(screen,(0,0,0),((x0+46)//2,(y0-15)//2,(x0+53)//2,(y0-10)//2))
    ellipse(screen,(255,0,0),((x0+46)//2,(y0-15)//2,482,329))
    circle(screen,(255,0,0),((x0+46)//2,(y0-15)//2),2)###
    circle(screen,(255,0,0),((x0+53)//2,(y0-10)//2),2)###
fish(606,974)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

