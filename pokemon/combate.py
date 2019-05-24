import pygame
from os import path
import random

img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
W, H = 800, 447
FPS = 30 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Blastoise(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "9.png"))
        self.image = blastoise_img_img
        self.image.set_colorkey(WHITE)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (90, 80))
        
        

        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = W - 10
        self.rect.bottom = H - 15
        
        
        
        
        



# Tamanho da tela.
screen = pygame.display.set_mode((W, H))



def combate(screen):
    clock = pygame.time.Clock()
    
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join(img_dir, 'luta.jpg')).convert()
    background_x = -700
    background_y = -600
   
    
    
    blastoise = Blastoise()
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(blastoise)
    
    
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS) 

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            
            
            



     
    return QUIT

    
    