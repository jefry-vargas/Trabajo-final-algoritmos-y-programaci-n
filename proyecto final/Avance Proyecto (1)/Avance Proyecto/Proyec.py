import pygame, random
pygame.init()

ANCHO = 1000
ALTO = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode([ANCHO, ALTO])
clock = pygame.time.Clock()
ejecutar = False

fontlives = pygame.font.SysFont("Algerian", 25)
fontscore = pygame.font.SysFont("Algerian", 25)

score = 0
vidas = 3

#Listas
all_sprite_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

#Fondo
fondo = pygame.image.load("defi.jpg").convert()

#Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nave4.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.centery = 520
        self.speed_x = 0
        self.speed_y = 0

    def changespeed(self, x):
        self.speed_x += x

    #Movimiento del jugador
    def update(self):
        self.rect.x += self.speed_x
        player.rect.y = 520
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > ANCHO):
            self.rect.right = ANCHO
 
#Clase de enemigos
class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemies1.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 50
        self.speedx = 2

    def update(self):
        self.rect.x += self.speedx
        if (self.rect.x == 900):
            self.speedx *= -1
            self.rect.y += 100
        if (self.rect.x == 20):
            self.speedx *= -1
            self.rect.y += 100

class Enemies2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemies3.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 890
        self.rect.y = 100
        self.speedx = -2

    def update(self):
        self.rect.x += self.speedx
        if (self.rect.x == 20):
            self.speedx *= -1
            self.rect.y += 100
        if (self.rect.x == 900):
            self.speedx *= -1
            self.rect.y += 100
    
#Clase de laser
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    
    #Movimiento del laser
    def update(self):
        self.rect.y -= 20

#Genera enemigos
contador = 0
for i in range (18):
    enemies = Enemies()
    enemies.rect.x += contador
    contador+= 50
    enemies_list.add(enemies)

contador2 = 0
for i in range (18):
    enemies2 = Enemies2()
    enemies2.rect.x += contador2
    contador2-= 50
    enemies_list.add(enemies2)
    
#Mete al jugador en todos los sprites
player = Player()
player_list.add(player)

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
NARANJA = (255, 128, 0)
VERDE = (0, 255, 0)
#Bucle principal
while not ejecutar:
    if (len(enemies_list) == 0 or len(player_list) == 0):
        ejecutar = True

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            ejecutar = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutar = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3)
            if event.key == pygame.K_d:
                player.changespeed(3)
            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 28
                laser.rect.y = player.rect.y - 20

                #Mete los laser en una lista
                all_sprite_list.add(laser)
                laser_list.add(laser)
                player = Player()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3)
            if event.key == pygame.K_d:
                player.changespeed(-3)

    #Colision Laser-Enemigos
    for laser in laser_list:
        enemies_hit_list = pygame.sprite.spritecollide(laser, enemies_list, True)
        for enemies in enemies_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 100

        if (laser.rect.y < -10):
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
    
    #Colision Enemigos-Jugador
    for player in player_list:
        player_hit_list = pygame.sprite.spritecollide(player, enemies_list, True)
        for i in player_hit_list:
            vidas -= 1
            if (vidas == 0):
                player_list.remove(player)

    #Dibujar objetos
    
    textlives = fontlives.render("Lives: " + str(vidas), True, WHITE)
    textscore = fontscore.render("Point: " + str(score), True, WHITE)

    screen.blit (textlives, (20, 520))
    screen.blit (textscore, (20, 550))
    
    all_sprite_list.update()
    player_list.update()
    enemies_list.update()
    pygame.display.update()
    screen.blit(fondo, [0,-20])
    all_sprite_list.draw(screen)
    enemies_list.draw(screen)
    player_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()