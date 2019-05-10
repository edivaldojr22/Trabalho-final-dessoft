# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
W, H = 800, 447
win = pygame.display.set_mode((W,H))
FPS = 30 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
speed = 8

def redrawWindow():
    win.blit(background, (background_x, background_y))  # draws our first bg image
    pygame.display.update()  # updates the screen


class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        

        player_img = pygame.image.load(path.join(img_dir, "personagem_costas.png"))
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (80, 80))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
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
background = pygame.image.load(path.join(img_dir, 'teste_mapa_2.png')).convert()
background_x = 0
background_y = 0

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

        if background_x < background.get_width() * -1: 
            background_x = background.get_width()
        if background_y < background.get_height() * -1: 
            background_y = background.get_height()

        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    background_x -= speed
                if event.key == pygame.K_RIGHT:
                    background_x += speed
                if event.key == pygame.K_UP:
                    background_y -= speed
                if event.key == pygame.K_DOWN:
                    background_y += speed
    
        # A cada loop, redesenha o fundo e os sprites
        redrawWindow()
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
