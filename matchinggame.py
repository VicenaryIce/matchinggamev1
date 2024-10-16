import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Hello World!')
font = pygame.font.SysFont('Sans',50)

def renderimages():
    images =['candycrush.jpg','sorry.png','temple_runner.png','subway_surfers.png']
    names = ['Candy crush','Sorry','Temple Runner','Subway Surfers']
    
    random.shuffle(names)
    cordinate = 25
    ncord = 25
    for i in images:
        image = pygame.image.load(i)
        screen.blit(image,(50,cordinate))
        cordinate = cordinate+100
    for i in names:
         name = font.render(i,True,'white')
         screen.blit(name,(400,ncord))
         print(name)
         ncord  = ncord+100




renderimages()

while True:
   
   for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            selectedimage = pygame.draw.circle(screen,'red',position,radius= 10)
        
   pygame.display.update()