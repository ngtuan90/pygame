#! /usr/bin/env python

import pygame, sys

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 6000),0 , 32)

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	screen.blit(background, (0,0))
	
	
	x,y = pygame.mouse.get_pos()
		
	pygame.draw.circle(screen, (255,255,255), (x,y), 10, 0) 
	
	pygame.display.update()
