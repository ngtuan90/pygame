#! /usr/bin/env python

import pygame, sys

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200, 150),0 , 32)
backgroundfile = "blade.jpg"
mousefile="ball.gif"

background = pygame.image.load(backgroundfile).convert()
mouse = pygame.image.load(mousefile).convert()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	screen.blit(background, (0,0))
	
	
	x,y = pygame.mouse.get_pos()
	
	x -= mouse.get_width()/2
	y -=mouse.get_height()/2
	
	screen.blit(mouse, (x,y))
	
	pygame.display.update()
