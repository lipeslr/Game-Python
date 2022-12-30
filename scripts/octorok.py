import pygame
from random import choice
from pygame.locals import *

gun_group = pygame.sprite.Group()

class Octorok(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #imagem e retangulo
        self.image = pygame.image.load('npc/octorok_blue/walk/down/0.png')
        #amplia a imagem
        self.image = pygame.transform.scale(self.image, (32,30))
        self.rect = self.image.get_rect(center=((200,400)))
        
        
        #contadores
        self.index_attack=0
        self.index_walk = 0 # variavel de orientação
        self.index = 3 # variavel de animação
        self.change_index = 0 # contador de movimento aleatorio
        self.life = 4# vida
        self.dano = 1# dano
        self.cor = choice(['red', 'blue', 'red', 'blue'])

        
        
# Funções
# =======================================================================================================================================================================                
    
    # função de animação 
    def animation(self):
        if self.cor=="troll":
            self.index_attack +=0.5
        else:
            self.index_attack+=0.1
            
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação sul         
        if self.index == 0: # orientação sul
                self.index_walk += 0.1 # incrementa a variavel de animação
                if self.index_walk >= 3: # verifica se a animação atingiu o seu limite
                    self.index_walk = 0 # reseta a variavel de animação
                
                #atualiza a imagem
                self.image = pygame.image.load(
                    f'npc/octorok_{self.cor}/walk/down/{int(self.index_walk)}.png')
                self.image = pygame.transform.scale(self.image, (32, 30))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação norte              
        elif self.index == 1: # orientação norte
                self.index_walk += 0.1 # incrementa a variavel de animação
                if self.index_walk >= 3: # verifica se a animação atingiu o seu limite
                    self.index_walk = 0 # reseta a variavel de animação
                
                #atualiza a imagem
                self.image = pygame.image.load(
                    f'npc/octorok_{self.cor}/walk/up/{int(self.index_walk)}.png')
                self.image = pygame.transform.scale(self.image, (32, 32))
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação esquerda                        
        elif self.index == 2: # orientação esquerda
                self.index_walk += 0.1 # incrementa a variavel de animação
                if self.index_walk >= 3: # verifica se a animação atingiu o seu limite
                    self.index_walk = 0 # reseta a variavel de animação
                #atualiza a imagem
                self.image = pygame.image.load(
                f'npc/octorok_{self.cor}/walk/left/{int(self.index_walk)}.png')
                self.image = pygame.transform.scale(self.image, (38, 30))                
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação direita                
        elif self.index == 3: # orientação direita
                self.index_walk += 0.1# incrementa a variavel de animação
                if self.index_walk >= 3: # verifica se a animação atingiu o seu limite
                    self.index_walk = 0 # reseta a variavel de animação
                
                #atualiza a imagem
                self.image = pygame.image.load(
                    f'npc/octorok_{self.cor}/walk/right/{int(self.index_walk)}.png')
                self.image = pygame.transform.scale(self.image, (38, 30))
        
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # movimentação do inimigos octorok
    def moviment(self):
        
    
        if self.index == 0:# orientação sul
            self.rect.y += 1# move orientação sul
            
        elif self.index == 1:# orientação norte
            self.rect.y += -1# move na orientação norte
        
        elif self.index == 2:# orientação esquerda
            self.rect.x += -1# move na orientação esquerda
        
        elif self.index == 3:# orientação direita
            self.rect.x += 1# move na orientação direita
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # função para mudar a orientação da octorok
    def change_orientation(self):

        #verifica se a octorok está no limite do mapa na orientação norte 
        if self.rect.y <= 120:
            self.rect.y = 120# reposiciona a octorok dentro dos limites do mapa
            self.index = 0# muda a orientaçao da octorok para o sentido contrario
        
        #verifica se a octorok está no limite do mapa na orientação
        elif self.rect.y >= 508:
            self.rect.y = 497# reposiciona a octorok dentro dos limites do mapa              
            self.index = 1# muda a orientaçao da octorok para o sentido contrario
        
        #verifica se a octorok está no limite do mapa na orientação esquerda        
        elif self.rect.x >= 580:
            self.rect.x = 570# reposiciona a octorok dentro dos limites do mapa
            self.index = 2# muda a orientaçao da octorok para o sentido contrario
        
        #verifica se a octorok está no limite do mapa na orientação direita    
        elif self.rect.x <= 123:
            self.rect.x = 133# reposiciona a octorok dentro dos limites do mapa
            self.index = 3# muda a orientaçao da octorok para o sentido contrario
        
        #verifica se a octorok está no limite do mapa
        if self.change_index == 100:# verifica se o contador de movimento aleatorio chegou ao limite
            self.index = (choice([0, 1, 2, 3]))# escolhe uma orientação aleatoriamente
            self.change_index = 0# reseta o contador de movimento aleatorio
          
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        else:# se não chegou ao limite
            self.change_index += 1# incrementa o contador de movimento aleatorio
        
    # função para eliminar a octorok
    def destroy(self):
        # se a vida da slug chegou a 0
        if self.life<=0:
            self.kill()
            self.rect = self.image.get_rect(center=(-200, -200))   
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
    def update(self):
        self.animation()# função de animação
        self.moviment()# movimentação do inimigos octorok
        self.change_orientation()# função para mudar a orientação da octorok
        self.destroy()# função para eliminar a octorok