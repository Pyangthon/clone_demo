import pygame
from pygame.locals import *
from sys import exit

#定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

ticks = 0

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('This is my frist pygame-program')

#载入资源图片
# ===new add ===
#载入背景图
background = pygame.image.load("C:/Users/Administrator/Desktop/Material/background.jpg")
#载入飞机图片
shoot_img = pygame.image.load("C:/Users/Administrator/Desktop/Material/shoot.jpg")
#剪切图片
hero1_rect = pygame.Rect(0, 99, 102, 126)
hero2_rect = pygame.Rect(165, 360, 102, 126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
hero_pos = [200, 500]

#事件循环(main loop)
while True:
	

	#绘制背景
	screen.blit(background, (0, 0))

	#绘制飞机
	if ticks % 50 < 25:
		screen.blit(hero1, hero_pos)
	else:
		screen.blit(hero2, hero_pos)
	ticks += 1

	#更新屏幕
	pygame.display.update()

	#处理游戏退出
	#从消息队列中循环取
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

			#控制方向 ==new add ===
		if event.type == pygame.KEYDOWN:
			if event.key in offset:
				offset[event.key] = 3
		elif event.type == pygame.KEYUP:
			if event.key in offset:
				offset[event.key] = 0

	offset_x = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
	offset_y = offset[pygame.K_DOWN] - offset[pygame.K_UP]
	hero_pos = [hero_pos[0] + offset_x, hero_pos[1] + offset_y]

	#控制方向
	hero_x = hero_pos[0] + offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
	hero_y = hero_pos[1] + offset[pygame.K_DOWN] - offset[pygame.K_UP]
	if hero_x < 0:
		hero_pos[0] = 0
	elif hero_x > SCREEN_WIDTH - hero1_rect.width:
		hero_pos[0] = SCREEN_WIDTH - hero1_rect.width
	else:
		hero_pos[0] = hero_x

	if hero_y < 0:
		hero_pos[1] = 0
	elif hero_y > SCREEN_HEIGHT - hero1_rect.height:
		hero_pos[1] = SCREEN_HEIGHT - hero1_rect.height
	else:
		hero_pos = hero_y
