# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:36:34 2018

@author: Arthur Farsky, Pedro Perri and Renato Tajima
"""

import pygame
import random

#======================= CLASSES ===========================


class Personagem (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 550
        self.vx = 0        

    def update(self):
        self.vx = 0 
        self.vy = 0
        keystate = pygame.key.get_pressed()
        
#### MOVIMENTO DA NAVE ####

#### Nave movendo para a diagonal esquerda alta ####
        if keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT] and not\
        keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
            self.vx = -6
            self.vy = -3.5
#### Nave movendo para a diagonal direita baixa ####
        if keystate[pygame.K_RIGHT] and not keystate[pygame.K_LEFT] and not\
        keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
            self.vx = 6
            self.vy = 3.5
#### Nave movendo para a diagonal direita alta ####
        if keystate[pygame.K_UP] and not keystate[pygame.K_DOWN] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = 6
            self.vy = -3.5
#### Nave movendo para a diagonal esquerda baixa ####
        if keystate[pygame.K_DOWN] and not keystate[pygame.K_UP] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = -6
            self.vy = 3.5
        
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
            
    def Tiro(self, tudo, tiros_group):
        tiro = Tiros('imagens/tiro_azul.gif', self.rect.top - 15, self.rect.centerx + 50)
        tudo.add(tiro)
        tiros_group.add(tiro)
        

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
            
#Referência
#https://github.com/kidscancode/pygame_tutorials/blob/master/shmup/shmup-4.py 
            
#### Obstáculos ####
            
class Satélite(pygame.sprite.Sprite):
    def __init__(self, obstaculos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(obstaculos).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(largura_tela - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > altura_tela + 10 or self.rect.left < -25 or self.rect.right > largura_tela + 20:
            self.rect.x = random.randrange(largura_tela - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
 
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
           
def Novo_Satélite(lista_obstaculos, tudo, mobs):
    S = Satélite(random.choice(lista_obstaculos))
    tudo.add(S)
    mobs.add(S)
    
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
#================ BOTÕES ===============

"BOTÃO VERDE"
x_green = largura_tela/2 - 170
y_green = altura_tela/2 
w_green = 350
h_green = 50
    
"BOTÃO VERMELHO"
x_red = largura_tela/2 - 170
y_red = altura_tela/2 + 200
w_red = 350
h_red = 50
        
'CARACTERÍSTICAS DO BOTÃO AZUL (X, Y, W, H)'
x_blue = largura_tela/2 - 170
y_blue = altura_tela/2 + 100
w_blue = 350
h_blue = 50      

#===================== FUNÇÕES =============================     
    
#### Função que gera a pontuação
def score(score):
    largeText = pygame.font.SysFont("None", 50)
    banana = largeText.render("score: "+str(score),0,(255,255,255))
    tela.blit(banana,(0,0))
    pygame.display.update()
    
#### Função das letras nos botões ####
def mensagem(msg, x, y, tamanho):
    
    def text_objects(texto, fonte):
        pygame.font.get_fonts()
        textSurface = fonte.render(texto, True, white)
        return textSurface, textSurface.get_rect()
    
    smallText = pygame.font.SysFont("rockwellcondensed", tamanho)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x, y)
    tela.blit(textSurf, textRect)

#### Função para sair da tela de jogo ####        
def sair ():
    pygame.quit()
    quit()
    
#### Função loop que faz o jogo rodar ####
def loop ():
    x = 0
    y = 0
    Game = True
    pygame.mixer.music.play(-1)
    
    #=================  CRIANDO GRUPOS  ========================
    
    tudo = pygame.sprite.Group()
    
    personagem_group = pygame.sprite.Group()
    personagem =  Personagem("imagens/personagem.gif")
    personagem_group.add(personagem)
    tudo.add(personagem)
    
    lista_obstaculos = ['imagens/Satélite.png', 'imagens/Satélite2.png',
                       'imagens/Satélite3.png', 'imagens/Satélite4.png', 'imagens/Satélite5.png',
                       'imagens/Satélite6.png']
    
    tiros_group = pygame.sprite.Group()
    
    for i in range(8):
        Novo_Satélite(lista_obstaculos, tudo, mobs)
    
    while Game:
        
        relogio.tick(FPS)
    
        pressed_keys = pygame.key.get_pressed()
#### ESC sai do jogo ####        
        if pressed_keys[pygame.K_ESCAPE]:
            Game = False
            menu()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                pygame.mixer.music.stop()
                Game = False
                
#### SPACE atira ####                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    personagem.Tiro(tudo, tiros_group)
                    pygame.mixer.Sound.play(som_tiro)
                    
#### MOVIMENTO DA TELA ####      
        rel_x = x % fundo.get_rect().width
        rel_y = y % fundo.get_rect().height
        tela.blit(fundo, (rel_x - fundo.get_rect().width, rel_y - fundo.get_rect().height))
        if rel_x < largura_tela and rel_y < altura_tela:
                tela.blit (fundo, (rel_x, 0))
        x -= 5
        y += 5
        
        # Update
        
        all_sprites = pygame.sprite.Group()
         
        all_sprites.update()
        
        # Verifica se o tiro acertou algum Satélite
        tiros = pygame.sprite.groupcollide(mobs, tiros_group, True, True)
        for tiro in tiros:
            Novo_Satélite(lista_obstaculos, tudo, mobs)
            
        # Verifica se o Satélite atingiu o player
        hits = pygame.sprite.spritecollide(personagem, mobs, False)
        if hits:
            Game = False
        
        #####PONTUACAO#####
        score(int(pygame.time.get_ticks()/1000))
        
        tudo.update()
#Desenhar tudo que está no grupo "tudo" na tela ####        
        tudo.draw(tela)
        pygame.display.flip()
       
def back():
    menu()
    
def play():
    loop()

#### REFERÊNCIA PRO MENU ####
#https://pythonprogramming.net/adding-sounds-music-pygame/  --> Menu

#### Função para o menu de instruções ####
def instructions():
    instruction = True
    x = 0
    bckgd = pygame.image.load("imagens/fundo.png").convert()
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        rel_x = x % bckgd.get_rect().width
        tela.blit(bckgd, (rel_x -bckgd.get_rect().width, 0))
        if rel_x < largura_tela:
            tela.blit (bckgd, (rel_x, 0))
        x -= 4
        
        
        mensagem("Instructions", largura_tela/2, altura_tela/3, 130)
        mensagem("Shoot ----> Space Bar", largura_tela/2, altura_tela/2, 50)
        mensagem("Move ----> Arrow Keys", largura_tela/2, altura_tela/2 + 100, 50)
        
        botoes("Play", largura_tela/2 - 175, altura_tela/2 + 150, w_green,\
               h_green, green, bright_green, play)
        botoes("Back", largura_tela/2- 175, altura_tela/2 + 250, w_red,\
               h_red, red, bright_red, back)
        
        pygame.display.update()
        relogio.tick(FPS)

def botoes(msg, x, y, w, h, ic, ac, action = None):
    
    #colocando os botões
    # x: A posição no eixo x da caixa do botão.
    # y: A posição no eixo y da caixa do botão.
    # w: Button width.
    # h: Button height.
    # ic: Inactive color (when a mouse is not hovering).
    # ac: Active color (when a mouse is hovering).
    
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(tela, ic, (x, y, w, h))
        
    mensagem(msg, x + (w/2),  y + (h/2), 40)
    
        
    
def menu():
    x = 0
    start = True
    fnd = pygame.image.load("imagens/fundo.png").convert()
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        rel_x = x % fnd.get_rect().width
        tela.blit(fnd, (rel_x -fnd.get_rect().width, 0))
        if rel_x < largura_tela:
            tela.blit (fnd, (rel_x, 0))
        x -= 4
        
        
        mensagem("Space Run", largura_tela/2, altura_tela/2-200, 120)

        botoes("Start", x_green, y_green, w_green, h_green, green, bright_green, loop)
        botoes("Instructions",x_blue, y_blue, w_blue, h_blue, blue, bright_blue, instructions)
        botoes("Quit", x_red, y_red, w_red, h_red, red, bright_red, sair)

        pygame.display.update()
        relogio.tick(FPS)
        
        
#===================== INÍCIO ======================
        
        
pygame.init()

pygame.mixer.music.load("sons/musica.mp3")
som_tiro=pygame.mixer.Sound("sons/tiro.ogg")

largura_tela = 1000
altura_tela = 700

tela = pygame.display.set_mode((largura_tela, altura_tela), 0, 32)

pygame.display.set_caption('Space Run')

relogio = pygame.time.Clock()
    
fundo = pygame.image.load("imagens/fundo.png").convert()


#=================  CRIANDO GRUPOS  ========================

lista_obstaculos = ['imagens/Satélite.png', 'imagens/Satélite2.png',
                   'imagens/Satélite3.png', 'imagens/Satélite4.png', 'imagens/Satélite5.png',
                   'imagens/Satélite6.png']

tudo = pygame.sprite.Group()

personagem_group = pygame.sprite.Group()
personagem =  Personagem("imagens/personagem.gif")
personagem_group.add(personagem)
tudo.add(personagem)

tiros_group = pygame.sprite.Group()


menu()
loop()
