my_name='Will Mg'
import pygame
from pygame.locals import *
from sys import exit


pygame.init()
screen=pygame.display.set_mode((640,480),0,32)


my_font=pygame.font.SysFont('arial',64)
name_surface=my_font.render(my_name,True,(0,0,255),(255,255,255))

x=0
y=(480 - name_surface.get_height()/2)

background=pygame.image.load('sushiplate.jpg').convert()
pygame.image.save(name_surface,'name.png')
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
		screen.blit(background,(0,0))

		x-=2
		if x< -name_surface.get_width():
			x = 640 - name_surface.get_width()

		screen.blit(name_surface,(x,y))
	pygame.display.update()
