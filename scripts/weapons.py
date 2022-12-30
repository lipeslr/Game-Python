import pygame
from scripts.player import Player

#adagas do jogador
class Adaga(pygame.sprite.Sprite):

    # =======================================================================================================================================================================
    # Código base
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'objects/sword/0.png').convert_alpha()  # imagem da adaga
        self.image = pygame.transform.scale2x(
            self.image).convert_alpha()  # aumenta a adaga
        self.rect = self.image.get_rect(
            center=(-200, -200))  # retangulo da adaga
        self.index = 0  # orientação que a adaga foi lançada
        self.speed = 15  # velocidade de disparo da adaga
        self.dano = 2  # dano da adaga
        self.player = Player()

# Código base
# =======================================================================================================================================================================
# Funções
# =======================================================================================================================================================================

    # Função de movimento

    def move(self):

        # verifica a orientação de disparo da adaga e move ela de acordo com ela
        if self.index == 0:  # direção sul
            self.rect[1] += self.speed  # incrementa o vetor da adaga
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.index == 1:  # direção norte
            self.rect[1] -= self.speed  # incrementa o vetor da adaga

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.index == 2:  # direção esquerda
            self.rect[0] -= self.speed  # incrementa o vetor da adaga

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.index == 3:  # direção direita
            self.rect[0] += self.speed  # incrementa o vetor da adaga

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # atualiza a imagem da adaga de acordo com sua orientação
        self.image = pygame.transform.scale2x(pygame.image.load(
            f'objects/sword/{self.index}.png')).convert_alpha()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # função de remoção da adaga
    def destroy(self):
        # se a adaga ultrapassar os limites do mapa ela é exclui
        if self.rect.y >= 900 or self.rect.y <= -100:  # orientação sul e norte
            self.kill()  # exclui a adaga

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.rect.x >= 900 or self.rect.x <= -100:  # orientação esquerda e direita
            self.kill()  # exclui a adaga

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # função de atualização geral
    def update(self):
        self.move()  # Função de movimento
        self.destroy()  # função de remoção da adaga

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#espada do jogador
class Sword(pygame.sprite.Sprite):
    # =======================================================================================================================================================================
    # Código Base
    def __init__(self):
        super().__init__()
        self.index = 0  # orientação que a espada foi usada
        self.image = pygame.image.load(
            f'objects/sword/0.png').convert_alpha()  # imagem da adaga
        self.image = pygame.transform.scale(
            self.image, (30, 51)).convert_alpha()  # amplia a imagem
        self.rect = self.image.get_rect(
            center=(-200, -200))  # retangulo da espada
        self.dano = 4  # dano

# Código Base
# =======================================================================================================================================================================
# Funções
# =======================================================================================================================================================================

    # função orientação da espada
    def orientation(self):

        #reposiciona a espada em situações expecificas
        if self.rect.y >= 490 and self.index == 0:  # verifica se o personagem chegou ao limite do mapa
            self.rect.y = 555  # reposiciona a espada no mapa
        elif self.rect.y <= 100 and self.index == 0:  # verifica se a espada está no limite do mapa
            self.rect.y = 165  # reposiciona a espada no mapa
        elif self.rect.y >= 490 and self.index == 1:  # verifica se o personagem chegou ao limite do mapa
            self.rect.y = 470  # reposiciona a espada no mapa
        elif self.rect.y <= 100 and self.index == 1:  # verifica se a espada está no limite do mapa
            self.rect.y = 70  # reposiciona a espada no mapa
        elif self.rect.x <= 125 and self.index == 2:  # verifica se a espada está no limite do mapa
            self.rect.x = 80  # reposiciona a espada no mapa
        elif self.rect.x >= 610 and self.index == 2:  # verifica se a espada está no limite do mapa
            self.rect.x = 570  # reposiciona a espada no mapa
        elif self.rect.x <= 125 and self.index == 3:  # verifica se a espada está no limite do mapa
            self.rect.x = 175  # reposiciona a espada no mapa
        elif self.rect.x >= 610 and self.index == 3:  # verifica se a espada está no limite do mapa
            self.rect.x = 660  # reposiciona a espada no mapa

        # verifica a orientação da espada
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        if 0 <= self.index <= 1:  # sul ou norte
            # atualiza a imagem
            self.image = pygame.image.load(
                f'objects/sword/{self.index}.png').convert_alpha()
            # amplia a imagem
            self.image = pygame.transform.scale(
                self.image, (30, 51)).convert_alpha()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # verifica a orientação da espada
        elif 2 <= self.index <= 3:  # esquerda ou direita

            # atualiza a imagem
            self.image = pygame.image.load(
                f'objects/sword/{self.index}.png').convert_alpha()

            # amplia a imagem
            self.image = pygame.transform.scale(
                self.image, (51, 30)).convert_alpha()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # função de atualização geral
    def update(self):
        self.orientation()  # função orientação da espada

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#bola do ocotorok
class Ball(pygame.sprite.Sprite):
    # =======================================================================================================================================================================
    # Código Base
    def __init__(self):
        super().__init__()
        self.index = 0  # orientação que a espada foi usada
        self.image = pygame.image.load(
            f'objects/enemie_gun_0.png').convert_alpha()  # imagem da ball
        self.image = pygame.transform.scale(
            self.image, (26, 30)).convert_alpha()  # amplia a imagem
        self.rect = self.image.get_rect(
            center=(-200, -200))  # retangulo da espada
        self.dano = 2  # dano
        self.speed = 5

# =======================================================================================================================================================================
# Funções
# =======================================================================================================================================================================

    # Função de movimento

    def move(self):
        # verifica a orientação de disparo da ball e move ela de acordo com ela
        if self.index == 0:  # direção sul
            self.rect[1] += self.speed  # incrementa o vetor da ball
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.index == 1:  # direção norte
            self.rect[1] -= self.speed  # incrementa o vetor da ball

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.index == 2:  # direção esquerda
            self.rect[0] -= self.speed  # incrementa o vetor da ball

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.index == 3:  # direção direita
            self.rect[0] += self.speed  # incrementa o vetor da ball
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # função de remoção da ball
    def destroy(self):
        # se a ball ultrapassar os limites do mapa ela é exclui
        if self.rect.y >= 900 or self.rect.y <= -100:  # orientação sul e norte
            self.kill()  # exclui a ball

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        elif self.rect.x >= 900 or self.rect.x <= -100:  # orientação esquerda e direita
            self.kill()  # exclui a ball

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # função de atualização geral
    def update(self):
        self.move()  # Função de movimento
        self.destroy()  # função de remoção da ball

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
