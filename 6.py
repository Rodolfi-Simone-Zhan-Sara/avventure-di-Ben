import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
AZZURRO = (0, 128, 255)
ROSSO = (255, 0, 0)
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
velocita = 2
salto = -7
s = 0
v = 0

all_sprites_list = pygame.sprite.Group()
morte_list = pygame.sprite.Group()

todraw = pygame.sprite.Group()

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
        self.image = pygame.Surface((30, 20))
        self.image.fill(AZZURRO)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 680
        todraw.add(self)
    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        screen.blit(self.image, (self.rect.x, self.rect.y))


pygame.init()


player = Player()
all_sprites_list.add(player)

font = pygame.font.SysFont("brittanic", 25)
scritta = font.render("Schiva più blocchi che puoi !!!", True, BLACK)


    

clock = pygame.time.Clock()

player.rect.x = 150

while True:

    s +=1
    if s == 100000:
        salto -=1
        s = 0
    
    v += 1
    if v == 1000:
        velocita +=2
        v= 0
    print(s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:   
                if player.onground:   
                    player.move_y = salto 
            if event.key == pygame.K_DOWN: 
                onground = False
                player.move_y = +10
            
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_UP:
                player.move_y = 0
            if event.key == pygame.K_DOWN:
                player.move_y = 0
    all_sprites_list.update()
    
    n = random.randrange(20)

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
            salto = -7 
            velocita = 2
            s = 0
            v = 0
        if blocco.rect.x < 50:
            all_sprites_list.remove(blocco)			

        
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    screen.blit(scritta,(100, 20))
    pygame.display.flip()
    pygame.display.set_caption("Le avventure di Ben: livello")
    clock.tick(60)     
