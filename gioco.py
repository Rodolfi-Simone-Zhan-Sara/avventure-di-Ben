import pygame

pygame.init()

SCREEN_W = 900
SCREEN_H = 700

BEN1_IMAGE = pygame.image.load("img/ben1.png")
BEN2_IMAGE = pygame.image.load("img/ben2.png")
BEN1_STARTING_POSITION = (20, 550)
BEN1_THRUST = 3
BEN1_SPEED = 4
GRAVITY = 0.1

LEANDRO_IMAGE = pygame.image.load("img/Leandro.png")
LEANDRO_SIZE = LEANDRO_IMAGE.get_size()
LEANDRO_POSITION = (SCREEN_W / 2 - LEANDRO_IMAGE[0] / 2, SCREEN_H / 2 - LEANDRO_IMAGE[1] / 2 -20)
