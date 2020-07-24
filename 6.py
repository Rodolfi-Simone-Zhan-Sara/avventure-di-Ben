import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
Eroe = pygame.image.load("img/eroe.png")
EROE = pygame.transform.scale(Eroe,(60, 55))
velocita = 2.5
v = 0
s = 0
score = 0

all_sprites_list = pygame.sprite.Group()
morte_list = pygame.sprite.Group()
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

class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= velocita
      
class Player(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    onground=True
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = EROE
        self.rect = self.image.get_rect()
        draw.add(self)
    def update(self):
        self.rect.x += self.move_x
        xcoll()
        self.rect.y += self.move_y
        ycoll()
        screen.blit(self.image, (self.rect.x, self.rect.y))

def xcoll():
    collision = pygame.sprite.spritecollide(player, plats, False)
    for block in collision:
        if player.move_x > 0:
            player.rect.right = block.rect.left
        if player.move_x < 0:
            player.rect.left = block.rect.right
def ycoll():
    collision = pygame.sprite.spritecollide(player, plats, False)
    player.onground = False
    for block in collision:
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
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#                                           #',
            '#############################################']

    for r in level:
        for c in r:
            if c == ' ':
                pass
            elif c == '#':
                p = Platform(myx,myy)
            myx += 20
        myy += 20
        myx = 0


pygame.init()
pygame.mixer.init()

player = Player()
all_sprites_list.add(player)
build()
game_over = pygame.mixer.Sound("img/Game Over.wav")
font = pygame.font.SysFont("brittanic", 25)
scritta = font.render("Schiva più blocchi che puoi !!!", True, BLACK)

clock = pygame.time.Clock()

player.rect.x = 150
player.rect.y = (screen_height / 2) - 30


while True:
    s += 1
    if s ==10:
        score += 1
        s= 0

    v += 1
    if v == 500:
        velocita +=1
        v= 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:   
                player.move_y = -7 
            if event.key == pygame.K_s: 
                player.move_y = 7
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_w:
                player.move_y = 0
            if event.key == pygame.K_s:
                player.move_y = 0
    all_sprites_list.update()
    
    n = random.randrange(15)

    if n == 1:
        morte = Block(BLACK)
        morte.rect.x = 900
        morte.rect.y = random.randrange(5, 680)
        morte_list.add(morte)
        all_sprites_list.add(morte)

    for blocco in morte_list:
        morte_hit_list = pygame.sprite.spritecollide(player, morte_list, True)
        for giocatore in morte_hit_list:
            all_sprites_list.remove(morte_list)
            game_over.play()

            velocita = 2
            v = 0
            score = 0
            s = 0

        if blocco.rect.x < 50:
            all_sprites_list.remove(blocco)		
            
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    plats.update()
    screen.blit(scritta,(100, 30))
    pygame.display.flip()
    pygame.display.set_caption("Le avventure di Ben: livello 6" + "  Score: " + str(score))
    clock.tick(60)
