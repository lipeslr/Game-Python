import pygame
from random import choice

class Bomb(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('npc/bomb/walk/right/0.png')
        self.image = pygame.transform.scale(self.image, (26,34))
        self.rect = self.image.get_rect(center=((400,400)))
        
        #contadores
        self.index_walk = 0 # variavel de orientação
        self.index = 0# variavel de animação
        self.change_index = 0 # contador de movimento aleatorio
        self.life = 4# vida
        self.auto_destroy = 160 #contador de auto destruição
        self.status = 'walk' #variavel para mudar direitorio das sprites
        self.dano=1
        self.status_image = 26 #variavel para mudar o a altura da imagem quando o self.life < 4
        self.status_image_2 = 34 #variavel para mudar o a altura da imagem quando o self.life < 4
# Funções
# =======================================================================================================================================================================    
    
    # função de animação   
    def animation(self):
        #verifica se a vida fica menor que 4 para mudar o sel.status
        if self.life < 4:
            self.status = 'destroy_walk'
            self.auto_destroy -= 1
            self.status_image = 32
            self.status_image_2 = 48
            
        #verifica se a vida é maior que 0  
        if self.life > 0:   
            # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # animação na orientação sul 
            if self.index == 0: # orientação sul
                    self.index_walk += 0.1 # incrementa a variavel de animação
                    if self.index_walk >= 2: # verifica se a animação atingiu o seu limite
                        self.index_walk = 0 # reseta a variavel de animação
                    
                    #atualiza a imagem
                    self.image = pygame.image.load(
                    f'npc/bomb/{self.status}/right/{int(self.index_walk)}.png')
                    self.image = pygame.transform.scale(self.image, (self.status_image, self.status_image_2))

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # animação na orientação norte               
            elif self.index == 1: # orientação norte
                    self.index_walk += 0.1 # incrementa a variavel de animação
                    if self.index_walk >= 2: # verifica se a animação atingiu o seu limite
                        self.index_walk = 0 # reseta a variavel de animação
                    
                    #atualiza a imagem
                    self.image = pygame.image.load(
                    f'npc/bomb/{self.status}/left/{int(self.index_walk)}.png')
                    self.image = pygame.transform.scale(self.image, (self.status_image, self.status_image_2))

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # animação na orientação esquerda                
            elif self.index == 2: # orientação esquerda
                    self.index_walk += 0.1 # incrementa a variavel de animação
                    if self.index_walk >= 2: # verifica se a animação atingiu o seu limite
                        self.index_walk = 0 # reseta a variavel de animação
                    
                    #atualiza a imagem
                    self.image = pygame.image.load(
                    f'npc/bomb/{self.status}/right/{int(self.index_walk)}.png')
                    self.image = pygame.transform.scale(self.image, (self.status_image, self.status_image_2))

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # animação na orientação direita      
            elif self.index == 3: # orientação direita
                    self.index_walk += 0.1 # incrementa a variavel de animação
                    if self.index_walk >= 2: # verifica se a animação atingiu o seu limite
                        self.index_walk = 0 # reseta a variavel de animação
                    
                    #atualiza a imagem
                    self.image = pygame.image.load(
                    f'npc/bomb/{self.status}/left/{int(self.index_walk)}.png')
                    self.image = pygame.transform.scale(self.image, (self.status_image, self.status_image_2))
                    

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # animação na orientação nordeste          
            elif self.index == 4:  # orientação nordeste
                    self.index_walk += 0.1 # incrementa a variavel de animação
                    if self.index_walk >= 2: # verifica se a animação atingiu o seu limite
                        self.index_walk = 0 # reseta a variavel de animação
                    
                    #atualiza a imagem
                    self.image = pygame.image.load(
                    f'npc/bomb/{self.status}/right/{int(self.index_walk)}.png')
                    self.image = pygame.transform.scale(self.image, (self.status_image, self.status_image_2))
                    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            # animação na orientação sudeste       
            elif self.index == 5: # animação na orientação sudeste
                    self.index_walk += 0.1 # incrementa a variavel de animação
                    if self.index_walk >= 2: # verifica se a animação atingiu o seu limite
                        self.index_walk = 0 # reseta a variavel de animação
                    
                    #atualiza a imagem
                    self.image = pygame.image.load(
                    f'npc/bomb/{self.status}/left/{int(self.index_walk)}.png')
                    self.image = pygame.transform.scale(self.image, (self.status_image, self.status_image_2))
        
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # movimentação do inimigo bomb
    def moviment(self):
        if self.life == 4:
            if self.index == 0: # orientação sudeste
                self.rect.y += 1 # move orientação sudeste
                self.rect.x += 1 # move orientação sudeste
            
            elif self.index == 1: # orientação noroeste
                self.rect.y += -1# move orientação noroeste
                self.rect.x += -1# move orientação noroeste
            
            elif self.index == 2:# orientação Leste
                self.rect.x += 1# move orientação Leste
                
            elif self.index == 3: # orientação Oeste
                self.rect.x += -1# move orientação Oeste
            
            elif self.index == 4:# orientação Nordeste
                self.rect.x += 1# move orientação Nordeste
                self.rect.y += -1# move orientação Nordeste
                
            elif self.index == 5:# orientação Sudoeste
                self.rect.x += -1# move orientação Sudoeste
                self.rect.y += 1# move orientação Sudoeste
        
        #aumento de velocidade do bomb após levar dano
        elif self.life < 4:
            if self.index == 0: # orientação sudeste
                self.rect.y += 2 # move orientação sudeste
                self.rect.x += 2 # move orientação sudeste
            
            elif self.index == 1: # orientação noroeste
                self.rect.y += -2# move orientação noroeste
                self.rect.x += -2# move orientação noroeste
            
            elif self.index == 2:# orientação Leste
                self.rect.x += 2# move orientação Leste
                
            elif self.index == 3: # orientação Oeste
                self.rect.x += -2# move orientação Oeste
            
            elif self.index == 4:# orientação Nordeste
                self.rect.x += 2# move orientação Nordeste
                self.rect.y += -2# move orientação Nordeste
                
            elif self.index == 5:# orientação Sudoeste
                self.rect.x += -2# move orientação Sudoeste
                self.rect.y += 2# move orientação Sudoeste
        
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # função para mudar a orientação do bomb       
    def change_orientation(self):
        
                #verifica se o bomb está no limite do mapa na orientação norte    
            if self.rect.y <= 120:
                self.rect.y = 120# reposiciona do bomb dentro dos limites do mapa
                self.index = 0# muda a orientaçao da bomb para o sentido contrario

            #verifica se a snake está no limite do mapa na orientação sul 
            elif self.rect.y >= 520:# reposiciona o bomb dentro dos limites do mapa
                self.rect.y = 510# reposiciona a bomb dentro dos limites do mapa
                self.index = 1# muda a orientaçao do bomb para o sentido contrario
                
             #verifica se a bomb está no limite do mapa na orientação esquerda
            elif self.rect.x >= 630:
                self.rect.x = 620# reposiciona a bomb dentro dos limites do mapa
                self.index = 3# muda a orientaçao da bomb para o sentido contrario

            #verifica se a bomb está no limite do mapa na orientação direita
            elif self.rect.x <= 123:
                self.rect.x = 133# reposiciona a bomb dentro dos limites do mapa
                self.index = 2# muda a orientaçao da bomb para o sentido contrario
        
            #verifica se a bomb está no limite do mapa
            if self.change_index == 100:# verifica se o contador de movimento aleatorio chegou ao limite
                self.index = (choice([0, 1, 2, 3, 4, 5]))# escolhe uma orientação aleatoriamente
                self.change_index = 0# reseta o contador de movimento aleatorio

            else:
                self.change_index += 1

    # função para eliminar  bomb
    def destroy(self):
        # se a vida da bomb chegou a 0
        if self.life<=0:
            self.kill()# elimina o bomb
            self.rect = self.image.get_rect(center=(-200, -200))  
    #função de atualização
    def update(self):
        self.animation()# função de animação
        self.moviment()# movimentação do inimigos bomb
        self.change_orientation()# função para mudar a orientação da bomb
        self.destroy()# função para eliminar a bomb