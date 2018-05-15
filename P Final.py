# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:36:34 2018

@author: Pedro Perri
"""

import pygame
from os import path
from random import randrange
import random


#======================= CLASSES ===========================
class Personagem (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 150
        self.vx = 0
        
    def move (self):
        self.vx = 0 
        self.vy = 0
        keystate = pygame.key.get_pressed()
        
        #### MOVIMENTO DA NAVE ####
        # x^2 + x^2 = 25 ---- x^2 =12.5 ---- x = 12.5 ** (1/2)
        if keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT] and not\
        keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
            self.vx = -(12.5 ** (1/2))
            self.vy = -(12.5 ** (1/2))
        if keystate[pygame.K_RIGHT] and not keystate[pygame.K_LEFT] and not\
        keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
            self.vx = (12.5 ** (1/2))
            self.vy = (12.5 ** (1/2))
        if keystate[pygame.K_UP] and not keystate[pygame.K_DOWN] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = (12.5 ** (1/2))
            self.vy = -(12.5 ** (1/2))
        if keystate[pygame.K_DOWN] and not keystate[pygame.K_UP] and not\
        keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.vx = -(12.5 ** (1/2))
            self.vy = (12.5 ** (1/2))
        
        #### OUTROS MOVIMENTOS ####
        if keystate[pygame.K_LEFT] and keystate[pygame.K_DOWN]:
            self.vy = -5
        if keystate[pygame.K_LEFT] and keystate[pygame.K_UP]:
            self.vy = -5
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_DOWN]:
            self.vx = 5
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_UP]:
            self.vx = 5
        self.rect.x += self.vx
        self.rect.y += self.vy
        
#===================== Cores ============================= 
       
black = (0,0,0)
white = (255,255,255)
gray = (128, 128, 128)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
        

#===================== FUNÇÕES =============================
        
def sair ():
    pygame.QUIT()
    quit()
        
def loop ():

    Game = True

    tela.blit(fundo, (0,0))
    
    while Game:
        relogio.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()       
                
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_ESCAPE]:
            Game = False
            
        personagem.move()
        
        tudo.draw(tela)
        pygame.display.flip()
        
       
#https://pythonprogramming.net/adding-sounds-music-pygame/  --> Menu
        
def text_objects(texto, fonte):
    
    textSurface = fonte.render(texto, True, white)
    return textSurface, textSurface.get_rect()

def botoes(msg,x,y,w,h,ic,ac,action=None):
    
    #colocando os botões
    # x: The x location of the top left coordinate of the button box.
    # y: The y location of the top left coordinate of the button box.
    # w: Button width.
    # h: Button height.
    # ic: Inactive color (when a mouse is not hovering).
    # ac: Active color (when a mouse is hovering).
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(tela, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(tela, ic,(x,y,w,h))
        
    smallText = pygame.font.SysFont("ARBONNIE",35)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    tela.blit(textSurf, textRect)
        
def start_menu():

    start = True

    while start:
        
        #(Características do o botão verde (x,y,z,h))
        x_green = largura_tela/2 - 170
        y_green = altura_tela/2 + 100
        w_green = 350
        h_green = 50
    
        #(Características do  botão vermelho(x,y,z,h))
        x_red = largura_tela/2 - 170
        y_red = altura_tela/2 + 200
        w_red = 350
        h_red = 50
        
        fundo = pygame.image.load("imagens/fundo.png").convert()
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            tela.blit(fundo, (0,0))
            largeText = pygame.font.SysFont("Goudystout",70)
            TextSurf, TextRect = text_objects("Space Run", largeText)
            TextRect.center = ((largura_tela/2),(altura_tela/3))
            tela.blit(TextSurf, TextRect)

            botoes("Start",x_green,y_green,w_green,h_green,green,bright_green,loop)
            botoes("Sair",x_red,y_red,w_red,h_red,red,bright_red, sair)

            pygame.display.update()
            relogio.tick(15)
        
        
#===================== INÍCIO ======================
pygame.init()

largura_tela = 1000
altura_tela = 700

tela=pygame.display.set_mode((largura_tela, altura_tela), 0, 32)

pygame.display.set_caption('STARSHIPS')

relogio = pygame.time.Clock()

personagem_group = pygame.sprite.Group()
tudo = pygame.sprite.Group()
    
fundo = pygame.image.load("imagens/fundo.png").convert()

personagem =  Personagem("imagens/personagem.png")
personagem_group.add(personagem)
tudo.add(personagem)

start_menu()
loop()