# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:36:34 2018

@author: Pedro Perri
"""


import pygame

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
            self.vx = 4
            self.vy = 3.5
#### Nave movendo para a diagonal direita alta ####
        if keystate[pygame.K_UP] and not keystate[pygame.K_DOWN] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = 6
            self.vy = -3.5
#### Nave movendo para a diagonal esquerda baixa ####
        if keystate[pygame.K_DOWN] and not keystate[pygame.K_UP] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = -4
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
        tiro = Tiros('imagens/tiro_azul.png', self.rect.top - 15, self.rect.centerx + 50)
        tudo.add(tiro)
        tiros_group.add(tiro)
        

class Tiros(pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem, pos_y, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.top = pos_y
        self.rect.centerx = pos_x
        self.vy = -3.5
        self.vx = 6
        
    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
#### Tiro morre quando sai da tela (kill) #### 
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.right < 0:
            self.kill()
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
#================ BOTÕES ===============

"BOTÃO VERDE"
x_green = largura_tela/2 - 170
y_green = altura_tela/2 
w_green = 350
h_green = 50
    
"BOTÃO VERMELHO"
x_red = largura_tela/2 - 170
y_red = altura_tela/2 + 100
w_red = 350
h_red = 50
        
#CARACTERÍSTICAS DO BOTÃO AZUL (X, Y, W, H)
#x_blue = largura_tela/2 - 170
#y_blue = altura_tela/2 + 200
#w_blue = 350
#h_blue = 50      

#===================== FUNÇÕES =============================     
    

#### Função para sair da tela de jogo ####        
def sair ():
    pygame.quit()
    quit()
    
#### Função loop que faz o jogo rodar ####
def loop ():
    x = 0
    y = 0
    Game = True

    while Game:
        
        relogio.tick(100)
    
        pressed_keys = pygame.key.get_pressed()
#### ESC sai do jogo ####        
        if pressed_keys[pygame.K_ESCAPE]:
            Game = False
            sair()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                Game = False
#### SPACE atira ####                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    personagem.Tiro(tudo, tiros_group)

#### MOVIMENTO DA TELA ####      
        rel_x = x % fundo.get_rect().width
        rel_y = y % fundo.get_rect().height
        tela.blit(fundo, (rel_x - fundo.get_rect().width, rel_y - fundo.get_rect().height))
        if rel_x < largura_tela or rel_y < altura_tela:
            tela.blit (fundo, (rel_x, rel_y))
        x -= 4
        y += 4
        
        if rel_x == 300 and rel_y == 200:
            rel_x = 0
            rel_y = 0
        
        tudo.update()
#Desenhar tudo que está no grupo "tudo" na tela ####        
        tudo.draw(tela)
        pygame.display.flip()
       

#### REFERÊNCIA PRO MENU ####
#https://pythonprogramming.net/adding-sounds-music-pygame/  --> Menu

#### Função das letras nos botões ####
def text_objects(texto, fonte):
    pygame.font.get_fonts()
    textSurface = fonte.render(texto, True, white)
    return textSurface, textSurface.get_rect()


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
        
        
    smallText = pygame.font.SysFont("rockwellcondensed", 45)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    tela.blit(textSurf, textRect)
        
    
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
        
        
        largeText = pygame.font.SysFont("rockwellcondensed", 120)
        TextSurf, TextRect = text_objects("Space Run", largeText)
        TextRect.center = ((largura_tela / 2), (altura_tela / 3))
        tela.blit(TextSurf, TextRect)

        botoes("Start", x_green, y_green, w_green, h_green, green, bright_green, loop)
        botoes("Quit", x_red, y_red, w_red, h_red, red, bright_red, sair)

        pygame.display.update()
        relogio.tick(15)
        
        
#===================== INÍCIO ======================
        
        
pygame.init()

largura_tela = 1000
altura_tela = 700

tela = pygame.display.set_mode((largura_tela, altura_tela), 0, 32)

pygame.display.set_caption('STARSHIPS')

relogio = pygame.time.Clock()
    
fundo = pygame.image.load("imagens/fundo.png").convert()


#=================  CRIANDO GRUPOS  ========================


tudo = pygame.sprite.Group()

personagem_group = pygame.sprite.Group()
personagem =  Personagem("imagens/personagem.png")
personagem_group.add(personagem)
tudo.add(personagem)

tiros_group = pygame.sprite.Group()


menu()
loop()
