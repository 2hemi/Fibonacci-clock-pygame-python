import pygame
import time
from pygame.locals import *
from datetime import datetime


white = (255,255,255)

black = (0,0,0)

green = (0,255,0)

blue = (0,0,255)

red = (255,0,0)

pygame.init()

display = pygame.display.set_mode((803,503))

display.fill(white)

col20 = white
col30 = white
col10 = white
col102 = white
col50 = white


def splittime(hour):

	liste = []
	
	while True:

		if hour >= 5:
			hour -=5
			liste.append(5)

		if hour >= 3 and hour < 5:
			hour -=3
			liste.append(3)

		if hour == 2:
			hour -=2
			liste.append(2)
		
		if hour == 1:
			hour -=1
			liste.append(1)
		
		if hour == 0:
			break
	
	return liste


while True:

	rect20col = pygame.draw.rect(display, col20, (1,1,201,201))

	rect30col = pygame.draw.rect(display, col30, (1,201,301,301))

	rect10col = pygame.draw.rect(display, col10, (201,1,101,101))

	rect102col = pygame.draw.rect(display, col102, (201,101,101,101))

	rect50col = pygame.draw.rect(display, col50, (301,1,501,501))


	rect20 = pygame.draw.rect(display, black, (1,1,201,201), 3 )

	rect30 = pygame.draw.rect(display, black, (1,201,301,301), 3 )

	rect10 = pygame.draw.rect(display, black, (201,1,101,101), 3 )

	rect102 = pygame.draw.rect(display, black, (201,101,101,101), 3 )

	rect50 = pygame.draw.rect(display, black, (301,1,501,501), 3 )


	
	t = time.localtime()
	
	hour = time.strftime("%H",t)
	
	mint = time.strftime("%M",t)

	hour = int(hour)
	if int(hour) > 12 :
		hour -= 12
	
	mint = int(mint)//5
	for i in splittime(int(hour)):

		if i==5 :
			col50 = red

		if i==3 :
			col30 = red

		if i==2 :
			col20 = red
		
		if i==1 :
			col10 = red


	for i in splittime(int(mint)):

		if i==5 :
			col50 = green

		if i==3 :
			col30 = green

		if i==2 :
			col20 = green
		
		if i==1 :
			col10 = green


	for i in splittime(int(hour)):
		
		for j in splittime(int(mint)):

			if i==5 and i==j:
				col50 = blue

			if i==3 and i==j:
				col30 = blue

			if i==2 and i==j:
				col20 = blue
			
			if i==1 and i==j:
				col10 = blue


	#print(splittime(int(hour)) , splittime(int(mint)))

	for event in pygame.event.get():
		
		if event.type==QUIT:
				pygame.quit()
				

	pygame.display.update()
