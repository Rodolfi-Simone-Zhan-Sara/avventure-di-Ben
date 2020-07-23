import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((900,700), 0, 32)
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Ben = pygame.image.load("img/ben2.png")
BEN = pygame.transform.scale(Ben,(52, 55))
draw = pygame.sprite.Group()
plats = pygame.sprite.Group()

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        plats.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Platform1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        plats.add(self)
    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    onground=False
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = BEN
        self.rect=self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 650
        draw.add(self)
    def update(self):
        self.rect.x += self.move_x
        xcoll()
        self.rect.y += self.move_y
        ycoll()
        screen.blit(self.image, (self.rect.x, self.rect.y))

def xcoll():
    collisione = pygame.sprite.spritecollide(player, plats, False)
    for block in collisione:
        if player.move_x > 0:
            player.rect.right = block.rect.left
        if player.move_x < 0:
            player.rect.left = block.rect.right
def ycoll():
        collisione = pygame.sprite.spritecollide(player, plats, False)
        player.onground = False
        for block in collisione:
            if player.move_y == 0:
                player.onground = True
            if player.move_y < 0:
                player.rect.top = block.rect.bottom
                player.move_y = 0     
                player.onground = False
            if player.move_y > 0:
                player.rect.bottom = block.rect.top
                player.onground = True

def build():
    myx = 0
    myy = 0
    level = [
            '#############################################',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                            ',
            '#                                            ',
            '#                                            ',
            '#                             - - - - - - ###',
            '#                                           #',
            '#                        -                  #',
            '#                            #              #',
            '#                    -                      #',
            '#                                           #',
            '#                 -                 #       #',
            '#                                           #',
            '#             -                             #',
            '#                                          ##',
            '#          -                                #',
            '#                                      #    #',
            '#       -                                   #',
            '#                                #          #',
            '#    -                                      #',
            '#                         #                 #',
            '#-                                          #',
            '#                   #          #            #',
            '#############################################']

    for r in level:
        for c in r:
            if c == ' ':
                pass
            elif c == '-':
                p = Platform1(myx,myy)
            elif c == '#':
                p = Platform(myx,myy)
            myx += 20
        myy += 20
        myx = 0

def gravity():
    if not player.onground:
        player.move_y += 1
player = Player()
build()

font = pygame.font.SysFont("brittanic", 30)
font1 = pygame.font.SysFont("brittanic", 20)
testo = font.render("VAI SUBITO ALL'USCITA! E FAI ATTENZIONE!", True, BLACK)
testo1 = font1.render("EXIT", True, BLACK)

while True:

    screen.fill(WHITE)
    gravity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:   
                if player.onground:   
                    player.move_y =- 10
                    player.onground = False
            if event.key == K_LEFT: 
                player.move_x = -6
            if event.key == K_RIGHT:  
                player.move_x = 6
        if event.type == KEYUP:  
            if event.key == K_LEFT:
                player.move_x = 0
            if event.key == K_RIGHT:
                player.move_x = 0

    screen.blit(testo,(100, 50))
    screen.blit(testo1,(860, 286))
    draw.update()
    plats.update()
    pygame.display.update()
    pygame.display.set_caption("Le avventure di Ben: livello 3")
    clock.tick(60)
