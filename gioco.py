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

SUSI_IMAGE = pygame.transform.flip(pygame.image.load("img/furie1.png"), True , False)


LAVA = pygame.line (SCREEN, RED (255, 0, 0), (0, SCREEN_H), (SCREEN_W, SCREEN_H), 3)
BASE = pygame.rect (SCREEN, BLACK (0, 0, 0), 180, 110) 
PORTA = pygame.rect (SCREEN, BLACK (0, 0, 0), 10, 190) 
BLOCCO_SALTO = pygame.rect (SCREEN, BLACK (0, 0, 0), 163, 80) 


DEBUG = False


class Entity:
    def __init__(self, x, y, image, hitbox_relative_size=0):
        self.image = image
        self.size = image.get_size()
        self.hitbox_relative_size = hitbox_relative_size

        self.x = x
        self.y = y
        self.w = self.size[0]
        self.h = self.size[1]

        self.hitbox_x = self.x + hitbox_relative_size
        self.hitbox_y = self.y + hitbox_relative_size
        self.hitbox_w = self.w - hitbox_relative_size * 2
        self.hitbox_h = self.h - hitbox_relative_size * 2

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        if DEBUG:
            pygame.draw.rect(surface, (255, 0, 0), (self.hitbox_x, self.hitbox_y, self.hitbox_w, self.hitbox_h))

    def update(self):
        self.hitbox_x = self.x + self.hitbox_relative_size
        self.hitbox_y = self.y + self.hitbox_relative_size
    
    def is_colliding(self, colliding_entity):
        return self.hitbox_x + self.hitbox_w >= colliding_entity.hitbox_x and \
            self.hitbox_x <= colliding_entity.hitbox_x + colliding_entity.hitbox_w and \
            self.hitbox_y + self.hitbox_h >= colliding_entity.hitbox_y and \
            self.hitbox_y <= colliding_entity.hitbox_y + colliding_entity.hitbox_h


class Ben(Entity):
    def __init__(self):
        super().__init__(BEN1_STARTING_POSITION[0], BEN1_STARTING_POSITION[1], BEN1_IMAGE, +5)
        self.fall_speed = 0
        self.alive = True

    def update(self):
        self.fall_speed += GRAVITY
        self.y += self.fall_speed
        super().update()

    def fly(self):
        self.fall_speed = - BEN1_THRUST

    def reset(self):
        self.alive = True
        self.fall_speed = 0
        self.y = BEN1_STARTING_POSITION[1]


class Block(Entity):
    
