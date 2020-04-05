import pygame
import pygame.mixer
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640, 480))
#sets title at top of window screen
pygame.display.set_caption('This Is The Game')

#creates the player object
circleSurfaceObj = pygame.image.load('thebluecircle.png')
whiteColor = pygame.Color(255, 255, 255)
redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
mousex, mousey = 0, 0


fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hover over red squares to get points.'

#plays music
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

while True:
    windowSurfaceObj.fill(whiteColor)
                                        #top, left, width, height
    pygame.draw.rect(windowSurfaceObj, redColor, (10, 10, 50, 50))
    pygame.draw.rect(windowSurfaceObj, redColor, (580, 420, 50, 50))
    pygame.draw.rect(windowSurfaceObj, redColor, (580, 10, 50, 50))
    pygame.draw.rect(windowSurfaceObj, redColor, (10, 420, 50, 50))
    
    
    pixArr = pygame.PixelArray(windowSurfaceObj)
    for x in range(100, 100, 4):
        for y in range(100, 200, 4):
                pixArr[x][y] = redColor
    del pixArr
    
    windowSurfaceObj.blit(circleSurfaceObj, (mousex, mousey))
    
    msgSurfaceObj = fontObj.render(msg, False, greenColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (10, 65)
    windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
                
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                msg = 'Arrow Key Pressed'
            if event.key == K_a:
                msg = '"a" Key Pressed'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    pygame.display.update()
    fpsClock.tick(60)
