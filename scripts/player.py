import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    # =======================================================================================================================================================================
    # Código base

    def __init__(self):
        super().__init__()

        # código essencial do player

        # imagem do player
        self.image = pygame.image.load('npc/link/idle/1.png')
        # retangulo do player
        self.rect = self.image.get_rect(center=(400, 355))
        # aumenta o player
        self.image = pygame.transform.scale(
            self.image, (57, 72))
        

        # contadores e checadores
        self.index = 0  # orientação
        self.index_walk = 0  # animação de movimento
        self.index_attack = 0  # animação de attack
        self.life = 12  # vida do player
        self.kills = 0
        self.adagas = 10

        self.keys = pygame.key.get_pressed()  # verifica os botões precionados

# Código base
# =======================================================================================================================================================================
# Funções
# =======================================================================================================================================================================

    # animações, movimentos e comandos basicos do player
    def player_anim_move_input(self):
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # reposiciona o jogador
        if self.rect.y >= 490:  # verifica se o personagem chegou ao limite do mapa
            self.rect.y = 490  # reposiciona o player no mapa
        if self.rect.y <= 100:  # verifica se o player está no limite do mapa
            self.rect.y = 100  # reposiciona o player no mapa
        if self.rect.x <= 125:  # verifica se o playerestá no limite do mapa
            self.rect.x = 125  # reposiciona o player no mapa
        if self.rect.x >= 610:  # verifica se o playerestá no limite do mapa
            self.rect.x = 610  # reposiciona o player no mapa


# reposiciona o jogador
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # attack curto (espada)
        # verifica se o botão "q" está apertado
        if self.keys[pygame.K_q]:
            # verifica se a animação do personagem não está no limite
            if self.index_attack < 2:
                # toca o som de attack
                # incrementa a váriavel que gera animação
                self.index_attack += 1
                # atualiza a imagem de acordo a orientação do player e a váriavel de animação
                self.image = pygame.image.load(
                    f'npc/link/attack/attack{self.index}/{int(self.index_attack)}.png')
                # muda o tamanho da imagem de acordo a orientação do player
                # orientação sul
                if self.index == 0:
                    self.image = pygame.transform.scale(
                        self.image, (63, 78))

                # orientação norte
                elif self.index == 1:
                    self.image = pygame.transform.scale(
                        self.image, (57, 78))

                # orientação esquerda
                elif self.index == 2:
                    self.image = pygame.transform.scale(
                        self.image, (63, 78))

                # orientação direita
                elif self.index == 3:
                    self.image = pygame.transform.scale(
                        self.image, (63, 78))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # attake longo (adaga)
        # verifica se o botão "e" está apertado
        elif self.keys[pygame.K_e] and self.adagas>0:
            # incrementa a váriavel que gera animação
            self.index_attack += 0.75
            # verifica se a animação do personagem não está no limite
            if self.index_attack <= 10:

                # atualiza a imagem de acordo a orientação do player e a váriavel de animação
                self.image = pygame.image.load(
                    f'npc/link/trow/trow{self.index}/{int(self.index_attack)}.png')

                # muda o tamanho da imagem de acordo a orientação do player
                # orientação sul
                if self.index == 0:
                    self.image = pygame.transform.scale(
                        self.image, (60, 75))

                # orientação norte
                elif self.index == 1:
                    self.image = pygame.transform.scale(
                        self.image, (57, 75))

                # orientação esquerda e direita
                elif self.index == 2 or self.index == 3:
                    self.image = pygame.transform.scale(
                        self.image, (69, 69))

            # caso a animação atinja o limite
            # o personagem fica travado no estado parado até a tecla ser solta
            else:
                # atualiza a imagem de acordo com a orientação do player
                # muda o tamanho da imagem
                self.image = pygame.transform.scale(pygame.image.load(
                    f'npc/link/idle/{self.index}.png'), (57, 72))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # andar na orientação sul
        # verifica entre os botões de movimento se apenas o "s" está apertado e não está atacando
        elif self.index_attack == 0 and self.keys[pygame.K_s] and not self.keys[pygame.K_w] and not self.keys[pygame.K_a] and not self.keys[pygame.K_d]:
            if self.index_walk > 9:  # Verifica se a animação atingiu o seu limite
                self.index_walk = 0  # reseta a variavel de animação
            self.index_walk += 0.25  # incrementa a variavel de animação

            # muda orientação do player e move ele
            self.index = 0  # variavel de orientação (sul)
            if self.rect.y >= 490:  # verifica se o personagem chegou ao limite do mapa
                self.rect.y += 0  # se sim seu retangulo não sera incrementado

            else:  # se a animação não chegou ao limite
                self.rect.y += 5  # incrementa o retangulo pra mover o player na direção sul
            # atualiza a imagem

            self.image = pygame.image.load(
                f'npc/link/walk/walk-down/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(
                self.image, (57, 81))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # andar na orientação norte
        # verifica entre os botões de movimento se apenas o "w" está apertado e não está atacando
        elif self.index_attack == 0 and self.keys[pygame.K_w] and not self.keys[pygame.K_s] and not self.keys[pygame.K_a] and not self.keys[pygame.K_d]:
            # contador da animação
            if self.index_walk > 9:  # Verifica se a animação atingiu o seu limite
                self.index_walk = 0  # reseta a variavel de animação
            self.index_walk += 0.25  # incrementa a variavel de animação

            # muda orientação do player e move ele
            self.index = 1  # variavel de orientação (norte)
            if self.rect.y <= 100:  # verifica se o player está no limite do mapa
                self.rect.y += 0  # para o movimento do player

            else:  # se a animação não chegou ao limite
                self.rect.y -= 5  # incrementa o retangulo pra mover o player na direção norte

            # atualiza a imagem
            self.image = pygame.image.load(
                f'npc/link/walk/walk-up/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(
                self.image, (57, 81))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # andar na orientação esquerda
        # verifica entre os botões de movimento se apenas o "a" está apertado e não está atacando
        elif self.index_attack == 0 and self.keys[pygame.K_a] and not self.keys[pygame.K_w] and not self.keys[pygame.K_s] and not self.keys[pygame.K_d]:
            # contador da animação
            if self.index_walk > 9:  # Verifica se a animação atingiu o seu limite
                self.index_walk = 0  # reseta a variavel de animação
            self.index_walk += 0.25  # incrementa a variavel de animação

            # muda orientação do player e move ele
            self.index = 2  # variavel de orientação (esquerda)
            if self.rect.x <= 125:  # verifica se o playerestá no limite do mapa
                self.rect.x += 0  # para o movimento do player

            else:  # se a animação não chegou ao limite
                self.rect.x -= 5  # incrementa o retangulo pra mover o player na direção norte
            # atualiza a imagem
            self.image = pygame.image.load(
                f'npc/link/walk/walk-left/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(
                self.image, (72, 72))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # andar na orientação direita
        # verifica entre os botões de movimento se apenas o "d" está apertado e não está atacando
        elif self.index_attack == 0 and self.keys[pygame.K_d] and not self.keys[pygame.K_w] and not self.keys[pygame.K_s] and not self.keys[pygame.K_a]:
            # contador da animação
            if self.index_walk > 9:  # Verifica se a animação atingiu o seu limite
                self.index_walk = 0  # reseta a variavel de animação
            self.index_walk += 0.25  # incrementa a variavel de animação

            # muda o lado do personagem e move ele
            self.index = 3  # variavel de orientação (direita)
            if self.rect.x >= 610:  # verifica se o playerestá no limite do mapa
                self.rect.x += 0  # para o movimento do player

            else:  # se a animação não chegou ao limite
                self.rect.x += 5  # incrementa o retangulo pra mover o player na direção norte

            # atualiza a imagem
            self.image = pygame.image.load(
                f'npc/link/walk/walk-right/{int(self.index_walk)}.png')
            self.image = pygame.transform.scale(
                self.image, (72, 72))
        # parado

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        else:
            # atualiza a imagem
            self.image = pygame.image.load(
                f'npc/link/idle/{self.index}.png')
            self.image = pygame.transform.scale(
                self.image, (57, 72))
            # atualiza as variaveis de animação
            self.index_attack = 0  # variavel de attack
            self.index_walk = 0  # variavel de movimento

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # função do código do player na tela de menu e game over
    def mainmenu(self):
        if self.index_walk > 9:  # verifica se animação chegou ao limite
            self.index_walk = 0  # reseta a variavel de animação
        self.index_walk += 0.25  # incrementa a variavel de animação

        # atualiza a imagem
        self.image = pygame.image.load(
            f'npc/link/walk/walk-down/{int(self.index_walk)}.png')

        # amplia a imagem
        self.image = pygame.transform.scale(self.image, (57, 75))
    # aplicação das funções

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # função de atualização geral
    def update(self):
        self.keys = pygame.key.get_pressed()  # verifica os botões precionados
        # funções usadas quando o jogo está ativo
        self.player_anim_move_input()  # variavel de animação e comandos basicos do player
        # funções usadas quando o jogo está no menu

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Life(pygame.sprite.Sprite):
 # =======================================================================================================================================================================
    # Código base

    def __init__(self):
        super().__init__()

        # código essencial das vidas
        # imagem das vidas
        self.image = pygame.image.load('objects/lifes/12.png')
        # retangulo das vidas
        self.rect = self.image.get_rect(center=(300, 110))
        self.image = pygame.transform.scale(
            self.image, (100, 27)).convert_alpha()

        # contadores e checadores
        self.cont_life = 12  # vidas

# =======================================================================================================================================================================
# Funções
# =======================================================================================================================================================================
    # função de atualização
    def update(self):
        if self.cont_life <= 12 and self.cont_life >= 1:
            self.image = pygame.image.load(
                f'objects/lifes/{self.cont_life}.png')
            # amplia a imagem
            self.image = pygame.transform.scale(
                self.image, (100, 27)).convert_alpha()
        else:
            self.image = pygame.image.load(f'objects/lifes/0.png')
            # amplia a imagem
            self.image = pygame.transform.scale(
                self.image, (100, 27)).convert_alpha()
        
