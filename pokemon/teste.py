# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import random
from combate import combate, pokemon_do_player

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')
music_dir = path.join(path.dirname(__file__), 'music')


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
pygame.mixer.music.play()

# Dados gerais do jogo.
W, H = 800, 447
FPS = 60 # Frames por segundo

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
INIT = 42
QUIT = 1337
COMBATE = 5

class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.images = {
            MOVING_LEFT: pygame.image.load(path.join(img_dir, "andar_esquerda_1.png")),
            MOVING_RIGHT: pygame.image.load(path.join(img_dir, "andar_direita_1.png")),
            MOVING_UP: pygame.image.load(path.join(img_dir, "andar_cima_1.png")),
            MOVING_DOWN: pygame.image.load(path.join(img_dir, "andar_baixo_1.png")),
            MOVING_NONE: pygame.image.load(path.join(img_dir, "andar_direita_1.png"))
        }

        for k in self.images:
            self.images[k] = pygame.transform.scale(self.images[k], (31, 40))

        self.state = MOVING_NONE
        self.change_state(MOVING_RIGHT)

    def change_state(self, state):
        if state != self.state:
            self.state = state

            self.image = self.images[self.state]
            self.images[MOVING_NONE] = self.image
            self.image.set_colorkey(WHITE)

            self.mask = pygame.mask.from_threshold(self.image, (0, 0, 0, 255), (255,255,255,10))

            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            
            # Centraliza embaixo da tela.
            self.rect.centerx = W / 2
            self.rect.bottom = H / 2
                   

# Variável para o ajuste de velocidade
def jogo(screen):
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = pygame.image.load(path.join(img_dir, 'mapa.jpeg')).convert()
    background_mask_img = pygame.image.load(path.join(img_dir, 'mascara_final.png')).convert()
    background_mask_mato = pygame.image.load(path.join(img_dir, 'mascara_mato.png')).convert()
<<<<<<< HEAD
=======

>>>>>>> c3005484f6cac943445aee6d31669aa46e5df1bd
    #background_mask_entrada_caverna_1 = pygame.image.load(path.join(img_dir, 'caverna_entradas_mascara.png')).convert()

    background_mask_entrada_caverna_1 = pygame.image.load(path.join(img_dir, 'caverna_entradas_mascara.jpeg')).convert()

    
    background_x = -700
    background_y = -600
    background_x_prev = background_x
    background_y_prev = background_y

    background_mask = pygame.mask.from_threshold(background_mask_img, (0, 0, 0), (20,20,20,255))
    matinho = pygame.mask.from_threshold(background_mask_mato, (0, 0, 0), (20,20,20,255))

    #caverna_entrada_1 = pygame.mask.from_threshold(background_mask_entrada_caverna, (0, 0, 0), (20,20,20,255))
<<<<<<< HEAD
=======

>>>>>>> c3005484f6cac943445aee6d31669aa46e5df1bd
    caverna_entrada_1 = pygame.mask.from_threshold(background_mask_entrada_caverna_1, (0, 0, 0), (20,20,20,255))


    moving_state = MOVING_NONE

    player = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
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

        player.change_state(moving_state)

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

        if matinho.overlap(player.mask, (player.rect.x - background_x, player.rect.y - background_y)) and moving_state != MOVING_NONE:
            chance = random.randint(0, 100)
            if chance < 2:
                pygame.mixer.music.stop()
                combate(screen,hp_player)
                moving_state = MOVING_NONE 
        if caverna_entrada_1(player.mask, (player.rect.x - background_x, player.rect.y - background_y)):
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.load(path.join(music_dir, "musica_caverna.mp3"))
            pygame.mixer.music.play()
            #caverna(screen)
                

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, (background_x, background_y))  # draws our first bg image
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return(QUIT)
        

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((W, H))

# Nome do jogo
pygame.display.set_caption("Pokephyton")


rayquaza = pokemon_do_player()
hp_player = rayquaza.hp
# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = jogo(screen)
        elif state == COMBATE:
            state = combate(screen,hp_player)
            print(state)
        else:
            state = QUIT
finally:
    pygame.quit()
