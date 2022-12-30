import pygame
class Portal(pygame.sprite.Sprite):
    # =======================================================================================================================================================================
    # Código base
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'objects/portal/blue/0.png')  # imagem do portal
        self.image = pygame.transform.scale2x(
            self.image)  # aumenta do portal
        self.rect = self.image.get_rect(center=((200,200)))
        self.index_anim=0
        self.color='blue'
        self.transported=False
        self.time=0

    def animation(self):
        self.time+=0.5
        if self.time==50:
            self.time=0
        self.index_anim+=0.2
        if self.index_anim>=3:
            self.index_anim=0

        self.image = pygame.image.load(
            f'objects/portal/{self.color}/{int(self.index_anim)}.png')  # imagem o portal
        self.image = pygame.transform.scale2x(
            self.image).convert_alpha()  # aumenta o portal
    
    #remove o portal
    def destroy(self):
        if self.transported:
            self.kill()

    def update(self):
        self.animation()
        self.destroy()


class Explosion(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #imagem
        self.image = pygame.image.load('npc/bomb/explosion/0.png')
        self.image = pygame.transform.scale(self.image, (70,70))
        #retangulo
        self.rect = self.image.get_rect(center=((400,400)))
        
        self.index_animation = 0
        self.dano = 2
        self.index = 0
        
    def animation(self):
        #atualiza a imagem
        self.image = pygame.image.load(
        f'npc/bomb/explosion/{int(self.index_animation)}.png')
        self.image = pygame.transform.scale(self.image, (70, 70))

        self.index_animation += 0.3 # incrementa a variavel de animação
        if self.index_animation >= 7: # verifica se a animação atingiu o seu limite
            self.kill

            self.rect = self.image.get_rect(center=((-400, -400)))
            self.index_animation = 0 # reseta a variavel de animação
    
    def update(self):
        self.animation() 

#corações
class Heart(pygame.sprite.Sprite):
    # =======================================================================================================================================================================
    # Código base
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'objects/life.png')  # imagem do portal
        self.image = pygame.transform.scale(
            self.image, (30, 25))  # aumenta do portal
        self.rect = self.image.get_rect(center=((200,200)))
        self.used=False
        self.recovery_life=4
        self.time=0
    #remove o item
    def destroy(self):
        self.time+=0.3
        if self.used or self.time>=100:
            self.time=0
            self.rect = self.image.get_rect(center=(-200, -200))  
            self.kill()

    def update(self):
        self.destroy()  

#adagas (item)
class Adaga_item(pygame.sprite.Sprite):
    # =======================================================================================================================================================================
    # Código base
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            'objects/sword/sword_ico.png').convert_alpha()
        self.image = pygame.transform.scale2x(self.image).convert_alpha() 
        self.rect = self.image.get_rect(center=((200,200)))
        self.used=False
        self.recovery_life=4
        self.time=0

    #remove o item
    def destroy(self):
        self.time+=0.3
        if self.used or self.time>=100:
            self.time=0
            self.rect = self.image.get_rect(center=(-200, -200))  
            self.kill()

    def update(self):
        self.destroy()  