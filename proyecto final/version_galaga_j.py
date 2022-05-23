import pygame, sys, random 

#colores
WHITE = ( 255, 255, 255)
BLACK = (   0,   0,   0)
#fps
FPS = (60)
#dimensiones pantalla
SCREEN_WIDTH = (400)
SCREEN_HEIGHT = (600)
#dimensiones en el juego
SHIPS_WIDTH = (25)
SHIPS_HEIGHT = (25)
#clases
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		jugador = self.image = pygame.image.load("imagenes/nave_j1/nave_jugador.png").convert()
		jugador = self.image = pygame.transform.scale(jugador, [SHIPS_WIDTH,SHIPS_HEIGHT])
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREEN_WIDTH//2
		self.speed_x = 0
		self.speed_y = 0
	def changespeed(self, x, y):
		self.speed_x += x
		self.speed_y += y
	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		if (self.rect.top < 0):
			self.rect.top = 0
		if (self.rect.bottom >  SCREEN_HEIGHT):
			self.rect.bottom  = SCREEN_HEIGHT
		if (self.rect.left < 0):
			self.rect.left = 0
		if (self.rect.right > SCREEN_WIDTH):
			self.rect.right = SCREEN_WIDTH
class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		laser = self.image = pygame.image.load("imagenes/laser/laser.png").convert()
		laser = self.image = pygame.transform.scale(laser, [10,15])
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y -= 10
class Green_enemi(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		green = self.image = pygame.image.load("imagenes/enemigos/Green_enemi/Green_1.png").convert()
		green = self.image = pygame.transform.scale(green, [SHIPS_WIDTH,SHIPS_HEIGHT])
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 20
		self.rect.y = 20
	def update(self):
		pass
class Game(object):
	def __init__(self):
		self.game_over = False
		self.score = 0
		self.enemies_list = pygame.sprite.Group()
		self.laser_list = pygame.sprite.Group()
		self.all_sprides_list = pygame.sprite.Group()
		for i in range(2):
			green_enemi = Green_enemi()
			self.enemies_list.add(green_enemi)
			self.all_sprides_list.add(green_enemi)
		self.player = Player()
		self.all_sprides_list.add(self.player)
		#sonido y fondo 
		self.sonido = pygame.mixer.Sound("imagenes/laser/laser5.ogg")
		self.fondo = pygame.image.load("imagenes/fondo/fondo.jpg").convert()
		self.fondo = pygame.transform.scale(self.fondo, [SCREEN_WIDTH,SCREEN_HEIGHT])
		self.icono = pygame.image.load("imagenes/fondo/icono.png")
		pygame.display.set_icon(self.icono)
		pygame.display.set_caption("Trabajo final Algoritmos y programación")
	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
			#movimiento jugador
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.player.changespeed(-3,0)
				if event.key == pygame.K_RIGHT:
					self.player.changespeed(3,0)
				if event.key == pygame.K_UP:
					self.player.changespeed(0,-3)
				if event.key == pygame.K_DOWN:
					self.player.changespeed(0,3)
				if event.key == pygame.K_SPACE:
					self.laser = Laser()
					self.laser.rect.x = self.player.rect.x +8
					self.laser.rect.y = self.player.rect.y -6
					self.laser_list.add(self.laser)
					self.all_sprides_list.add(self.laser)
					if not self.game_over:
						self.sonido.play()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.player.changespeed(3,0)
				if event.key == pygame.K_RIGHT:
					self.player.changespeed(-3,0)
				if event.key == pygame.K_UP:
					self.player.changespeed(0,3)
				if event.key == pygame.K_DOWN:
					self.player.changespeed(0,-3)
			#reiniciar el juego 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					if self.game_over:
						self.__init__()
	def run_logic(self):
		if not self.game_over:
			self.all_sprides_list.update()
			for self.laser in self.laser_list:
				self.enemies_hit_list = pygame.sprite.spritecollide(self.laser, self.enemies_list, True)
				for self.enemies in self.enemies_hit_list:
					self.all_sprides_list.remove(self.laser)
					self.laser_list.remove(self.laser)
					self.score += 150
					print(self.score)
					if self.laser.rect.y < -10:
						self.laser_list.remove(self.laser)
						self.all_sprides_list.remove(self.laser)
			if len(self.enemies_list) == 0:
				self.game_over = True
	def display_frame(self, screen):
		if self.game_over:
			font = pygame.font.SysFont("serif", 25)
			text = font.render("Game over, Click 'R' to continue", True, WHITE)
			center_text_x = SCREEN_WIDTH//2
			center_text_y = SCREEN_HEIGHT//2
			screen.blit(self.fondo, [0,0])
			screen.blit(text,[center_text_x-170,center_text_y-20])
		if not self.game_over:
			screen.blit(self.fondo, [0,0])
			self.all_sprides_list.draw(screen)
		pygame.display.flip()
def main():
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
	done = False
	clock = pygame.time.Clock()
	game = Game()
	while not done:
		done = game.process_events()
		game.run_logic()
		game.display_frame(screen)
		clock.tick(FPS)
	pygame.quit()
if __name__ == "__main__":
	main()