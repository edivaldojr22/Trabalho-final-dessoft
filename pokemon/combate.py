import pygame
from os import path
import random

music_dir = path.join(path.dirname(__file__), 'music')
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

img_dir = path.join(path.dirname(__file__), 'img')
fnt_dir = path.join(path.dirname(__file__), 'fonte')

# Dados gerais do jogo.
W, H = 800, 447
FPS = 60 # Frames por segundo

QUIT = 2

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

FONTE = pygame.font.Font(path.join(fnt_dir, "fonte.ttf"), 18)
FONTE.set_bold(True)
fonte_pequena = pygame.font.Font(path.join(fnt_dir, "fonte.ttf"), 12)
fonte_pequena.set_bold(True)

class Blastoise(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "9.png"))
        self.image = blastoise_img
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 196
        self.hp = self.maxhp
        
        self.ataque = 30

class Charizard(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "6.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 187
        self.hp = self.maxhp
        
        self.ataque = 33



class Mewtwo(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "150.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 360
        self.hp = self.maxhp
        self.ataque = 40
        
class Mew(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "151.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 330
        self.hp = self.maxhp 
        
        self.ataque = 36
class Bulbasaur(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "1.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 97
        self.hp = self.maxhp 
        
        self.ataque = 22
class Venosaur(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "150.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 201
        self.hp = self.maxhp  
        
        self.ataque = 30
class Charmander(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "4.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 92
        self.hp = self.maxhp
        self.ataque = 24
        
class Squirtle(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "7.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 87
        self.hp = self.maxhp
        self.ataque = 22
        
class Ratata(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "19.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 24
        self.hp = self.maxhp
        self.ataque = 14
        
        
class Pikachu(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "25.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 75
        self.hp = self.maxhp  
        self.ataque = 19
class Zubat(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "41.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 51
        self.hp = self.maxhp
        self.ataque = 15
        
class Diglet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "50.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 36
        self.hp = self.maxhp
        self.ataque = 15

class Psyduck(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "54.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 52
        self.hp = self.maxhp
        self.ataque = 17

class Machamp(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "68.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 92
        self.hp = self.maxhp
        self.ataque = 32

class Golem(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "76.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 124
        self.hp = self.maxhp
        self.ataque = 31

class Gengar(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "94.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 145
        self.hp = self.maxhp
        self.ataque = 32


class Onix(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "95.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 162
        self.hp = self.maxhp
        self.ataque = 33

class Gyarados(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "130.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 167
        self.hp = self.maxhp
        self.ataque = 33

class Lapras(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "131.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 202
        self.hp = self.maxhp
        self.ataque = 35

class Snorlax(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "143.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 252
        self.hp = self.maxhp
        self.ataque = 35

class Articuno(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "144.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 302
        self.hp = self.maxhp
        self.ataque = 38

class Zapdos(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "145.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 306
        self.hp = self.maxhp
        self.ataque = 38

class Moltres(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "146.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 301
        self.hp = self.maxhp
        self.ataque = 38

class Dragonite(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        blastoise_img = pygame.image.load(path.join(img_dir, "batata.png"))
        self.image = blastoise_img
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 598
        self.rect.bottom =  220
        
        self.maxhp = 276
        self.hp = self.maxhp
        self.ataque = 37

        
class pokemon_do_player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        rayquaza_img = pygame.image.load(path.join(img_dir, "149.png"))
        self.image = rayquaza_img
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 206
        self.rect.bottom =  340
        
        self.maxhp = 276
        self.hp = self.maxhp
        self.xp = 0
        self.maxxp = 200
        self.level = 50
        self.maxlevel = 100
        self.ataque = 30

def escreve(fonte,msg, pos, screen, cor):
    text_surface = fonte.render(msg, True, cor)
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = pos
    screen.blit(text_surface, text_rect)
    
def pokemon_inimigo(escolha,screen):
    
    if escolha == 0:
        escreve(fonte_pequena,'Blastoise',(  0,H - 367), screen, BLACK)
    elif escolha == 1:
        escreve(fonte_pequena,'Charizard',(  0,H - 367), screen, BLACK)
    elif escolha == 2:
        escreve(fonte_pequena,'Mewtwo',(  0,H - 367), screen, BLACK)    
    elif escolha == 3:
        escreve(fonte_pequena,'Mew',(  0,H - 367), screen, BLACK)
    elif escolha == 4:
        escreve(fonte_pequena,'Charmander',(  0,H - 367), screen, BLACK)
    elif escolha == 5:
        escreve(fonte_pequena,'Bulbasaur',(  0,H - 367), screen, BLACK)    
    elif escolha == 6:
        escreve(fonte_pequena,'Venusaur',(  0,H - 367), screen, BLACK) 
    elif escolha == 7:
        escreve(fonte_pequena,'Squirtle',(  0,H - 367), screen, BLACK)    
    elif escolha == 8:
        escreve(fonte_pequena,'Ratata',(  0,H - 367), screen, BLACK)     
    elif escolha == 9:
        escreve(fonte_pequena,'Pikachu',(  0,H - 367), screen, BLACK)
    elif escolha == 10:
        escreve(fonte_pequena,'Zubat',(  0,H - 367), screen, BLACK)     
    elif escolha == 11:
        escreve(fonte_pequena,'Diglet',(  0,H - 367), screen, BLACK)     
    elif escolha == 12:
        escreve(fonte_pequena,'Psyduck',(  0,H - 367), screen, BLACK)     
    elif escolha == 13:
        escreve(fonte_pequena,'Machamp',(  0,H - 367), screen, BLACK)     
    elif escolha == 14:
        escreve(fonte_pequena,'Golem',(  0,H - 367), screen, BLACK)    
    elif escolha == 15:
        escreve(fonte_pequena,'Gengar',(  0,H - 367), screen, BLACK)    
    elif escolha == 16:
        escreve(fonte_pequena,'Onix',(  0,H - 367), screen, BLACK)    
    elif escolha == 17:
        escreve(fonte_pequena,'Gyarados',(  0,H - 367), screen, BLACK)    
    elif escolha == 18:
        escreve(fonte_pequena,'Lapras',(  0,H - 367), screen, BLACK)
    elif escolha == 19:
        escreve(fonte_pequena,'Snorlax',(  0,H - 367), screen, BLACK)    
    elif escolha == 20:
        escreve(fonte_pequena,'Articuno',(  0,H - 367), screen, BLACK)    
    elif escolha == 21:
        escreve(fonte_pequena,'Zapdos',(  0,H - 367), screen, BLACK)    
    elif escolha == 22:
        escreve(fonte_pequena,'Moltres',(  0,H - 367), screen, BLACK)    
    elif escolha == 23:
        escreve(fonte_pequena,'Dragonite',(  0,H - 367), screen, BLACK)  
        
def desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2,level):
    screen.blit(background, (background_x, background_y))
    all_sprites.draw(screen)
    screen.blit(bar, (157, 88))
    screen.blit(barra, (630, 272))
    screen.blit(barraxp, (482, 315))
    pokemon_inimigo(escolha,screen)
    escreve(fonte_pequena,'Dragonite',(  475,H - 186), screen, BLACK)
    escreve(FONTE,'{0}'.format(level),(760, H - 184),screen, BLACK)
    escreve(FONTE,'50',(292, H - 367),screen, BLACK)
    escreve(FONTE,'{0}/{1}'.format(hp2,maxhp2),(650, H - 137), screen , BLACK)


        
            
rayquaza = pokemon_do_player()

hp_atual = rayquaza.hp
xp_atual = rayquaza.xp

def combate(screen,hp_atual, xp_atual):
    #font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
        
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join(img_dir, 'luta_basica.jpg')).convert()
    background = pygame.transform.scale(background,(W,H))
    background_x = 0
    background_y = 0

    escolha = random.randrange(24)
    if escolha == 0:
        enemy = Blastoise()
    elif escolha == 1:
        enemy = Charizard()
    elif escolha == 2:
        enemy = Mewtwo()
    elif escolha == 3:
        enemy = Mew()    
    elif escolha == 4:
        enemy = Charmander()    
    elif escolha == 5:
        enemy = Bulbasaur()    
    elif escolha == 6:
        enemy = Venosaur()   
    elif escolha == 7:
        enemy = Squirtle()    
    elif escolha == 8:
        enemy = Ratata()
    elif escolha == 9:
        enemy = Pikachu()    
    elif escolha == 10:
        enemy = Zubat()
    elif escolha == 11:
        enemy = Diglet()    
    elif escolha == 12:
        enemy = Psyduck()
    elif escolha == 13:
        enemy = Machamp()
    elif escolha == 14:
        enemy = Golem()    
    elif escolha == 15:
        enemy = Gengar()    
    elif escolha == 16:
        enemy = Onix()    
    elif escolha == 17:
        enemy = Gyarados()
    elif escolha == 18:
        enemy = Lapras()    
    elif escolha == 19:
        enemy =Snorlax()
    elif escolha == 20:
        enemy = Articuno()    
    elif escolha == 21:
        enemy = Zapdos() 
    elif escolha == 22:
        enemy = Moltres()    
    elif escolha == 23:
        enemy = Dragonite()
        
        
        
        
        
    all_sprites = pygame.sprite.Group()
    all_sprites.add(enemy)
    rayquaza = pokemon_do_player() 
    all_sprites.add(rayquaza)

    #inicio = pygame.time.get_ticks()

    # Loop principal.
    running = True
    MUSICA = True
    turno = True
    
    
    
    ataque = 0
    defesa = 0
    fuga = 0
    ataque_do_adversario = 0
    now = pygame.time.get_ticks()
    while running:
        if MUSICA:
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.load(path.join(music_dir, "musica_luta.mp3"))
            pygame.mixer.music.play()
            MUSICA = False
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
                if turno:
                    time = pygame.time.get_ticks()
                    ataque = 0
                    defesa = 0
                    fuga = 0
                    
                    if x > 606 and x < 780 and y > 404 and y < 436:
                        now = pygame.time.get_ticks()
                        diff = now - time
                        fuga = random.randint(1,101)
                        
                        if  fuga > 0 and fuga <=6:
                                turno = False
                        elif fuga > 6 :
                                
                                turno = False
                    elif x > 404 and x < 576 and  y > 352 and y < 385  :
                        ataque = random.randint(1,101)
                        
                        if ataque >= 90:
                            enemy.hp -= 22 + rayquaza.ataque
                        elif ataque >= 5:
                            enemy.hp -=rayquaza.ataque
                        elif ataque > 0 :
                            enemy.hp -= 0
                          
                        turno= False
                    elif x > 606 and x < 780 and  y > 352 and y < 385:
                        defesa = 100
                        turno = False
           

        if not turno:
             now = pygame.time.get_ticks()
             diff= now - time
             
             if diff> 1000:
                 
                 if fuga > 6:
                     
                     pygame.mixer.music.stop()
                     pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
                     pygame.mixer.music.play()
                     running = False
             
             if diff> 3000 and diff < 3010 :
                 ataque_do_adversario = random.randint(1,100)
             if diff> 3700:
                 if ataque_do_adversario >= 90:
                    dano = 22 + enemy.ataque - defesa
                    if dano < 0:
                        dano = 0
                    hp_atual -= dano
                   
                 elif ataque_do_adversario >=5:
                     dano = enemy.ataque - defesa
                     if dano < 0:
                         dano = 0
                     hp_atual -= dano
                     
                    
                 elif ataque_do_adversario > 0:
                     dano = 0
                     hp_atual -= dano
                 
                 if hp_atual <= 0 and diff > 5500:
                     
                     running = False
                 
                 elif hp_atual > 0:
                     turno = True
                
                
           
            
                    
        
        
        
        

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, (background_x, background_y))  # draws our first bg image
        all_sprites.draw(screen)
        
        # Desenha o power bar do enemy.
        hp= enemy.hp
        maxhp = enemy.maxhp
        
        
        if enemy.hp <= 0:
            hp = 0
            now = pygame.time.get_ticks()
            
            if rayquaza.level < rayquaza.maxlevel and diff  < 15:
                xp_ganho = random.randint(300, 452)
                rayquaza.xp += xp_ganho
                xp_atual = rayquaza.xp
                if xp_atual >= rayquaza.maxxp:
                    rayquaza.level += 1
                    rayquaza.maxhp += 200
                    rayquaza.hp += 8
                    rayquaza.ataque += 5
                    rayquaza.xp = 0
                    xp_atual -= rayquaza.maxxp 
            elif rayquaza.level == rayquaza.maxlevel:
                xp_ganho = 0
                xp_atual = 0    
                
            if diff > 1900:
                running = False 
        

        
        
        
        hp2 = hp_atual
        maxhp2 = rayquaza.maxhp
        
        if hp_atual <= 0:
            hp2 = 0
                
        if hp_atual <= 0 or enemy.hp <= 0: 
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
            pygame.mixer.music.play()

        bar = pygame.Surface((154*hp/maxhp, 9))
        if hp > maxhp/2:
            bar.fill(GREEN)
        elif hp > maxhp / 9:
            bar.fill(YELLOW)
        else:
            bar.fill(RED)
        screen.blit(bar, (157, 88))
        
            
        barra = pygame.Surface((152*hp2/maxhp2, 9))
        if hp2 > maxhp2/2:
            barra.fill(GREEN)
        elif hp2 > maxhp2 / 9:
            barra.fill(YELLOW)
        else:
            barra.fill(RED)
        screen.blit(barra, (630, 272))
        
        
        barraxp =  pygame.Surface((300*xp_atual/rayquaza.maxxp,4))
        barraxp.fill(BLUE)
        screen.blit(barraxp, (482, 315))

        level = rayquaza.level
        
        escreve(fonte_pequena,'Dragonite',(  475,H - 186), screen, BLACK)
        escreve(FONTE,'{0}'.format(level),(760, H - 184),screen, BLACK)
        escreve(FONTE,'50',(292, H - 367),screen, BLACK)
        escreve(FONTE,'{0}/{1}'.format(hp2,maxhp2),(650, H - 137), screen , BLACK)
        
        
        
        pokemon_inimigo(escolha,screen)
        
        
        
                 
        if turno  :
            
            now = pygame.time.get_ticks()
            desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
            escreve(FONTE,"O que Dragonite" , (50, H - 50), screen, BLACK) 
            escreve(FONTE,"fará?", (50, H - 20), screen, BLACK)
              
            
        elif not turno:
            if hp <=0 and diff >300:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"Venceu! Ganhou" , (28, H - 50), screen, BLACK)
                escreve(FONTE,"{0} de xp!".format(xp_ganho) , (28, H - 30), screen, BLACK) 
            elif ataque >= 90 and defesa == 0 and fuga == 0 and diff > 500:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"Ataque crítico!" , (50, H - 50), screen, BLACK)
            elif ataque >= 5  and defesa == 0 and fuga == 0 and diff > 500:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"Acertou!" , (50, H - 50), screen, BLACK)
            elif ataque < 5 and ataque > 0 and defesa == 0 and fuga == 0 and diff > 500:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"Errou!" , (50, H - 50), screen, BLACK)
            elif defesa > 0 and ataque == 0 and fuga ==0 and diff > 500:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"Seu pokemon" , (50, H - 50), screen, BLACK)
                escreve(FONTE,"defendeu!" , (50, H - 20), screen, BLACK)    
            elif fuga > 6 and defesa == 0 and ataque ==0 and diff >500:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"Fuga bem sucedida!" , (29, H - 50), screen, BLACK)
            elif fuga <= 6 and fuga > 0  and defesa == 0 and ataque ==0 and diff > 500:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"A fuga falhou!" , (30, H - 50), screen, BLACK)
            
            
                
            
            
            if diff > 2000:
                desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                escreve(FONTE,"Vez do adversário!" , (30, H - 50), screen, BLACK)   
                
                if ataque_do_adversario >= 90 and defesa == 0 and diff > 3000:
                    desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                    escreve(FONTE,"Ataque crítico!" , (30, H - 50), screen, BLACK)
                elif defesa > 0 and ataque == 0 and fuga ==0 and diff > 3000:
                    desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                    escreve(FONTE,"Seu pokemon" , (50, H - 50), screen, BLACK)
                    escreve(FONTE,"defendeu!" , (50, H - 20), screen, BLACK)   
                elif ataque_do_adversario >= 5 and defesa ==0 and diff > 3000:
                    desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2,level)
                    escreve(FONTE,"Acertou!" , (50, H - 50), screen, BLACK)              
                elif ataque_do_adversario > 0 and defesa ==0 and diff > 3000:
                    desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                    escreve(FONTE,"Errou!" , (50, H - 50), screen, BLACK)
                if hp2 <=0 and diff > 3800:
                    desenha_tudo(screen,background, background_x, background_y,all_sprites,bar,barra,barraxp,escolha,hp2,maxhp2, level)
                    escreve(FONTE,"Perdeu feio!" , (29, H - 50), screen, BLACK)     
                    
                    

                        
      
            
       
        
        
        # Depois de desenhar tudo, inverte o dispay.
        pygame.display.flip()
        
   
    return 42, hp_atual,xp_atual



if __name__ == "__main__":
    
     #Inicialização do Pygame.
    pygame.init()
    pygame.mixer.init()
    
    # Tamanho da tela.
    screen = pygame.display.set_mode((W, H))
    
    # Nome do jogo
    pygame.display.set_caption("Pokemon")
    
    try:
        combate(screen,hp_atual,xp_atual)    
    finally:
        pygame.quit()
    
