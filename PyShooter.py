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
			
		def update(self):
			
			'''add enemy speed to current rectangle y value so it moves horizotally across the screen'''
			self.rect.right += self.enemyspeed
			
			'''get the rectangle for the screen'''
			screenrect = screen.get_rect()
			
			'''if the left edge of enemy >= edge of screen then reset '''
			if self.rect.left >= screenrect.right:
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
	
def eventHandling():
	'''handle event'''
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
		if event.type == MOUSEBUTTONDOWN:
			'''Mouse clicked so if sprites rectangles collide the pygame.sprite.collide_rect returns 
			eighter True of False'''
			hit = pygame.sprite.collide_rect(crosshairs, enemy)
			
			if hit == True:
				print "hit"

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

'''innitialize an instance of pi class with start y = 70 and speed of 10'''
enemy = enemyClass(70 , 10)

''' create a sprite group which will contain all our sprites
This sprite groupd can draw all the sprites it contains to the screen'''
allsprites = pygame.sprite.RenderPlain((crosshairs, enemy))

while True:
	clock.tick(framesPerSecond)
	eventHandling()
	background.draw()
	
	allsprites.update()
	allsprites.draw(screen)
	
	pygame.display.update()
	
