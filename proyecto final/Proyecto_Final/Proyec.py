import pygame, random, sys
pygame.init()

#Constantes
ANCHO = 1000
ALTO = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
CANTENE = 5

screen = pygame.display.set_mode([ANCHO, ALTO])
clock = pygame.time.Clock()
game_over = False
ejecutar = False
playing = False
beginning = True
dead = False
final = False

fontlives = pygame.font.SysFont("Algerian", 25)
fontscore = pygame.font.SysFont("Algerian", 25)

score = 0
lives = 3
#Sonidos
laser_sonido=pygame.mixer.Sound('sonido/laser.wav')
explosion_sonido=pygame.mixer.Sound('sonido/explosion.wav')
golpe_sonido=pygame.mixer.Sound('sonido/golpe.wav')
musica_fondo=pygame.mixer.Sound('sonido/fondo.wav')
musica_fondo.set_volume(0.03)
explosion_sonido.set_volume(0.03)
golpe_sonido.set_volume(0.05)
laser_sonido.set_volume(0.1)

#Listas
all_sprite_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

#Fondo
fondo = pygame.image.load("Fondos/fondo.jpg").convert()
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))
fondo_y = 0
icono = pygame.image.load("Fondos/icono.png")
pygame.display.set_icon(icono)
pygame.display.set_caption("Trabajo final Algoritmos y programación")

titulo = pygame.image.load("Fondos/titulo.png").convert()
titulo.set_colorkey(WHITE)

#Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player/nave4.png").convert()
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
        green = self.image = pygame.image.load("Enemigos/Green_1.png").convert()
        green = self.image = pygame.transform.scale(green, [46,44])
        self.image.set_colorkey(BLACK)
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
        bee = self.image = pygame.image.load("Enemigos/Bee.png").convert()
        bee = self.image = pygame.transform.scale(bee, [41,39])
        self.image.set_colorkey(BLACK)
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
        self.image = pygame.image.load("Laser/laser.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    
    #Movimiento del laser
    def update(self):
        self.rect.y -= 20
#Genera enemigosl
contador = 0
for i in range (CANTENE):
    enemies = Enemies()
    enemies.rect.x += contador
    contador+= 50
    enemies_list.add(enemies)
    all_sprite_list.add(enemies)

contador2 = 0
for i in range (CANTENE):
    enemies2 = Enemies2()
    enemies2.rect.x += contador2
    contador2-= 50
    enemies_list.add(enemies2)
    all_sprite_list.add(enemies2)
    
#Mete al lugador en todos los sprites
player = Player()
player_list.add(player)
all_sprite_list.add(player)

#Bucle principal
while not ejecutar:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3)
            if event.key == pygame.K_d:
                player.changespeed(3)

            if event.key == pygame.K_LEFT:
                player.changespeed(-3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3)

            if event.key == pygame.K_u:
                player.speed_x = 0
                player.speed_y = 0

            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 28
                laser.rect.y = player.rect.y - 20
                if playing:
                    laser_sonido.play()

                #Mete los laser en una lista
                all_sprite_list.add(laser)
                laser_list.add(laser)
                player = Player()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3)
            if event.key == pygame.K_d:
                player.changespeed(-3)

            if event.key == pygame.K_LEFT:
                player.changespeed(3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if game_over:                                   
                    playing = True
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if beginning:
                    musica_fondo.play()   
                    beginning = False
                    playing = True
                               
    #Colision Laser-Enemigos
    for laser in laser_list:
        enemies_hit_list = pygame.sprite.spritecollide(laser, enemies_list, True)
        for enemies in enemies_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 100
            explosion_sonido.play()
              
        if (laser.rect.y < -10):
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            
    #Colision Enemigos-Jugador
    for player in player_list:
        player_hit_list = pygame.sprite.spritecollide(player, enemies_list, True)
        for i in player_hit_list:
            lives -= 1
            golpe_sonido.play()
            if (lives == 0):
                player_list.remove(player)

    #Dibujar objeto
    if beginning:
        font = pygame.font.SysFont("serif", 40)
        final = font.render("Press 'E' to play game.", True, WHITE)
        center_text_x = ANCHO//2
        center_text_y = ALTO//2

        movimiento_fondo = fondo_y % fondo.get_rect().height
        screen.blit(fondo, (0,movimiento_fondo-fondo.get_rect().height))
        if movimiento_fondo < ALTO:
            screen.blit(fondo, (0,movimiento_fondo))
        fondo_y += 1
        screen.blit(final,[center_text_x-180,center_text_y-20])
        screen.blit(titulo, [300,30])

    if playing:
        all_sprite_list.update()
        if(len(player_list) == 0):
            dead = True
            playing = False

        if (len(enemies_list) == 0):
            game_over = True
            playing = False
            
            contador = 0
            CANTENE += 4
            for i in range (CANTENE):
                enemies = Enemies()
                enemies.rect.x += contador
                contador+= 50
                enemies_list.add(enemies)
                all_sprite_list.add(enemies)

            contador2 = 0
            for i in range (CANTENE):
                enemies2 = Enemies2()
                enemies2.rect.x += contador2
                contador2-= 50
                enemies_list.add(enemies2)
                all_sprite_list.add(enemies2)

        movimiento_fondo = fondo_y % fondo.get_rect().height
        screen.blit(fondo, (0,movimiento_fondo-fondo.get_rect().height))
        if movimiento_fondo < ALTO:
            screen.blit(fondo, (0,movimiento_fondo))
        fondo_y += 1
        textlives = fontlives.render("Lives: " + str(lives), True, WHITE)
        textscore = fontscore.render("Point: " + str(score), True, WHITE)
        screen.blit (textlives, (20, 520))
        screen.blit (textscore, (20, 550))
        all_sprite_list.draw(screen)
    pygame.display.flip()

    if not beginning:
        if not playing:
            font = pygame.font.SysFont("serif", 40)
            final = font.render("Level Complete, Press 'R' to play next level.", True, WHITE)
            center_text_x = ANCHO//2
            center_text_y = ALTO//2

            movimiento_fondo = fondo_y % fondo.get_rect().height
            screen.blit(fondo, (0,movimiento_fondo-fondo.get_rect().height))
            if movimiento_fondo < ALTO:
                screen.blit(fondo, (0,movimiento_fondo))
            fondo_y += 1
            screen.blit(final,[center_text_x-350,center_text_y-20])
            screen.blit(titulo, [300,30])

            score = 0
            lives = 3
            player.rect.centerx = ANCHO//2
            player.speed_x = 0
            player.speed_y = 0

        if dead:
            font = pygame.font.SysFont("serif", 40)
            final = font.render("You're Dead, Press 'ESC' to exit.", True, WHITE)
            center_text_x = ANCHO//2 + 80
            center_text_y = ALTO//2

            movimiento_fondo = fondo_y % fondo.get_rect().height
            screen.blit(fondo, (0,movimiento_fondo-fondo.get_rect().height))
            if movimiento_fondo < ALTO:
                screen.blit(fondo, (0,movimiento_fondo))
            fondo_y += 1
            screen.blit(final,[center_text_x-350,center_text_y-20])
            screen.blit(titulo, [300,30])

    if (CANTENE > 17):
        final = True

        if final:
            font = pygame.font.SysFont("serif", 40)
            final = font.render("Game Complete, Press ESC to exit.", True, WHITE)
            center_text_x = ANCHO//2 - 90
            center_text_y = ALTO//2

            movimiento_fondo = fondo_y % fondo.get_rect().height
            screen.blit(fondo, (0,movimiento_fondo-fondo.get_rect().height))
            if movimiento_fondo < ALTO:
                screen.blit(fondo, (0,movimiento_fondo))
            fondo_y += 1
            screen.blit(final,[center_text_x-180,center_text_y-20])
            screen.blit(titulo, [300,30])

            playing: False
            beginning: False
            game_over: False

    clock.tick(FPS)
pygame.quit()