import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

draw = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
 
        self.image = pygame.Surface([30, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
class Player(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    
    def __init__(self):
        super().__init__()
 
        self.image = pygame.image.load("img/pistola.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        draw.add(self)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        screen.blit(self.image, (self.rect.x, self.rect.y))

 
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([5, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y -= 8


pygame.init()
pygame.mixer.init()

screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK)
    block.rect.x = random.randrange(890)
    block.rect.y = random.randrange(50, 600)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player()
all_sprites_list.add(player)
sparo = pygame.mixer.Sound("img/sparo.wav")
font = pygame.font.SysFont("brittanic", 25)
scritta = font.render("TOCCA I BLOCCHI, RIESCI AD ARRIVARE A 50 ? IL TUO PUNTEGGIO SI TROVA SUL TERMINALE ", True, BLACK)

done = False

clock = pygame.time.Clock()
score = 0
player.rect.y = 630

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                player.move_x =- 5
            if event.key == pygame.K_d:  
                player.move_x = 5
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_a:
                player.move_x = 0
            if event.key == pygame.K_d:
                player.move_x = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:           
            sparo.play()
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    all_sprites_list.update()

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

        if bullet.rect.y < -5:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        elif score == 50:
            all_sprites_list.remove(bullet, player, block)
            screen.fill(WHITE)
            done= True

    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    screen.blit(scritta,(50, 20))
    pygame.display.flip()
    pygame.display.set_caption("Le avventure di Ben: livello 5" + "  Score: " + str(score))
    clock.tick(60)     
pygame.quit()
