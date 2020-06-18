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

LEANDRO_IMAGE = pygame.image.load("img/leandro.png")
LEANDRO_SIZE = LEANDRO_IMAGE.get_size()
LEANDRO_POSITION = (SCREEN_W / 2 - LEANDRO_SIZE[0] / 2, SCREEN_H / 2 - LEANDRO_SIZE[1] / 2 - 50)

LAPIDE_IMAGE = pygame.image.load("img/lapide.jpg")
LAPIDE_SIZE = LAPIDE_IMAGE.get_size()
LAPIDE_POSITION = (SCREEN_W / 2 - LAPIDE_SIZE[0] / 2, SCREEN_H / 2 - LAPIDE_SIZE[1] / 2 + 50)

FURIE1_IMAGE = pygame.image.load("img/furie1.png")
FURIE2_IMAGE = pygame.image.load("img/furie2.png")
BEN_FURIE1_IMAGE = pygame.image.load("img/ben-furie1.png")
BEN_FURIE2_IMAGE = pygame.image.load("img/ben-furie2.png")
SUSI = pygame.transform.flip(pygame.image.load("img/furie1.png"), True, False)
