import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
background_image_filename='sushiplate.jpg'
mouse_image_filename='fugu.png'

pygame.init()
SCREEN_SIZE=(640,480)
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)

#load image
background=pygame.image.load(background_image_filename).convert()
sprite=pygame.image.load(mouse_image_filename).convert_alpha()

clock=pygame.time.Clock()
sprite_pos=Vector2(100.0,100.0)
sprite_speed=300

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()	
	screen.blit(background,(0,0))
	screen.blit(sprite,sprite_pos)

	time_passed=clock.tick()
	time_passed_seconds=time_passed/1000.0

	pressed_keys=pygame.key.get_pressed()
	key_direction=Vector2(0,0)
	if pressed_keys[K_LEFT]:
		key_direction.x=-1
	elif pressed_keys[K_RIGHT]:
		key_direction.x=+1
	if pressed_keys[K_DOWN]:
		key_direction.y=+1
	elif pressed_keys[K_UP]:
		key_direction.y=-1

	key_direction.normalize()
	screen.blit(background,(0,0))
	screen.blit(sprite,sprite_pos)

	sprite_pos+=key_direction*sprite_speed*time_passed_seconds

	pygame.display.update()