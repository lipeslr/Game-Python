import pygame
from random import choice
class Snake(pygame.sprite.Sprite):
# =======================================================================================================================================================================
# Código Base 

    def __init__(self):
        super().__init__()
        #imagem e retangulo
        self.image = pygame.image.load('npc/snake/walk/down/0.png')
        #amplia a imagem
        self.image = pygame.transform.scale(self.image, (32, 32))
        #retanugulo da snake
        self.rect = self.image.get_rect(center=((200,400)))
        # contadores
        self.index = 3 # variavel de orientação
        self.index_walk = 0 # variavel de animação
        self.change_index = 0 # contador de movimento aleatorio
        self.life=4# vida
        self.dano=1# dano de colisão com o inimigo
        

# Código Base         
# =======================================================================================================================================================================
# Funções
# =======================================================================================================================================================================    
    
    # função de animação
    def animation(self):

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação sul
        if self.index == 0:  # orientação sul
            self.index_walk += 0.1 # incrementa a variavel de animação
            if self.index_walk >= 4:# verifica se a animação atingiu o seu limite
                self.index_walk = 0# reseta a variavel de animação

            #atualiza a imagem
            self.image = pygame.image.load(
                f'npc/snake/walk/down/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(self.image, (32, 32))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação norte
        elif self.index == 1: # orientação norte
            self.index_walk += 0.1# incrementa a variavel de animação
            if self.index_walk >= 4:# verifica se a animação atingiu o seu limite
                self.index_walk = 0# reseta a variavel de animação

             #atualiza a imagem
            self.image = pygame.image.load(
                f'npc/snake/walk/up/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(self.image, (30, 32))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação esquerda
        elif self.index == 2:# orientação esquerda
            self.index_walk += 0.1# incrementa a variavel de animação
            if self.index_walk >= 4:# verifica se a animação atingiu o seu limite
                self.index_walk = 0# reseta a variavel de animação

             #atualiza a imagem
            self.image = pygame.image.load(
                f'npc/snake/walk/right/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(self.image, (48, 32))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # animação na orientação direita
        elif self.index == 3:  # orientação direita
            self.index_walk += 0.1# incrementa a variavel de animação
            if self.index_walk >= 4:# verifica se a animação atingiu o seu limite
                self.index_walk = 0# reseta a variavel de animação

             #atualiza a imagem
            self.image = pygame.image.load(
                f'npc/snake/walk/left/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(self.image, (48, 32))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # movimentação do inimigos snake
    def moviment(self):

        if self.index == 0:# orientação sul
            self.rect.y += 1# move orientação sul

        elif self.index == 1:# orientação norte
            self.rect.y += -1# move na orientação norte

        elif self.index == 2:# orientação esquerda
            self.rect.x += 1# move na orientação esquerda

        elif self.index == 3:# orientação direita
            self.rect.x += -1# move na orientação direita

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # função para mudar a orientação da snake
    def change_orientation(self):


        #verifica se a snake está no limite do mapa na orientação norte
        if self.rect.y <= 120:
            self.rect.y=120# reposiciona a snake dentro dos limites do mapa
            self.index = 0# muda a orientaçao da snake para o sentido contrario

        #verifica se a snake está no limite do mapa na orientação sul
        elif self.rect.y >= 538:
            self.rect.y=520# reposiciona a snake dentro dos limites do mapa
            self.index = 1# muda a orientaçao da snake para o sentido contrario

        #verifica se a snake está no limite do mapa na orientação esquerda
        elif self.rect.x >= 630:
            self.rect.x=620# reposiciona a snake dentro dos limites do mapa
            self.index = 2# muda a orientaçao da snake para o sentido contrario

        #verifica se a snake está no limite do mapa na orientação direita
        elif self.rect.x <= 123:
            self.rect.x=130# reposiciona a snake dentro dos limites do mapa
            self.index = 3# muda a orientaçao da snake para o sentido contrario

        #verifica se a snake está no limite do mapa
        if self.change_index == 100:# verifica se o contador de movimento aleatorio chegou ao limite
            self.index = choice([0, 1, 2, 3])# escolhe uma orientação aleatoriamente
            self.change_index = 0# reseta o contador de movimento aleatorio


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        else:# se não chegou ao limite
            self.change_index += 1# incrementa o contador de movimento aleatorio


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # função para eliminar a snake
    def destroy(self):
        # se a vida da slug chegou a 0
        if self.life<=0:
            self.kill()
            self.rect = self.image.get_rect(center=(-200, -200))        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def update(self):
        self.animation()# função de animação
        self.moviment()# movimentação do inimigos snake
        self.change_orientation()# função para mudar a orientação da snake
        self.destroy()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------