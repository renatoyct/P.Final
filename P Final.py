# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:36:34 2018

@author: Pedro Perri
"""

import pygame
from pygame.locals import *

#inpirado em https://www.youtube.com/watch?v=ccpVi7DRNF8
screenDimension=(1000,700)
screen=pygame.display.set_mode(screenDimension,0,32)

player=pygame.image.load("imagens/personagem.jpeg")
keys=[False,False,False,False]
playerpos=[200,200]
velocidade=10
out=True
relogio = pygame.time.Clock()
x=0
y=0
while out:
    fundo = pygame.image.load("imagens/fundo.png").convert()
    
    tempo = relogio.tick(100)
    
    
    
    screen.blit(player,playerpos)
    pygame.display.flip()
    screen.fill(0)
    ponto1=[10,510]
    ponto2=[1250,-630]
    ponto3=[1500,-490]
    ponto4=[250,650]
    relx=x%fundo.get_rect().width
    #pygame.draw.polygon(screen,(0,255,0),(ponto1,ponto2,ponto3,ponto4,ponto1))

    screen.blit(fundo, (relx-fundo.get_rect().width, y))
    if relx<screenDimension[0]:
        screen.blit(fundo, (relx,0))
    #pygame.draw.line(screen,(170,150,0),(ponto1[0]-1,ponto1[1]+20),(ponto4[0],ponto4[1]+20),42)
    #pygame.draw.line(screen,(100,80,0),(ponto4[0],ponto4[1]+20),(ponto3[0]-1,ponto3[1]+20),42)
    
    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.locals.K_w:
                keys[0]=True
                keys[3]=True
            if event.key==pygame.locals.K_s:
                keys[1]=True
                keys[2]=True
            if event.key==pygame.locals.K_a:
                keys[2]=True
                keys[0]=True
            if event.key==pygame.locals.K_d:
                keys[3]=True
                keys[1]=True
        if event.type==pygame.locals.QUIT:
                out=False
        if event.type ==pygame.KEYUP:
            if event.key==pygame.locals.K_w:
                keys[0]=False
                keys[3]=False
            if event.key==pygame.locals.K_s:
                keys[1]=False
                keys[2]=False
            if event.key==pygame.locals.K_a:
                keys[2]=False
                keys[0]=False
            if event.key==pygame.locals.K_d:
                keys[3]=False
                keys[1]=False
      
    if keys[0]:
        playerpos[1]-=velocidade
    if keys[1]:
        playerpos[1]+=velocidade
    if keys[2]:
        playerpos[0]-=velocidade
    if keys[3]:
        playerpos[0]+=velocidade
    x-=5
    y+=0
    
pygame.display.quit()