import pygame
from random import randrange
import random
import time

#======================= CLASSES ===========================

#Classe do Personagem
class Personagem (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 550
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = largura_tela / 2
        self.rect.bottom = altura_tela - 10
        self.vx = 0        

    def update(self):
        self.vx = 0 
        self.vy = 0
        keystate = pygame.key.get_pressed()
        
#### MOVIMENTO DA NAVE ####

#### Nave movendo para a diagonal esquerda alta ####
        if keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT] and not\
        keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
            self.vx = -3
            self.vy = -2
#### Nave movendo para a diagonal direita baixa ####
        if keystate[pygame.K_RIGHT] and not keystate[pygame.K_LEFT] and not\
        keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
            self.vx = 3
            self.vy = 2
#### Nave movendo para a diagonal direita alta ####
        if keystate[pygame.K_UP] and not keystate[pygame.K_DOWN] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = 3
            self.vy = -2
            #### Nave movendo para a diagonal esquerda baixa ####
        if keystate[pygame.K_DOWN] and not keystate[pygame.K_UP] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = -3
            self.vy = 2
        
#### OUTROS MOVIMENTOS ####
        
#### Nave movendo para a esquerda ####
        if keystate[pygame.K_LEFT] and keystate[pygame.K_DOWN]:
            self.vx = -5
#### Nave movendo para cima ####
        if keystate[pygame.K_LEFT] and keystate[pygame.K_UP]:
            self.vy = -5
#### Nave movendo para baixo ####
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_DOWN]:
            self.vy = 5
#### Nave movendo para a direita ####
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_UP]:
            self.vx = 5
        self.rect.x += self.vx
        self.rect.y += self.vy        
       
#### LIMITES DA NAVE NA TELA ####
#### Lado direito da tela ####        
        if self.rect.right > largura_tela -5:
            self.rect.right = largura_tela - 5
#### Lado esquerdo da tela ####
        if self.rect.left < 5:
            self.rect.left = 5
#### Parte de baixo da tela ####
        if self.rect.bottom > altura_tela - 5:
            self.rect.bottom = altura_tela - 5
#### Parte de cima da tela ####
        if self.rect.top < 5:
            self.rect.top = 5

#### Função que faz a nave atirar ####            
    def Tiro(self, tudo, tiros_group):
        tiro = Tiros('imagens/tiro_1.gif', self.rect.top - 15, self.rect.centerx + 50)
        tudo.add(tiro)
        tiros_group.add(tiro)
        
#Classe dos tiros
class Tiros(pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem, pos_y, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.top = pos_y
        self.rect.centerx = pos_x
        self.vy = -7
        self.vx = 10
        
    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
#### Tiro morre quando sai da tela (kill) #### 
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.right < 0:
            self.kill()
            
#### Obstáculos ####
            
class Satélite(pygame.sprite.Sprite):
    def __init__(self, obstaculos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(obstaculos).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(1000,1700)
        self.rect.y = randrange(-1000, 0)
        self.radius = int(self.rect.width * .85 / 2)
        self.speedy = randrange(2,4)
        self.speedx = -randrange(2,4)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > altura_tela + 1000 or self.rect.left < -75 \
        or self.rect.right > largura_tela + 700:
            self.rect.x = randrange(1000,1700)
            self.rect.y = randrange(-1000, 0)
            self.speedy = randrange(2,4)
           
def Novo_Satélite(lista_obstaculos, tudo, mobs):
    S = Satélite(random.choice(lista_obstaculos))
    tudo.add(S)
    mobs.add(S)
   
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
#===================== CORES ============================= 

#### Combinação de numeros caracteriza as cores RGB ####
black = (0,0,0)
white = (255,255,255)
gray = (128, 128, 128)

red = (200,0,0)
green = (0,200,0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
purple = (200, 0, 200)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0, 0, 255)
bright_yellow = (255, 255, 0)
bright_purple = (255, 0, 255)


#=============== CONFIGURAÇÕES DA TELA ===========
largura_tela = 1000
altura_tela = 700
FPS = 100     
    
#===================== FUNÇÕES ============================= 

#Cronometro para dicionar no score final --> quanto mais tempo o player vive, 
#mais pontos ele faz
def cronometro(valor):
    Seconds = int(valor)
    return Seconds

#Escreve na tela
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
def mensagem(msg, x, y, tamanho):
    
    def text_objects(texto, fonte):
        pygame.font.get_fonts()
        textSurface = fonte.render(texto, True, white)

        return textSurface, textSurface.get_rect()
    
    smallText = pygame.font.SysFont("rockwellcondensed", tamanho)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x, y)
    tela.blit(textSurf, textRect)
   
#Loop do jogo
def loop():
    x = 0
    Start = True
    Menu = True
    Instruction = False
    Game = False
    Game_over = False
    Pause = False
    comeco = time.time()
    tempo_pause = 0
    fnd = pygame.image.load("imagens/fundo.png").convert()
    fundo_x = 0
    fundo_y = tela.get_height() - fnd.get_height()
    pygame.mixer.music.play(-1)
    tudo = pygame.sprite.Group()    
    personagem_group = pygame.sprite.Group()
    personagem =  Personagem("imagens/personagem.gif")
    personagem_group.add(personagem)
    mobs = pygame.sprite.Group()
    tudo.add(mobs)
    tudo.add(personagem)
    
    lista_obstaculos = ['imagens/Satélite.png', 'imagens/Satélite2.png',
                       'imagens/Satélite3.png', 'imagens/Satélite4.png', 
                       'imagens/Satélite5.png', 'imagens/Satélite6.png']    
    
    while Start:
        
        for i in range(15):
            Novo_Satélite(lista_obstaculos, tudo, mobs)
        
        while Menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
            rel_x = x % fnd.get_rect().width
            tela.blit(fnd, (rel_x -fnd.get_rect().width, 0))
            if rel_x < largura_tela:
                tela.blit (fnd, (rel_x, 0))
            x -= 4
                        
            mensagem("SPACE RUN", largura_tela/2, altura_tela/2-200, 120 )
    
            mensagem("Press enter to play", largura_tela/2, altura_tela/2, 50 )
            mensagem("Press ' I ' for instructions",largura_tela/2, altura_tela/2 + 100, 50)
            mensagem("Press 'ESC' to quit", largura_tela/2, altura_tela/2 + 200, 50)

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_RETURN]:
                Menu= False
                Game = True
                score_hit = 0
            if pressed_keys[pygame.K_i]:
                Menu = False
                Instruction = True
            if pressed_keys[pygame.K_ESCAPE]:
                Menu = False
                Start = False
                
            pygame.display.update()
            relogio.tick(FPS)        
        
        while Instruction:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            rel_x = x % fnd.get_rect().width
            tela.blit(fnd, (rel_x -fnd.get_rect().width, 0))
            if rel_x < largura_tela:
                tela.blit (fnd, (rel_x, 0))
            x -= 4               
                
            mensagem("INSTRUCTIONS", largura_tela/2, altura_tela/4, 120)
            mensagem("Shoot ----> Space Bar", largura_tela/2, altura_tela/3+50, 50)
            mensagem("Move ----> Arrow Keys", largura_tela/2, altura_tela/2 , 50)
            mensagem("Pause ----> P key", largura_tela/2, altura_tela/ 2+ 70, 50)
            mensagem("Press 'B' to menu", largura_tela/2, altura_tela/2 + 200, 50)
            
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_b]:
                Instruction = False
                tudo = pygame.sprite.Group()    
                personagem_group = pygame.sprite.Group()
                personagem =  Personagem("imagens/personagem.gif")
                personagem_group.add(personagem)
                tudo.add(personagem)
                mobs = pygame.sprite.Group()
                tudo.add(mobs)
                comeco = time.time()
                tempo_pause = 0
                score_hit = 0
                Menu = True
                
            pygame.display.update()
            relogio.tick(FPS)
        
        while Game:
                
            tempo_jogado = time.time()
            
            pressed_keys = pygame.key.get_pressed()
    #### ESC sai do jogo ####        
            if pressed_keys[pygame.K_ESCAPE]:
                Game = False
                Start = False
            
            if pressed_keys[pygame.K_p]:
                comeco_pause = time.time()
                Pause = True
                while Pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return
                        if event.type == pygame.KEYDOWN:
                            final_pause = time.time()
                            tempo_pause = tempo_pause + final_pause - comeco_pause
                            Pause = False
                    
                    
                    mensagem("PAUSED", largura_tela/2, altura_tela/2-200, 120)
                    mensagem("Press enter to continue", largura_tela/2, altura_tela/2, 50)
                    mensagem("Press 'M' to menu", largura_tela/2, altura_tela/2 + 100, 50)
                    mensagem("Press 'ESC' to quit", largura_tela/2, altura_tela/2 + 200, 50)
                    
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[pygame.K_RETURN]:                
                        Pause = False
                        Game = True
                        score_final = 0
                        tempo_pause = 0
                    if pressed_keys[pygame.K_m]:
                        Pause = False
                        Game= False
                        tudo = pygame.sprite.Group()    
                        personagem_group = pygame.sprite.Group()
                        personagem =  Personagem("imagens/personagem.gif")
                        personagem_group.add(personagem)
                        tudo.add(personagem)
                        mobs = pygame.sprite.Group()
                        tudo.add(mobs)
                        comeco = time.time()
                        tempo_pause = 0
                        score_hit = 0
                        Menu = True
                    if pressed_keys[pygame.K_ESCAPE]:
                        Pause = False
                        Game = False
                        Start = False
                        
                    
                    pygame.display.update()
                    relogio.tick(FPS)   
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:            
                    pygame.mixer.music.stop()
                    Game = False
                    Start = False
                    
    #### SPACE atira ####                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        personagem.Tiro(tudo, tiros_group)
                        pygame.mixer.Sound.play(som_tiro)
                        
    #### MOVIMENTO DA TELA ####      
            
            fundo_x -= 0.9
            fundo_y += 0.9
            if fundo_y > 0:
                fundo_x = 0
                fundo_y = tela.get_height() - fnd.get_height()
                
            # Verifica se o tiro acertou algum Satélite
            tiros = pygame.sprite.groupcollide(mobs, tiros_group, True, True)
            
            for tiro in tiros:
                Novo_Satélite(lista_obstaculos, tudo, mobs)
                expl = Explosion(tiro.rect.center, 'lg')
                tudo.add(expl)
                score_hit += 100 - tiro.radius
            
            # Verifica se o Satélite atingiu o player
            hits = pygame.sprite.spritecollide(personagem, mobs, False,pygame.sprite.collide_circle)
            for hit in hits:
                expl = Explosion(hit.rect.center, 'sm')
                tudo.add(expl)
                Novo_Satélite(lista_obstaculos, tudo, mobs)
                Game = False
                Game_over = True
                x = 0
                
             ###Pontuação###
            segundos_passsados = cronometro(tempo_jogado - comeco - tempo_pause)
            score_tempo = segundos_passsados*1
            score_final = score_tempo + score_hit
            
            tela.fill(black)
            tela.blit(fnd, (fundo_x, fundo_y))
            mensagem('{0}'.format(score_final), largura_tela/2, altura_tela/2-300, 50)
            
            tudo.update()
    #Desenhar tudo que está no grupo "tudo" na tela ####        
            tudo.draw(tela)
            pygame.display.flip()#      
            
        while Game_over:
            tudo = pygame.sprite.Group()    
            personagem_group = pygame.sprite.Group()
            personagem =  Personagem("imagens/personagem.gif")
            personagem_group.add(personagem)
            tudo.add(personagem)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
            rel_x = x % fnd.get_rect().width
            tela.blit(fnd, (rel_x -fnd.get_rect().width, 0))
            if rel_x < largura_tela:
                tela.blit (fnd, (rel_x, 0))
            x -= 4
            
            mensagem("GAME OVER", largura_tela/2, altura_tela/2-200, 120)
            
            mensagem("Press 'R' to restart", largura_tela/2, altura_tela/2, 50)
            mensagem("Presse 'M' to menu", largura_tela/2, altura_tela/2 + 100, 50)
            mensagem("Press 'ESC' to quit", largura_tela/2, altura_tela/2 + 200, 50)
                
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[pygame.K_r]:
                Game_over = False
                tudo = pygame.sprite.Group()    
                personagem_group = pygame.sprite.Group()
                personagem =  Personagem("imagens/personagem.gif")
                personagem_group.add(personagem)
                tudo.add(personagem)
                mobs = pygame.sprite.Group()
                tudo.add(mobs)
                Game = True
                comeco = time.time()
                tempo_pause = 0
                score_hit = 0
                
            if pressed_keys[pygame.K_m]:
                Game_over = False
                tudo = pygame.sprite.Group()    
                personagem_group = pygame.sprite.Group()
                personagem =  Personagem("imagens/personagem.gif")
                personagem_group.add(personagem)
                tudo.add(personagem)
                mobs = pygame.sprite.Group()
                tudo.add(mobs)
                comeco = time.time()
                tempo_pause = 0
                score_hit = 0
                Menu = True
            if pressed_keys[pygame.K_ESCAPE]:
                Game_over = False
                Start = False
                
            tudo.draw(tela)
            pygame.display.update()
            relogio.tick(FPS)      
                
        
                
        tela.fill(black)
        
        tela.blit(fnd, (0,0))
       
            
        tudo.update()
#Desenhar tudo que está no grupo "tudo" na tela ####        
        tudo.draw(tela)
        pygame.display.flip()   
#===================== INÍCIO ======================
        
pygame.init()

pygame.mixer.music.load("sons/musica.mp3")
som_tiro=pygame.mixer.Sound("sons/tiro.ogg")

largura_tela = 1000
altura_tela = 700

tela = pygame.display.set_mode((largura_tela, altura_tela), 0, 32)

pygame.display.set_caption('Space Run')

relogio = pygame.time.Clock()

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in range(8):
    filename = 'imagens/Explosao{}.gif'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    
#=================  CRIANDO GRUPOS  ========================
tudo = pygame.sprite.Group()

tiros_group = pygame.sprite.Group()

loop()

pygame.quit()
#=================  Referências ========================

#https://pythonprogramming.net/adding-sounds-music-pygame/
#https://github.com/kidscancode/pygame_tutorials/blob/master/shmup/shmup-14.py