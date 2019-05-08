# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
W, H = 800, 447
win = pygame.display.set_mode((W,H))
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def redrawWindow():
    win.blit(background, (background_x, 0))  # draws our first bg image
    pygame.display.update()  # updates the screen

class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "personagem_costas.png"))
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 100))
        
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
background = pygame.image.load(path.join(img_dir, 'teste_mapa_1.jpg')).convert()
background_x = 0
background_x2 = background.get_width()

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
        background_x -= 1.4

        if background_x < background.get_width() * -1:  # If our bg is at the -width then reset its position
            background_x = background.get_width()

        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
    
        # A cada loop, redesenha o fundo e os sprites
        redrawWindow()
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
