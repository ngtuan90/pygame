import pygame,sys,random,os

from pygame.locals import *

def initPyGame():
	pygame.init()
	'''center the pygame window'''
	os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
	'''set the window title'''
	pygame.display.set_caption("Py Shooter")
	'''hide the mouse cursor'''
	pygame.mouse.set_visible(False)
	
	
class backgroundClass():
		'''construcor'''
		def __init__(self):
			'''path to file'''
			backgroundfile = "background.png"
			'''load file to pygame'''
			self.image = pygame.image.load(backgroundfile).convert()
			
		def draw(self):
			screen.blit(self.image, (0,0))

class crosshairsClass(pygame.sprite.Sprite):
	'''constructor'''
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		crosshairsfile = "crosshairs.png"
		
		self.image = pygame.image.load(crosshairsfile).convert_alpha()
		self.rect = self.image.get_rect()
		
	def update(self):
		'''get the mouse posion'''
		position = pygame.mouse.get_pos()
		'''assign it to the center of rectangle'''
		self.rect.center = position
		
class enemyClass(pygame.sprite.Sprite):
	
	
		'''construcor'''
		def __init__(self, starty, speed):
			'''initialize the super sprite class'''
			pygame.sprite.Sprite.__init__(self)
			
			'''path to file'''
			enemyfile = "enemy.png"
			
			'''load file to pygame'''
			self.image = pygame.image.load(enemyfile).convert_alpha()
			self.rect = self.image.get_rect()
			
			self.rect.right = 0
			self.rect.centery = starty
			
			self.enemyspeed = speed
			
		def increaseSpeed(self):
			self.enemyspeed += 10
			
		def update(self):
			
			'''add enemy speed to current rectangle y value so it moves horizotally across the screen'''
			self.rect.right += self.enemyspeed
			
			'''get the rectangle for the screen'''
			screenrect = screen.get_rect()
			
			'''if the left edge of enemy >= edge of screen then reset '''
			if self.rect.left >= screenrect.right:
				self.reDraw(screenrect)
				
		def reDraw(self, screenrect):
			self.rect.right = 0
			'''random y position of enemy'''
			self.rect.top = self.randomYValue(screenrect)
				
		def randomYValue(self, screenrect):
			startrange = self.rect.height
			endrange = screenrect.height - self.rect.height
			
			randomY = random.randrange(startrange, endrange)
			
			return randomY
			
		def draw(self):
			screen.blit(self.image, (0,0))
			
		def stop(self):
			self.rect.right = 0
			self.rect.top = 0
			self.draw()
	
class scoreClass:
	def __init__(self):
		self.value = 0
		'''Set a fone default font with size'''
		self.font = pygame.font.Font(None, 50)
		
	def update(self):
		'''Font.render (text, fontSmoothing, colour(rgb))'''
		text = self.font.render("Score: %s" % self.value, 1, (255, 255, 255))
		textRect = text.get_rect()
		screenrect = screen.get_rect()
		textRect.centerx = screenrect.width - textRect.width
		screen.blit(text, textRect)
		
class bulletClass:
	def __init__(self, value):
		pygame.sprite.Sprite.__init__(self)
		bulletfile = "bullet.png"
		self.quatity = value
		self.image = pygame.image.load(bulletfile).convert_alpha()
		self.rect = self.image.get_rect()
				
	def draw(self):
		for num in range(self.quatity):
			screen.blit(self.image, (0+num*20,0))

def eventHandling():
	'''handle event'''
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
		if event.type == MOUSEBUTTONDOWN:
			'''Mouse clicked so if sprites rectangles collide the pygame.sprite.collide_rect returns 
			eighter True of False'''
			hit = enemy.rect.collidepoint(crosshairs.rect.centerx, crosshairs.rect.centery)
			
			if hit == True:
				score.value += 1
				enemy.reDraw(screen.get_rect())
				enemy.increaseSpeed()
			else:
				bullet.quatity -= 1
				screen.blit(background.image, (0, 0+bullet.quatity*20), pygame.Rect(0, 0+bullet.quatity*20, 50, 50))
				if (bullet.quatity == 0):
					gameOver()
					
def gameOver():
	drawGameOver()
	while True:
		''' Pause Until Input is Given '''
		e = pygame.event.wait()
		if e.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
			pygame.quit()
			sys.exit()
	

def drawGameOver():
    ''' Display GameOver Text '''
    font = pygame.font.Font(None, 50)
    text1 = font.render("GAME OVER", 1, (255, 0, 0))
    text1pos = text1.get_rect()
    text1pos.centerx = screen.get_rect().centerx 
    text1pos.centery = screen.get_rect().centery - 50
    screen.blit(text1, text1pos)
    
    ''' Display GameOver Text '''
    font = pygame.font.Font(None, 45)
    text2 = font.render("Total Score: %s" % score.value, 1, (255, 0, 0))
    text2pos = text1.get_rect()
    text2pos.centerx = screen.get_rect().centerx
    text2pos.centery = screen.get_rect().centery
    screen.blit(text2, text2pos)
    
    font = pygame.font.Font(None, 36)
    text3 = font.render("Press Any Key to Quit", 1, (255, 0, 0))
    text3pos = text2.get_rect()
    text3pos.centerx = screen.get_rect().centerx
    text3pos.centery = screen.get_rect().centery + 50
    screen.blit(text3, text3pos)
    pygame.display.flip()

'''initialize the display and environment varianles'''
initPyGame()

'''set display to width 370, height 542 with 32 bit and start at 0 position'''
screen = pygame.display.set_mode((1280,720),0,32)

'''use to manage how fast the screen updates'''
clock = pygame.time.Clock()

'''frame per second'''
framesPerSecond = 20

'''declare the class instances to used in game loop'''
background = backgroundClass()
crosshairs = crosshairsClass()
score = scoreClass()
bulletsNum = 5
bullet = bulletClass(bulletsNum)
speed = 10

'''innitialize an instance of pi class with start y = 70 and speed of 10'''
enemy = enemyClass(70 , speed)

''' create a sprite group which will contain all our sprites
This sprite groupd can draw all the sprites it contains to the screen'''
allsprites = pygame.sprite.RenderPlain((crosshairs, enemy))

while True:
	clock.tick(framesPerSecond)
	eventHandling()
	background.draw()
	bullet.draw()
	score.update()
	
	allsprites.update()
	allsprites.draw(screen)
	
	pygame.display.update()
	
