import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800


class Bird(pygame.sprite.Sprite): # Definindo a classe do pássaro
    
    def __init__(self): # init padrão da OO
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('bluebird-midflap.png').convert_aplha()  # convert_alpha vai ignorar o pixels que se sobressaem na imagem
        
    
    
    
pygame.init()

tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # cria uma tela do tamanho definido

BACKGROUND = pygame.image.load('background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))  # criando background da imagem a partir da tupla com tamanho definido


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    tela.blit(BACKGROUND, (0, 0))
    pygame.display.update()