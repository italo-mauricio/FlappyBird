from turtle import Screen
import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100



class Bird(pygame.sprite.Sprite): # Definindo a classe do pássaro
    
    def __init__(self): # init padrão da OO
        
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('bluebird-upflap.png').convert_alpha(),
                       pygame.image.load('bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('bluebird-downflap.png').convert_alpha(),
                       ]
        
        self.speed = SPEED
        self.current_image = 0
        self.image = pygame.image.load('bluebird-upflap.png').convert_alpha()  # convert_alpha vai ignorar o pixels que se sobressaem na imagem
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2                                         # colocando o pássaro no meio da tela
        self.rect[1] = SCREEN_HEIGHT / 2
        
    def update(self):
        
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images [ self.current_image ]
        self.speed += GRAVITY
        # -----------------------------
        self.rect[1] += self.speed  # faz o pássaro cair
        # -----------------------------
    
    def bump(self):
        self.speed = -SPEED
    
    
    
class Ground(pygame.sprite.Sprite):
    def __init__(self, xposition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('base.png')
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xposition
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT
    
    def update(self):
        self.rect[0] -= GAME_SPEED
    
def off_screen(sprite):
    return sprite.rect[0] < - (sprite.rect[2])
    
    
    
    

    
pygame.init()

tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # cria uma tela do tamanho definido

BACKGROUND = pygame.image.load('background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))  # criando background da imagem a partir da tupla com tamanho definido

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)
ground_group = pygame.sprite.Group()

for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:   # usa o espaço para fazer ele subir
                bird.bump()
                
                
    tela.blit(BACKGROUND, (0, 0))
    
    if off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        
        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground)
    
    bird_group.update()
    ground_group.update()
    bird_group.draw(tela)
    ground_group.draw(tela)
    pygame.display.update()