import pygame

pygame.init()

SCREEN_W = 902
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


screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

BLACK = (0,0,0)
WHITE = (255,255,255)

LAVA = pygame.Rect (screen, WHITE, SCREEN_W, 5)
BASE = pygame.Rect (screen, BLACK, 180, 110) 
PORTA = pygame.Rect (screen, BLACK, 10, 190) 
BLOCCO_SALTO = pygame.Rect (screen, BLACK, 163, 80) 


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

    def jump(self):
        self.fall_speed = - BEN1_THRUST

    def reset(self):
        self.alive = True
        self.fall_speed = 0
        self.y = BEN1_STARTING_POSITION[1]
    

pygame.display.set_caption("Le avventure di Ben")
clock = pygame.time.Clock()
background_colour = (WHITE)
running = True


BEN1 = Ben()
LAVA = Entity
BASE = Entity
PORTA = Entity
BLOCCO_SALTO = Entity

entities = (BEN1, LAVA, BASE, PORTA, BLOCCO_SALTO)

while running:
    
import pygame

pygame.init()


screen = pygame.display.set_mode((900, 700))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pulsante1 = pygame.draw.rect(screen, (WHITE),(100, 490, 200, 150))
pulsante2 = pygame.draw.rect(screen, (WHITE),(600, 490, 200, 150))
font = pygame.font.SysFont("brittanic", 35)
font1 = pygame.font.SysFont("brittanic", 57)
testo1 = font.render("Giochi d'azione", True, BLACK)
testo2 = font.render("Giochi di abilità", True, BLACK)
testo3 = font1.render("SCEGLI LA MODALITÀ A CUI VUOI GIOCARE!", True, WHITE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if pulsante1.collidepoint(pos) and pressed1:
            print("YEAH")
        if pulsante2.collidepoint(pos) and pressed1:
            print("WOW")
    pygame.display.update()
    screen.blit(testo1, (100, 540))
    screen.blit(testo2, (600, 540))
    screen.blit(testo3, (13, 30))
    
    '''
    blocchi + grandi
    blocchi centrati
    testo centrato
    testo + grande a capo
    '''
