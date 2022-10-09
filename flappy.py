import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
SPEED = 10

class Bird(pygame.sprite.Sprite): # Definindo a classe do pássaro
    
    def __init__(self): # init padrão da OO
        pygame.sprite.Sprite.__init__(self)
        
        self.images = [pygame.image.load('bluebird-upflap.png').convert_alpha(),
                       pygame.image.load('bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('bluebird-downflap.png').convert_alpha(),
                       ]
        
        self.current_image = 0
        
        self.image = pygame.image.load('bluebird-upflap.png').convert_alpha()  # convert_alpha vai ignorar o pixels que se sobressaem na imagem

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2                                         # colocando o pássaro no meio da tela
        self.rect[1] = SCREEN_HEIGHT / 2
        
         
    def update(self):
        
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images [ self.current_image ]
        
    
    
    
pygame.init()

tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # cria uma tela do tamanho definido

BACKGROUND = pygame.image.load('background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))  # criando background da imagem a partir da tupla com tamanho definido

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    tela.blit(BACKGROUND, (0, 0))
    
    bird_group.update()
    
    bird_group.draw(tela)
    
    
    pygame.display.update()