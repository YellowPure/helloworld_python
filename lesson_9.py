import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE=(640,480)
background_image_filename='sushiplate.jpg'
mouse_image_filename='fugu.png'
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
pygame.display.set_caption('hello world!')

clock=pygame.time.Clock()

#load image
background=pygame.image.load(background_image_filename).convert()
sprite=pygame.image.load(mouse_image_filename).convert_alpha()

x,y=100.,100.
speed_x,speed_y=133.,170.

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()

	screen.blit(background,(0,0))
	screen.blit(sprite,(x,y))
	time_passed=clock.tick()
	time_passed_seconds=time_passed/1000.0

	x+=time_passed_seconds*speed_x
	y+=time_passed_seconds*speed_y

	if x>640-sprite.get_width():
		speed_x=-speed_x
		x=640-sprite.get_width()
	elif x<0:
		speed_x=-speed_x
		x=0.

	if y>480-sprite.get_height():
		speed_y=-speed_y
		y=480-sprite.get_height()
	elif y<0:
		speed_y=-speed_y
		y=0.


	pygame.display.update()