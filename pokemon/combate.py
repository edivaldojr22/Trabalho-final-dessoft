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
        
        self.maxhp = 394
        self.hp = self.maxhp

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
        
        self.maxhp = 296
        self.hp = self.maxhp

        
        

class pokemon_do_player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        rayquaza_img = pygame.image.load(path.join(img_dir, "149.png"))
        self.image = rayquaza_img
        self.image.set_colorkey(GREEN)
        self.image = pygame.transform.scale(self.image,(120,140))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = 206
        self.rect.bottom =  340
        
        self.maxhp = 461
        self.hp = self.maxhp
        

def escreve(fonte,msg, pos, screen, cor):
    text_surface = fonte.render(msg, True, cor)
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = pos
    screen.blit(text_surface, text_rect)
    

def combate(screen):
    #font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
        
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join(img_dir, 'luta_basica.jpg')).convert()
    background = pygame.transform.scale(background,(W,H))
    background_x = 0
    background_y = 0

    escolha = random.randrange(2)
    if escolha == 0:
        enemy = Blastoise()
    elif escolha == 1:
        enemy = pokemon_do_player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(enemy)
    rayquaza = pokemon_do_player() 
    all_sprites.add(rayquaza)

    #inicio = pygame.time.get_ticks()

    # Loop principal.
    running = True
    MUSICA = True
    turno = True
    time =0
    
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
                    defesa = 0
                    
                    if x > 404 and x < 576 and  y > 352 and y < 385  :
                        ataque = random.randint(0,100)
                        if ataque >= 90:
                            print('ataque crítico')
                            enemy.hp -= 50
                        elif ataque >= 5:
                            enemy.hp -=20
                        else :
                            print('Errrrou')
                        turno= False
                    elif x > 606 and x < 780 and  y > 352 and y < 385:
                        defesa = random.randint(0,100)
                        print(defesa) 
                        turno = False
                    elif x > 606 and x < 780 and y > 404 and y < 436:
                        fuga = random.randint(0,100)
                        if fuga > 5:
                            print('fuga bem sucedida!')
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
                            pygame.mixer.music.play()
                            running = False
                        else:
                            print('se ferrou arregão!')
                            turno = False
                        
           

        if not turno:
             now = pygame.time.get_ticks()
             diff= now - time
             if diff> 1000:
                print('Vez do adversário!')
                ataque_do_adversario = random.randint(0,100)
                if ataque_do_adversario >= 90:
                    print('ataque crítico')
                    dano = 50 - defesa
                    if dano < 0:
                        dano = 0
                    rayquaza.hp -= dano
                elif ataque_do_adversario >=5:
                    dano = 20 - defesa
                    if dano < 0:
                        dano = 0
                    rayquaza.hp -= dano
                    print('acertou')
                else :
                    print('Errrrou')
                turno = True
                    
        
        

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, (background_x, background_y))  # draws our first bg image
        all_sprites.draw(screen)
        
        # Desenha o power bar do enemy.
        hp= enemy.hp
        maxhp = enemy.maxhp
        if enemy.hp < 0:
            hp = 0
            running = False
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
            pygame.mixer.music.play()

        bar = pygame.Surface((154*hp/maxhp, 9))
        bar.fill(GREEN)
        screen.blit(bar, (157, 88))
        
        hp2 = rayquaza.hp
        maxhp2 = rayquaza.maxhp
        if rayquaza.hp <0:
            hp2 = 0
            running = False
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
            pygame.mixer.music.play()
        barra = pygame.Surface((152*hp2/maxhp2, 9))
        barra.fill(GREEN)
        screen.blit(barra, (630, 272))
        
        if enemy.hp <= 0 or rayquaza.hp <= 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path.join(music_dir, "route 209.mp3"))
            pygame.mixer.music.play()
>>>>>>> 4d08af28f026b6628bf8e477af70eed9de5b36f4
            running = False
        
        escreve(fonte_pequena,'Blastoise',(  0,H - 367), screen, BLACK)
        escreve(fonte_pequena,'Dragonite',(  475,H - 186), screen, BLACK)
        escreve(FONTE,'50',(292, H - 367),screen, BLACK)
        escreve(FONTE,'50',(760, H - 184),screen, BLACK)
        escreve(FONTE,'{0}/{1}'.format(hp2,maxhp2),(650, H - 137), screen , BLACK)

        if turno:
            escreve(FONTE,"O que Dragonite" , (50, H - 50), screen, BLACK) 
            escreve(FONTE,"fará?", (50, H - 20), screen, BLACK)
        elif not turno:
            escreve(FONTE,"Vez do adversário!" , (30, H - 50), screen, BLACK) 
            
                 
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    return 42


if __name__ == "__main__":
    
     #Inicialização do Pygame.
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
    
