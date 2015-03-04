import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE=(640,480)
background_image_filename='sushiplate.jpg'
mouse_image_filename='fugu.png'
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
pygame.display.set_caption('hello world!')

#load image
background=pygame.image.load(background_image_filename).convert()
sprite=pygame.image.load(mouse_image_filename).convert_alpha()

x=0
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()

	screen.blit(background,(0,0))
	screen.blit(sprite,(x,100))
	x+=.5

	if x>640:
		x=-sprite.get_width()
	pygame.display.update()