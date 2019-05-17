# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import random

# Estabelece a pasta que contem as figuras.
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
SPEED = 8
MOVING_NONE = 0
MOVING_LEFT = 1
MOVING_RIGHT = 2
MOVING_UP = 3
MOVING_DOWN = 4
BATTLE = 5

class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        player_img = pygame.image.load(path.join(img_dir, "andar_direita.png"))
        self.image = player_img
        self.image.set_colorkey(WHITE)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (31, 40))
        
        self.mask = pygame.mask.from_threshold(self.image, (0, 0, 0, 255), (255,255,255,10))

        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = W / 2
        self.rect.bottom = H / 2
        
        # Velocidade da nave
        self.speedx = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((W, H))

# Nome do jogo
pygame.display.set_caption("Pokemon")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'mapa.jpeg')).convert()
background_mask_img = pygame.image.load(path.join(img_dir, 'mascara_mapa.png')).convert()
background_mask_mato = pygame.image.load(path.join(img_dir, 'mascara_mato.png')).convert()
background_x = -700
background_y = -600
background_x_prev = background_x
background_y_prev = background_y

background_mask = pygame.mask.from_threshold(background_mask_img, (0, 0, 0), (20,20,20,255))

moving_state = MOVING_NONE

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS) 

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_state = MOVING_LEFT
                elif event.key == pygame.K_RIGHT:
                    moving_state = MOVING_RIGHT
                elif event.key == pygame.K_UP:
                    moving_state = MOVING_UP
                elif event.key == pygame.K_DOWN:
                    moving_state = MOVING_DOWN
            elif event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                moving_state = MOVING_NONE

        background_x_prev = background_x
        background_y_prev = background_y

        if moving_state == MOVING_UP:
            background_y += SPEED
        elif moving_state == MOVING_DOWN:
            background_y -= SPEED
        elif moving_state == MOVING_LEFT:
            background_x += SPEED
        elif moving_state == MOVING_RIGHT:
            background_x -= SPEED

        if background_x < background.get_width() * -1: 
            background_x = background.get_width()
        if background_y < background.get_height() * -1: 
            background_y = background.get_height()

        if background_mask.overlap(player.mask, (player.rect.x - background_x, player.rect.y - background_y)):
            background_x = background_x_prev
            background_y = background_y_prev

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, (background_x, background_y))  # draws our first bg image
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
