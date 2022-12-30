import pygame
from sys import exit
from random import choices, choice, randint
from scripts.bomb import Bomb
from scripts.player import Player, Life
from scripts.weapons import Sword, Adaga, Ball
from scripts.snake import Snake
from scripts.slug import Slug
from scripts.octorok import Octorok
from scripts.objects import Adaga_item, Portal, Explosion, Heart
from pygame.locals import *

# =======================================================================================================================================================================
# Funções

# colisão de inimigo com arma curta


def damage_curta(player, arma, grupo_da_arma, inimigo, grupo_do_inimigo):
    # laço para o inimigo dentro de seu grupo
    for inimigo in grupo_do_inimigo:
        # se o inimigo colide com a arma
        if pygame.sprite.collide_rect(arma, inimigo):
            # o recuo não ocorrerá se o inimigo morrer instantaneamente
            if inimigo.life > 0:
                # o inimigo recua de acordo a posição que a arma foi usada
                if arma.index == 0:  # verifica a posição da arma
                    inimigo.rect.y += 50  # recuo do inimigo

                if arma.index == 1:  # verifica a posição da arma
                    inimigo.rect.y += -50  # recuo do inimigo

                if arma.index == 2:  # verifica a posição da arma
                    inimigo.rect.x += -50  # recuo do inimigo

                if arma.index == 3:  # verifica a posição da arma
                    inimigo.rect.x += 50  # recuo do inimigo

                # inimigo recebe o dano de acordo com a arma
            inimigo.life -= arma.dano
            enemy_hit.play()
        # se a vida do inimigo chegou a 0
        if inimigo.life <= 0:
            player.kills += 1
            player.kills -= 1  # corrige bug de morte duplicada
            spaw_item = choices([0, 1, 2], weights=[0.5, 0.25, 0.25], k=1)
            if spaw_item == [1]:
                coração = Heart()
                coração.rect[0] = inimigo.rect[0]
                # passa a posicao inicial em y
                coração.rect[1] = inimigo.rect[1]
                grupo_dos_corações.add(coração)
            elif spaw_item == [2]:
                adagas_item = Adaga_item()
                adagas_item.rect[0] = inimigo.rect[0]
                # passa a posicao inicial em y
                adagas_item.rect[1] = inimigo.rect[1]
                grupo_das_adagas_item.add(adagas_item)
            enemy_kill.play()
            # elimina o inimigo

    # laço para arma em seu grupo
    for arma in grupo_da_arma:
        # se a animação de attack do jogador acaba
        if player.index_attack == 0:
            # elimina a espada
            pygame.sprite.Sprite.kill(arma)
            # e remove ela do mapa
            arma.rect = arma.image.get_rect(center=(-200, -200))

# colisão de inimigo com arma de longo alcance


def damage_longa(player, arma, grupo_da_arma, inimigo, grupo_do_inimigo):
    # laço para o inimigo dentro de seu grupo
    for inimigo in grupo_do_inimigo:
        # se o inimigo colide com a arma
        if pygame.sprite.spritecollideany(inimigo, grupo_da_arma):

            for arma in grupo_da_arma:
                if pygame.sprite.spritecollideany(inimigo, grupo_da_arma):
                    arma.rect = arma.image.get_rect(center=(-200, -200))
                    pygame.sprite.Sprite.kill(arma)

            # o inimigo recua de acordo a posição que a arma foi jogada
            if inimigo.life > 0:
                # o inimigo recua de acordo a posição que a arma foi usada
                if arma.index == 0:  # verifica a posição da arma
                    inimigo.rect.y += 50  # recuo do inimigo

                if arma.index == 1:  # verifica a posição da arma
                    inimigo.rect.y += -50  # recuo do inimigo

                if arma.index == 2:  # verifica a posição da arma
                    inimigo.rect.x += -50  # recuo do inimigo

                if arma.index == 3:  # verifica a posição da arma
                    inimigo.rect.x += 50  # recuo do inimigo

            # inimigo recebe o dano de acordo com a arma
            inimigo.life -= arma.dano
        if inimigo.life <= 0:
            player.kills += 1  # elimina o inimigo
            spaw_item = choices([0, 1, 2], weights=[0.5, 0.25, 0.25], k=1)
            if spaw_item == [1]:
                coração = Heart()
                coração.rect[0] = inimigo.rect[0]
                # passa a posicao inicial em y
                coração.rect[1] = inimigo.rect[1]
                grupo_dos_corações.add(coração)
            elif spaw_item == [2]:
                adagas_item = Adaga_item()
                adagas_item.rect[0] = inimigo.rect[0]
                # passa a posicao inicial em y
                adagas_item.rect[1] = inimigo.rect[1]
                grupo_das_adagas_item.add(adagas_item)

# colisão do jogador com inimigos


def damage_player(player, grupo_do_player, inimigo, grupo_do_inimigo, arma_curta, contador_de_vidas):

    for player in grupo_do_player:
        # reposiciona o jogador
        if pygame.sprite.groupcollide(grupo_do_inimigo, grupo_do_player, False, False):
            dano = choice([dano0, dano1])
            dano.set_volume(0.05)
            dano.play()
            player.life -= inimigo.dano
            contador_de_vidas.cont_life = player.life

            for inimigo in grupo_do_inimigo:
                # reposiciona o inimigo
                if pygame.sprite.spritecollideany(inimigo, grupo_do_player):
                    # o inimigo recua de acordo o sentido
                    if player.index == 0:  # verifica a posição da inimigo
                        inimigo.rect.y += 50  # recuo do inimigo

                    if player.index == 1:  # verifica a posição da inimigo
                        inimigo.rect.y -= 50  # recuo do inimigo

                    if player.index == 2:  # verifica a posição da inimigo
                        inimigo.rect.x -= 50  # recuo do inimigo

                    if player.index == 3:  # verifica a posição da inimigo
                        inimigo.rect.x += 50  # recuo do inimigo

            if player.life < 0:
                player.life = 0

            # recuo do jogador
            if player.index == 0 and player.rect.y >= 120 and player.rect.y <= 460:
                player.rect.y -= 100  # recuo do player
                # passa a posicao inicial em y

            elif player.index == 1 and player.rect.y >= 120 and player.rect.y <= 460:
                player.rect.y += 100  # recuo do player
                # passa a posicao inicial em y

            elif player.index == 2 and player.rect.x >= 145 and player.rect.x <= 580:
                player.rect.x += 100  # recuo do player
                # passa a posicao inicial em x

            elif player.index == 3 and player.rect.x >= 145 and player.rect.x <= 580:
                player.rect.x -= 100  # recuo do player
                # passa a posicao inicial em x

            if player.index_attack > 0:
                # reposiciona a espada após o recuo
                if arma_curta.index == 0:
                    # passa a posicao inicial em x
                    arma_curta.rect[0] = player.rect[0]+20
                    # passa a posicao inicial em y
                    arma_curta.rect[1] = player.rect[1]+65

                # posição da espada quando o jogador esteja na orientação sul
                elif arma_curta.index == 1:
                    # passa a posicao inicial em x
                    arma_curta.rect[0] = player.rect[0]+10
                    # passa a posicao inicial em y
                    arma_curta.rect[1] = player.rect[1]-30

                # posição da espada quando o jogador esteja na orientação esquerda
                elif arma_curta.index == 2:
                    # passa a posicao inicial em x
                    arma_curta.rect[0] = player.rect[0]-40
                    # passa a posicao inicial em y
                    arma_curta.rect[1] = player.rect[1]+35

                # posição da espada quando o jogador esteja na orientação direita
                elif arma_curta.index == 3:
                    # passa a posicao inicial em x
                    arma_curta.rect[0] = player.rect[0]+55
                    # passa a posicao inicial em y
                    arma_curta.rect[1] = player.rect[1]+35


# colisão do jogador com a bola atirada pelo octorok
def damage_player_ball(player, grupo_do_player, ball, grupo_da_ball, contador_de_vidas):
    for player in grupo_do_player:
        if pygame.sprite.groupcollide(grupo_da_ball, grupo_do_player, False, False):
            dano = choice([dano0, dano1])
            dano.set_volume(0.05)
            dano.play()
            player.life -= ball.dano
            if player.life < 0:
                player.life = 0
            for ball in grupo_da_ball:
                if pygame.sprite.groupcollide(grupo_da_ball, grupo_do_player, False, False):
                    ball.kill()
                    ball.rect = ball.image.get_rect(center=(-200, -200))
            contador_de_vidas.cont_life = player.life


def damage_explosion_enemy(npc, grupo_do_npc, grupo_da_explosion):
    for npc in grupo_do_npc:
        if pygame.sprite.spritecollideany(npc, grupo_da_explosion):
            if npc.life == 0:
                player.kills += 1
            npc.life -= ball.dano
            npc.kill()


# exibe o tempo de jogo


def display_score():
    current_time = float(pygame.time.get_ticks() / 1000) - start_time
    score_surf = score_font.render(
        f'Tempo: {current_time:.2f}s', False, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(630, 670))
    window.blit(score_surf, score_rect)
    return current_time

# conta os inimigos mortos pelo player


def conta_mortes_inimigas(contador_de_mortes):
    contador_de_mortes_surf = kills_font.render(
        f'{contador_de_mortes} - Inimigos Mortos', False, (255, 255, 255))
    contador_de_mortes_rect = contador_de_mortes_surf.get_rect(
        center=(150, 20))
    window.blit(contador_de_mortes_surf, contador_de_mortes_rect)

# conta o numero de adagas e exibe para o jogador


def conta_adagas(contador_de_adagas):
    contador_de_adagas_surf = kills_font.render(
        f'{contador_de_adagas} - Adagas Disponiveis', False, (255, 255, 255))
    contador_de_adagas_rect = contador_de_adagas_surf.get_rect(
        center=(160, 80))
    adaga = pygame.image.load(
        'objects/sword/sword_ico.png').convert_alpha()
    adaga_rect = adaga.get_rect(center=((20, 80)))

    window.blit(adaga, adaga_rect)
    window.blit(contador_de_adagas_surf, contador_de_adagas_rect)

# quando o contador do octoroc chegar a 10 o ocotorok atira uma bola


def ocotorok_attack(ocotorok, grupo_do_ocotorok, ball):

    for ocotorok in grupo_do_ocotorok:
        if ocotorok.index_attack >= 10:
            ocotorok.index_attack = 0
            ball = Ball()
            ball.index = ocotorok.index
            ball_group.add(ball)

            # posiciona a bola no mesmo lugar do octorok
            if ocotorok.index == 1 or ocotorok.index == 0:
                # passa a posicao inicial em x
                ball.rect[0] = ocotorok.rect[0]+6
                # passa a posicao inicial em y
                ball.rect[1] = ocotorok.rect[1]-5

            elif ocotorok.index == 3 or ocotorok.index == 2:
                # passa a posicao inicial em x
                ball.rect[0] = ocotorok.rect[0]-5
                # passa a posicao inicial em y
                ball.rect[1] = ocotorok.rect[1]+6

# troca o inimigo bom por uma explosão


def troca_explosão(inimigo, grupo_inimigo, explosão, grupo_explosão):

    for inimigo in grupo_inimigo:
        if inimigo.life >= 1 and inimigo.life < 4 and inimigo.auto_destroy >= 1:
            timer.play()
        if player.life == 0:
            timer.stop()
        # verifica o contador de auto destruição se eles atenderem o requerido ele troca de lugar com uma explosão
        if inimigo.auto_destroy <= 1 or inimigo.life <= 1:
            timer.stop()
            explosão == Explosion()

            grupo_explosão.add(explosão)

            # passa a posicao inicial em x
            explosão.rect[0] = inimigo.rect[0]
            # passa a posicao inicial em y
            explosão.rect[1] = inimigo.rect[1]
            if inimigo.life <= 1:
                player.kills += 0
            else:
                player.kills += 1

            bomb_explosion.play()

            inimigo.kill()

# gera os inimigos no mapa


def spaw_de_inimigos():

    # varifica se o número de inimigos na tela é menor que
    if len(grupo_dos_ocotorok)+len(grupo_dos_bombs)+len(grupo_dos_snakes)+len(grupo_dos_slugs) < spaw_minimo:
        if fase1:
            # gera um portal para spaw de inimigos com cordenadas aleatorias
            if len(portal_group) == 0:
                portal = Portal()
                if player.kills >= 25:
                    portal.color = 'red'
                portal.rect[0] = randint(140, 590)
                portal.rect[1] = randint(130, 430)
                portal_group.add(portal)
        # ativa o spaw de inimigos
        for portal in portal_group:
            if len(grupo_dos_ocotorok)+len(grupo_dos_bombs)+len(grupo_dos_snakes)+len(grupo_dos_slugs) < spaw_minimo:
                # seleciona o inimigo para o spaw de acordo com suas chançes de ser escolhido, isso pode mudar de acordo com as mortes dos inimigos
                if player.kills < 5:
                    escolha = choices([1, 2, 3, 4, 5], weights=[
                        6, 6, 1, 1, 0.1], k=1)
                elif player.kills >= 5 and player.kills < 15:
                    escolha = choices([1, 2, 3, 4, 5], weights=[
                        4, 4, 2, 2, 0.1], k=1)
                elif player.kills >= 15 and player.kills < 25:
                    escolha = choices([1, 2, 3, 4, 5], weights=[
                        4, 4, 4, 4, 0.1], k=1)
                elif player.kills >= 25 and player.kills < 35:
                    escolha = choices([1, 2, 3, 4, 5], weights=[
                        2, 2, 6, 6, 0.1], k=1)
                elif player.kills >= 35 and player.kills < 50:
                    escolha = choices([1, 2, 3, 4, 5], weights=[
                        2, 2, 7, 7, 1], k=1)
                elif player.kills >= 50:
                    escolha = choices([1, 2, 3, 4, 5], weights=[
                        3, 3, 3, 3, 10], k=1)
                # gera os inimigos e da spaw neles no mesmo lugar do portal
                if portal.time >= 45:

                    if escolha == [1]:
                        snake = Snake()
                        grupo_dos_snakes.add(snake)
                        snake.rect[0] = portal.rect[0]
                        snake.rect[1] = portal.rect[1]
                        portal.transported = True

                    elif escolha == [2]:
                        slug = Slug()
                        grupo_dos_slugs.add(slug)
                        slug.rect[0] = portal.rect[0]
                        slug.rect[1] = portal.rect[1]
                        portal.transported = True

                    elif escolha == [3]:
                        bomb = Bomb()
                        grupo_dos_bombs.add(bomb)
                        bomb.rect[0] = portal.rect[0]
                        bomb.rect[1] = portal.rect[1]
                        portal.transported = True

                    elif escolha == [4]:
                        ocotorok = Octorok()
                        grupo_dos_ocotorok.add(ocotorok)
                        ocotorok.rect[0] = portal.rect[0]
                        ocotorok.rect[1] = portal.rect[1]
                        portal.transported = True
                    elif escolha == [5]:
                        ocotorok = Octorok()
                        ocotorok.cor = "troll"
                        grupo_dos_ocotorok.add(ocotorok)
                        ocotorok.rect[0] = portal.rect[0]
                        ocotorok.rect[1] = portal.rect[1]
                        portal.transported = True

# se o jogador colidir com um coração ele ganha +4 de vida


def pegar_coração(player, grupo_do_player, coração, grupo_do_coração, contador_de_vidas):

    for player in grupo_do_player:
        if pygame.sprite.groupcollide(grupo_do_coração, grupo_do_player, False, False):
            player.life += coração.recovery_life
            # limite de vida
            if player.life > 12:
                player.life = 12
            life_sound.play()
            contador_de_vidas.cont_life = player.life
            for coração in grupo_do_coração:
                if pygame.sprite.spritecollideany(coração, grupo_do_player):
                    coração.used = True  # ativa a remoção do coração

# se o jogador colidir com uma adaga ele ganha +1 adaga


def pegar_adagas(player, grupo_do_player, adaga_item, grupo_das_adagas):

    for player in grupo_do_player:
        if pygame.sprite.groupcollide(grupo_das_adagas, grupo_do_player, False, False):
            player.adagas += 1
            # limite de adagas
            if player.adagas > 99:
                player.adagas = 99
            player.adagas = player.adagas
            adaga_sound.play()
            for adaga_item in grupo_das_adagas:
                if pygame.sprite.spritecollideany(adaga_item, grupo_do_player):
                    adaga_item.used = True  # ativa a remoção da adaga


# Funções
# =======================================================================================================================================================================
# Código Basico
pygame.init()  # inicializa o pygame

window_width = 800  # largura da janela
window_height = 711  # altura da janela

# cria a janela passando a largura e a altura como parametros
window = pygame.display.set_mode(
    (window_width, window_height))
# nome do jogo
pygame.display.set_caption('Zelda Pocket')
# FPS
# joga o clock dentro de uma variavel para controle de fps
fps = pygame.time.Clock()

# Código Basico
# =======================================================================================================================================================================
# backgrounds

arena = pygame.transform.scale(pygame.image.load(
    'Background/temple_arena.png'), (800, 711)).convert()
main_menu = pygame.transform.scale(pygame.image.load(
    'Background/main_menu.png'), (1067, 711)).convert()

game_over = pygame.image.load('Background/game_over.png').convert()

life_group = pygame.sprite.GroupSingle()
life = Life()
portal = Portal()
portal_group = pygame.sprite.GroupSingle()

score_font = pygame.font.Font('font/8bit.ttf', 50)
kills_font = pygame.font.Font('font/8bit.ttf', 20)
font_menu_1 = pygame.font.Font('font/The Wild Breath of Zelda.otf', 140)
font_menu_2 = pygame.font.Font('font/The Wild Breath of Zelda.otf', 50)

# backgrounds
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Player e suas variaveis

player_group = pygame.sprite.GroupSingle()  # cria um grupo para o player
player = Player()  # cria o player
# adiciona o player no grupo
player_group.add(player)
life_cont = player.life
coração = Heart()
grupo_dos_corações = pygame.sprite.Group()

# Player e suas variaveis
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grupo de armas e suas variaveis

# Adaga do jogador
adaga_group = pygame.sprite.Group()  # cria um grupo para adaga
adaga = Adaga()  # chama a adaga
adaga_item = Adaga_item()
grupo_das_adagas_item = pygame.sprite.Group()

# Espada do player
sword_group = pygame.sprite.Group()
sword = Sword()  # chama a espada

ball = Ball()
ball_group = pygame.sprite.Group()
# Grupo de armas e suas variaveis
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grupo de Inimigos e suas variaveis
snake = Snake()  # chama a cobra
slug = Slug()  # chama a lesma
bomb = Bomb()  # chama o bomb
ocotorok = Octorok()  # chama o octorok

# grupo dos inimigos
grupo_dos_ocotorok = pygame.sprite.Group()
grupo_dos_bombs = pygame.sprite.Group()
grupo_dos_snakes = pygame.sprite.Group()
grupo_dos_slugs = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()


explosion = Explosion()


# Grupo de Inimigos e suas variaveis
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define a fase ativa (fase sempre começa False)

fase1 = False

# Define a fase ativa (fase sempre começa False)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Timer e contadores
score = 0
enemies_deaths = 0
spaw_minimo = 5
#1- snake(snake), 2 - lesma(slug), 3 - bomb, 4 - octorok, 5 - octorokTroll
inimigos = [1, 2, 3, 4, 5]
alert_ativator = True


# Timer e contadores
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# sons

# sons de attack
attack0 = pygame.mixer.Sound('audio/link_attack/attack0.wav')
attack1 = pygame.mixer.Sound('audio/link_attack/attack1.wav')
attack2 = pygame.mixer.Sound('audio/link_attack/attack2.wav')
attack3 = pygame.mixer.Sound('audio/link_attack/attack3.wav')


# sons de dano
dano0 = pygame.mixer.Sound('audio/link_dano/dano0.wav')
dano1 = pygame.mixer.Sound('audio/link_dano/dano1.wav')

# bomb
bomb_explosion = pygame.mixer.Sound('audio/bomb/explosion.wav')
bomb_explosion.set_volume(0.05)
timer = pygame.mixer.Sound('audio/bomb/timer.wav')
timer.set_volume(0.05)

# itens
life_sound = pygame.mixer.Sound('audio/sfx/heart.wav')
life_sound.set_volume(0.05)
adaga_sound = pygame.mixer.Sound('audio/sfx/item.wav')
adaga_sound.set_volume(0.05)

# inimigos
enemy_hit = pygame.mixer.Sound('audio/sfx/enemy_hit.wav')
enemy_hit.set_volume(0.05)
enemy_kill = pygame.mixer.Sound('audio/sfx/enemy_kill.wav')
enemy_kill.set_volume(0.05)

# alert
alert = pygame.mixer.Sound('audio/sfx/hey_listen.wav')
alert.set_volume(0.1)

# Musicas
# main menu
main0 = pygame.mixer.Sound('audio/music/main_menu/main0.wav')
main1 = pygame.mixer.Sound('audio/music/main_menu/main1.wav')
main2 = pygame.mixer.Sound('audio/music/main_menu/main2.wav')
main3 = pygame.mixer.Sound('audio/music/main_menu/main3.wav')
main4 = pygame.mixer.Sound('audio/music/main_menu/main4.wav')
# toca musica do menu
main_menu_song = choice([main0, main1, main2, main3, main4])
main_menu_song.play(loops=-1).set_volume(0.1)

# battle
battle0 = pygame.mixer.Sound('audio/music/battle/battle0.wav')
battle1 = pygame.mixer.Sound('audio/music/battle/battle1.wav')
battle2 = pygame.mixer.Sound('audio/music/battle/battle2.wav')
battle3 = pygame.mixer.Sound('audio/music/battle/battle3.wav')
battle4 = pygame.mixer.Sound('audio/music/battle/battle4.wav')
battle5 = pygame.mixer.Sound('audio/music/battle/battle5.wav')


# =======================================================================================================================================================================
# LOOP PRINCIPAL

while True:

    fps.tick(60)  # defini o fps do jogo
    for event in pygame.event.get():  # evento para os comandos especificos do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # acaba com o jogo se a vida do jogador chegar a 0


# LOOP PRINCIPAL
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comandos

        # comandos caso o jogo esteja ativo
        if event.type == KEYDOWN:
            # verifica se alguma fase está ativa
            if fase1:

                # botão de attack curto
                # verifica se o botão "q" (attack curto) está apertado
                # verifica se não há mais espadas sendo usadas
                # verifica se o player não está executando a animação de attack
                if event.key == K_q and len(sword_group) == 0:
                    # cria a espada
                    sword = Sword()
                    # cria variavel que indica a orientação do player
                    sword.index = player.index
                    sword.player = Player()
                    # adiciona a espada para seu grupo
                    sword_group.add(sword)
                    attack = choice([attack0, attack1, attack2, attack3, ])
                    attack.set_volume(0.05)
                    attack.play()
                    if sword.index == 0:
                        # passa a posicao inicial em x
                        sword.rect[0] = player.rect[0]+20
                        # passa a posicao inicial em y
                        sword.rect[1] = player.rect[1]+65

                    # posição da espada quando o jogador esteja na orientação sul
                    elif sword.index == 1:
                        # passa a posicao inicial em x
                        sword.rect[0] = player.rect[0]+10
                        # passa a posicao inicial em y
                        sword.rect[1] = player.rect[1]-30

                    # posição da espada quando o jogador esteja na orientação esquerda
                    elif sword.index == 2:
                        # passa a posicao inicial em x
                        sword.rect[0] = player.rect[0]-40
                        # passa a posicao inicial em y
                        sword.rect[1] = player.rect[1]+35

                    # posição da espada quando o jogador esteja na orientação direita
                    elif sword.index == 3:
                        # passa a posicao inicial em x
                        sword.rect[0] = player.rect[0]+55
                        # passa a posicao inicial em y
                        sword.rect[1] = player.rect[1]+35
# Comandos
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comandos
                # botao para laçar adaga
                # verifica se o botão "e" (attack longo) está apertado
                # verifica se o botão "q" (attack curto) não está apertado
                elif event.key == K_e and not player.keys[pygame.K_q] and player.adagas > 0:
                    # cria adaga
                    adaga = Adaga()
                    # variavel que indica a orientação do jogador
                    adaga.index = player.index
                    # adiciona adaga no seu grupo
                    adaga_group.add(adaga)
                    attack = choice([attack0, attack1, attack2, attack3])
                    attack.set_volume(0.05)
                    attack.play()
                    player.adagas += -1
                    # posição inicial da adaga quando o jogador está nas orientação norte ou sul
                    if 0 <= adaga.index <= 1:
                        # passa a posicao inicial em x
                        adaga.rect[0] = player.rect[0]+15
                        # passa a posicao inicial em y
                        adaga.rect[1] = player.rect[1]

                    # posição inicial da adaga quando o jogador está nas orientação esquerda ou direita
                    elif 2 <= adaga.index <= 3:
                        # passa a posicao inicial em x
                        adaga.rect[0] = player.rect[0]+15
                        # passa a posicao inicial em y
                        adaga.rect[1] = player.rect[1]+30
                '''
                # volta ao menu (botão de teste)
                elif event.key == K_SPACE:
                    enemies_deaths = player.kills
                    fase1 = False
                    battle.stop()
                    # muda a música
                    main_menu_song = choice(
                        [main0, main1, main2, main3, main4])
                    main_menu_song.set_volume(0.1)
                    main_menu_song.play(loops=-1)

                # botão para testar inimigos
                elif event.key == K_p:
                    # cria a cobra
                    snake = Snake()
                    bomb = Bomb()
                    slug = Slug()
                    octorok = Octorok()
                    grupo_dos_bombs.add(bomb)
                    grupo_dos_snakes.add(snake)
                    grupo_dos_slugs.add(slug)
                    grupo_dos_ocotorok.add(octorok)
                '''
# Comandos
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comandos
            # Se o jogo não estiver ativo
            else:
                # verifica se o botão "Espaço" está apertado
                if event.key == K_SPACE:
                    # para a musica de menu e toca a música de batalha
                    main_menu_song.stop()
                    battle = choice(
                        [battle0, battle1, battle2, battle3, battle4, battle5])
                    battle.play(loops=-1).set_volume(0.1)

                    # elimina todos os inimigos
                    grupo_dos_snakes.empty()
                    grupo_dos_bombs.empty()
                    grupo_dos_ocotorok.empty()
                    grupo_dos_corações.empty()
                    grupo_das_adagas_item.empty()
                    grupo_dos_slugs.empty()
                    portal_group.empty()
                    ball_group.empty()
                    # posiciona o player no mapa
                    player.rect = player.image.get_rect(center=(396, 340))
                    # reseta a orientação do jogador
                    player.index = 0
                    # ativa as vidas
                    player.life = 12
                    player.adagas = 10
                    # zera as mortes de inimigos
                    player.kills = 0
                    life = Life()
                    life_group.add(life)
                    start_time = int(pygame.time.get_ticks() / 1000)
                    # ativa a fase 1
                    fase1 = True

# Comandos
# =======================================================================================================================================================================
# Fase 1
# =======================================================================================================================================================================
# Atualização de funções
    if fase1:
        # Termina o jogo se a vida do player chegar a 0
        if player.life <= 0 and fase1 == True:
            enemies_deaths = player.kills
            fase1 = False
            battle.stop()
            timer.stop()
            # muda a música
            main_menu_song = choice([main0, main1, main2, main3, main4])
            main_menu_song.set_volume(0.1)
            main_menu_song.play(loops=-1)

        if player.kills == 0 and alert_ativator == True:
            spaw_minimo = 5
            alert.play()
            alert_ativator = False

        elif player.kills >= 5 and player.kills < 15 and alert_ativator == False:
            spaw_minimo = 6
            alert.play()
            alert_ativator = True
        elif player.kills >= 15 and player.kills < 25 and alert_ativator == True:
            spaw_minimo = 6
            alert.play()
            alert_ativator = False
        elif player.kills >= 25 and player.kills < 35 and alert_ativator == False:
            spaw_minimo = 6
            alert.play()
            alert_ativator = True
        elif player.kills >= 35 and player.kills < 50 and alert_ativator == True:
            spaw_minimo = 6
            alert.play()
            alert_ativator = False
        elif player.kills >= 50 and alert_ativator == False:
            spaw_minimo = 6
            alert.play()
            alert_ativator = True
        # chama a função update de todos que estiverem no grupo do  adaga
        adaga_group.update()
        # chama a função update de todos que estiverem no grupo do  player
        player_group.update()
        player.image = player.image.convert_alpha()
        # chama a função update de todos que estiverem no grupo da espada
        sword_group.update()
        # chama a função update de todos que estiverem no grupo da cobra
        grupo_dos_snakes.update()
        # chama a função update de todos que estiverem no grupo da vida

        grupo_dos_ocotorok.update()

        grupo_dos_bombs.update()
        grupo_dos_slugs.update()

        explosion_group.update()
        ball_group.update()
        life_group.update()

        portal_group.update()
        grupo_dos_corações.update()
        grupo_das_adagas_item.update()

# Atualização de funções
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Desenhos

        # desenha o background
        window.blit(arena, (0, 0))
        # desenha a bola do octo
        ball_group.draw(window)
        # desenha todo o grupo da adaga
        adaga_group.draw(window)
        # desenha todo o grupo de inimigos base
        grupo_dos_snakes.draw(window)
        # desenha todo o grupo do octo
        grupo_dos_ocotorok.draw(window)
        grupo_dos_slugs.draw(window)
        grupo_dos_bombs.draw(window)

        explosion_group.draw(window)

        portal_group.draw(window)

        grupo_dos_corações.draw(window)

        grupo_das_adagas_item.draw(window)

        # desenha a epeda e o player de acordo com a orientação do player
        if player.index == 1:
            # desenha todo o grupo da espada)
            sword_group.draw(window)
            # desenha todo grupo do  player na tela
            player_group.draw(window)
        else:
            # desenha todo o grupo da espada)
            player_group.draw(window)
            # desenha todo grupo do  player na tela
            sword_group.draw(window)

        # desenha a barra de vida
        life_group.draw(window)

# Desenhos
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# funções
        # função da arma curta espada
        damage_curta(player, sword, sword_group, snake, grupo_dos_snakes)
        damage_curta(player, sword, sword_group, bomb, grupo_dos_bombs)
        damage_curta(player, sword, sword_group,
                     ocotorok, grupo_dos_ocotorok)
        damage_curta(player, sword, sword_group, slug, grupo_dos_slugs)

        # dano explosão
        damage_player(player, player_group, explosion,
                      explosion_group, sword, life)
        damage_explosion_enemy(snake, grupo_dos_snakes, explosion_group)
        damage_explosion_enemy(slug, grupo_dos_slugs, explosion_group)
        damage_explosion_enemy(bomb, grupo_dos_bombs, explosion_group)
        damage_explosion_enemy(ocotorok, grupo_dos_ocotorok, explosion_group)

        # função da arma longa adaga
        damage_longa(player, adaga, adaga_group, snake, grupo_dos_snakes)
        damage_longa(player, adaga, adaga_group, bomb, grupo_dos_bombs)
        damage_longa(player, adaga, adaga_group,
                     ocotorok, grupo_dos_ocotorok)
        damage_longa(player, adaga, adaga_group, slug, grupo_dos_slugs)

        troca_explosão(bomb, grupo_dos_bombs, explosion, explosion_group)
        ocotorok_attack(ocotorok, grupo_dos_ocotorok, ball)

        # dano de colisão com inimigo e armas
        damage_player(player, player_group, snake,
                      grupo_dos_snakes, sword, life)
        damage_player(player, player_group, ocotorok,
                      grupo_dos_ocotorok, sword, life)
        damage_player(player, player_group, bomb,
                      grupo_dos_bombs, sword, life)
        damage_player(player, player_group, slug,
                      grupo_dos_slugs, sword, life)

        damage_player_ball(player, player_group, ball, ball_group, life)

        score = display_score()

        spaw_de_inimigos()

        pegar_coração(player, player_group, coração, grupo_dos_corações, life)
        pegar_adagas(player, player_group, adaga_item, grupo_das_adagas_item)

        conta_mortes_inimigas(player.kills)

        conta_adagas(player.adagas)

# funções
# =======================================================================================================================================================================
# Main Menu
# =======================================================================================================================================================================
# Main Menu

    else:
        if score == 0:
            window.blit(main_menu, (0, 0))
            # titulo do jogo
            game_name = font_menu_1.render("Zelda Pocket", True, (0, 0, 0))
            game_name_rect = game_name.get_rect(center=(400, 180))
            window.blit(game_name, game_name_rect)

            # instrução para para o jogador
            game_name_info = font_menu_2.render(
                "Aperte Space para iniciar", True, (255, 255, 255))
            game_name_info_rect = game_name.get_rect(center=(520, 550))
            window.blit(game_name_info, game_name_info_rect)

            # botões
            buton_q = score_font.render(
                'Aperte Q para atacar', True, (255, 255, 255))
            buton_q_rect = buton_q.get_rect(center=(400, 600))
            window.blit(buton_q, buton_q_rect)

            # botões
            buton_e = score_font.render(
                'Aperte E para lançar adagas', True, (255, 255, 255))
            buton_e_rect = buton_e.get_rect(center=(390, 50))
            window.blit(buton_e, buton_e_rect)
        else:
            if player.kills >= 30:
                window.blit(game_over, (0, 0))
            else:
                window.blit(main_menu, (0, 0))
            # titulo do jogo

            # instrução para para o jogador
            game_name_info = font_menu_2.render(
                "Aperte Space para jogar de novo", True, (255, 255, 255))
            game_name_info_rect = game_name_info.get_rect(center=(400, 550))
            window.blit(game_name_info, game_name_info_rect)

            # tempo de jogo
            game_name = score_font.render(
                f'Tempo {score:.0f} em Segundos', True, (255, 255, 255))
            game_name_rect = game_name.get_rect(center=(400, 110))
            window.blit(game_name, game_name_rect)

            # inimigos mortos
            game_name = score_font.render(
                f'{enemies_deaths} inimigos mortos', True, (255, 255, 255))
            game_name_rect = game_name.get_rect(center=(400, 210))
            window.blit(game_name, game_name_rect)

         # código para desenhar o player no menu
        player.mainmenu()
        player.image = pygame.transform.scale(
            player.image, (67, 91)).convert_alpha()
        player_group.draw(window)

        player.rect = player.image.get_rect(center=(400, 355))

# Main Menu
# =======================================================================================================================================================================

    # atualiza a tela
    pygame.display.flip()
