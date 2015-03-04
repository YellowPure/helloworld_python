import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen=pygame.display.set_mode((640,320),0,32)
mouse_cursor=pygame.image.load('fugu.png').convert_alpha()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	rand_col=(randint(0,255),randint(0,255),randint(0,255))
	screen.lock()

	for x in xrange(100):
		rand_pos=(randint(0,639),randint(0,479))
		screen.set_at(rand_pos,rand_col)

	screen.unlock()

	screen.blit(mouse_cursor,(100,200),(0,0,100,100))
	pygame.display.update()