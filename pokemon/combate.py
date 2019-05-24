import pygame
from os import path
import random

img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
W, H = 800, 447
FPS = 30 # Frames por segundo

QUIT = 2

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
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        
        self.hp = 155

def combate(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
        
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join(img_dir, 'luta.jpg')).convert()
    background = pygame.transform.scale(background,(W,H))
    background_x = 0
    background_y = 0

    blastoise = Blastoise()    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(blastoise)

    inicio = pygame.time.get_ticks()

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
            if pygame.mouse.get_pressed()[0]:
                x = pygame.mouse.get_pos()[0]
                y =  pygame.mouse.get_pos()[1]
                if x > 404 and x < 576 and  y > 352 and y < 385  :
                    ataque = random.randint(0,100)
                    if ataque >= 90:
                        print('ataque crítico')
                        blastoise.hp -= 50
                    elif ataque >=5:
                        blastoise.hp -=20
                    else :
                        print('Errrrou')
                        
                    
                    

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, (background_x, background_y))  # draws our first bg image
        all_sprites.draw(screen)
        
        # Desenha o power bar do blastoise.
        bar = pygame.Surface((blastoise.hp, 9))
        bar_rect = bar.get_rect()
        bar.fill(GREEN)
        screen.blit(bar, (157, 88))
        
        #agora = pygame.time.get_ticks()
        #if (agora - inicio) > 500:
            #inicio = agora
            #blastoise.hp -= 10
            #if blastoise.hp <= 0:
             #   running = False
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    return QUIT


if __name__ == "__main__":
    
    # Inicialização do Pygame.
    pygame.init()
    pygame.mixer.init()
    
    # Tamanho da tela.
    screen = pygame.display.set_mode((W, H))
    
    # Nome do jogo
    pygame.display.set_caption("Pokemon")
    
    try:
        combate(screen)    
    finally:
        pygame.quit()
    
