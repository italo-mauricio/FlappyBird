import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

pygame.init()

tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # cria uma tela do tamanho definido

BACKGROUND = pygame.image.load('background-day.png')


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    pygame.display.update()