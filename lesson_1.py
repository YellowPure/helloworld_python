import pygame

background_image_filename='sushiplate.jpg'
mouse_image_filename='fugu.png'
from pygame.locals import *
from sys import exit


pygame.init()
SCREEN_SIZE=(640,480)
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
pygame.display.set_caption('hello world!')

#load image
background=pygame.image.load(background_image_filename).convert()
mouse_cursor=pygame.image.load(mouse_image_filename).convert_alpha()

Fullscreen=False

x,y=0,0
move_x,move_y=0,0

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()

		if event.type==VIDEORESIZE:
			SCREEN_SIZE=event.size
			screen=pygame.display.set_mode(SCREEN_SIZE,RESIZEABLE,32)
			pygame.display.set_caption('Window resized to '+str(event.size))

		screen_width,screen_height=SCREEN_SIZE

		for j in range(0,screen_height,background.get_height()):
			for i in range(0,screen_width,background.get_width()):
				screen.blit(background,(i,j))
		if event.type==KEYDOWN:
			if event.key==K_LEFT:
				move_x=-1
			elif event.key==K_RIGHT:
				move_x=1
			elif event.key==K_DOWN:
				move_y=1
			elif event.key==K_UP:
				move_y=-1
			elif event.key==K_f:
				Fullscreen=not Fullscreen
				if Fullscreen:
					screen=pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN,32)
				else :
					screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
		elif event.type==KEYUP:
			move_x=0
			move_y=0

		x+=move_x
		y+=move_y

	screen.blit(background,(0,0))

	# x,y=pygame.mouse.get_pos()

	# x-=mouse_cursor.get_width()/2
	# y-=mouse_cursor.get_height()/2

	screen.blit(mouse_cursor,(x,y))

	pygame.display.update()