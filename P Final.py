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
                    
        
        
#===================== INÍCIO ======================
pygame.init()

tela=pygame.display.set_mode((1000, 700), 0, 32)

pygame.display.set_caption('STARSHIPS')

relogio = pygame.time.Clock()

personagem_group = pygame.sprite.Group()
tudo = pygame.sprite.Group()
    
fundo = pygame.image.load("imagens/fundo.png").convert()

personagem =  Personagem("imagens/personagem.png")
personagem_group.add(personagem)
tudo.add(personagem)


loop()