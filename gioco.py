import pygame
import random

pygame.init()


screen = pygame.display.set_mode((900, 700))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.display.set_caption("Le avventure di Ben")
clock = pygame.time.Clock()
background_colour = (WHITE)
pulsante1 = pygame.draw.rect(screen, (WHITE),(100, 450, 250, 200))
pulsante2 = pygame.draw.rect(screen, (WHITE),(550, 450, 250, 200))
font = pygame.font.SysFont("brittanic", 45)
font1 = pygame.font.SysFont("brittanic", 53)
testo0 = font.render("Giochi ", True, BLACK)
testo1 = font.render("d'azione", True, BLACK)
testo2 = font.render("Giochi", True, BLACK)
testo3 = font.render("d'abilità", True, BLACK)
testo4 = font1.render("SCEGLI LA MODALITÀ ", True, WHITE)
testo5 = font1.render("A CUI VUOI GIOCARE!", True, WHITE)

def livello_1():
    pygame.init()

    screen = pygame.display.set_mode((900,700), 0, 32)
    clock = pygame.time.Clock()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    Ben = pygame.image.load("img/ben2.png")
    BEN = pygame.transform.scale(Ben,(52, 55))
    draw = pygame.sprite.Group()
    plats = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()


    class Block(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
    
            self.image = pygame.Surface([25, 60])
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = 880
            self.rect.y = 260

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
                '-                                            ',
                '-                                            ',
                '-                                            ',
                '#                               #    #    ###',
                '#                                           #',
                '#    #                     #                #',
                '#                                           #',
                '#      #                       #            #',
                '#                                           #',
                '#            #                    #         #',
                '#                                           #',
                '#                  #                   #    #',
                '#                                           #',
                '#                       #          #        #',
                '#                                           #',
                '#                   #         #             #',
                '#                                           #',
                '#               #                           #',
                '#                                           #',
                '#          #                                #',
                '#                                           #',
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
    block = Block()
    all_sprites_list.add(block)


    font = pygame.font.SysFont("brittanic", 30)
    font1 = pygame.font.SysFont("brittanic", 20)
    testo = font.render("Raggiungi l'uscita, stai attento !", True, BLACK)
    testo1 = font1.render("EXIT", True, BLACK)

    while True:

        screen.fill(WHITE)
        gravity()
        pygame.draw.rect(screen, BLACK, (20,320,60,25),)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   
                    if player.onground:   
                        player.move_y =- 10
                        player.onground = False
                if event.key == pygame.K_a: 
                    player.move_x = -6
                if event.key == pygame.K_d:  
                    player.move_x = 6
            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_a:
                    player.move_x = 0
                if event.key == pygame.K_d:
                    player.move_x = 0
        
        morte_hit_list = pygame.sprite.spritecollide(player, all_sprites_list, True)
        if  len(morte_hit_list) > 0:
            livello_2()

        draw.update()
        plats.update() 
        all_sprites_list.draw(screen)
        screen.blit(testo,(100, 50))
        screen.blit(testo1,(6, 286))
        pygame.display.update()
        pygame.display.set_caption("Le avventure di Ben, abilità : livello 1")
        clock.tick(60)

def livello_2():
    pygame.init()

    screen = pygame.display.set_mode((900,700), 0, 32)
    clock = pygame.time.Clock()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    VETRO = (100, 149, 210)
    Ben = pygame.image.load("img/ben2.png")
    BEN = pygame.transform.scale(Ben,(50, 55))
    draw = pygame.sprite.Group()
    plats = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()


    class Block(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
    
            self.image = pygame.Surface([25, 80])
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = 880
            self.rect.y = 220

    class Platform(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((25, 22))
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
            self.image = pygame.Surface((13, 5))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            plats.add(self)

        def update(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    class Platform2(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((13, 5))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            plats.add(self)

        def update(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    class Platform3(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((7, 25))
            self.image.fill(VETRO)
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
            self.rect = self.image.get_rect()
            self.rect.x = 600
            self.rect.y = 650
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
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '#                      .                    #',
                '                       .                     ',
                '                       .                     ',
                '                       .                     ',
                '                       .                     ',
                '#                      .                    #',
                '#-                     .                   ,#',
                '#                      .                    #',
                '#   -                  .                ,   #',
                '#                      .                    #',
                '#                      .                    #',
                '#        -         -   .   ,         ,      #',
                '#                      .                    #',
                '#                      .                    #',
                '#                     -.,                   #',
                '#                      .                    #',
                '#                 ---  .  ,,,               #',
                '#             -        .      ,             #',
                '#                      .                    #',
                '#         -            .          ,         #',
                '#                      .                    #',
                '#    -                 .               ,    #',
                '#                      .                    #',
                '#-                     .                   ,#',
                '#############################################']

        for r in level:
            for c in r:
                if c == ' ':
                    pass
                elif c == '-':
                    plats = Platform1(myx,myy)
                elif c == ',':
                    plats = Platform2(myx,myy)
                elif c == '.':
                    plats = Platform3(myx,myy)
                elif c == '#':
                    plats = Platform(myx,myy)
                myx += 20
            myy += 20
            myx = 0

    def gravity():
        if not player.onground:
            player.move_y += 0.8
        
    player = Player()
    build()
    block = Block()
    all_sprites_list.add(block)


    font = pygame.font.SysFont("brittanic", 30)
    testo = font.render("S P E C C H I O ? ? ?", True, BLACK)
    font1 = pygame.font.SysFont("brittanic", 20)
    testo1 = font1.render("EXIT", True, BLACK)

    while True:
        screen.fill(WHITE)
        gravity()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   
                    if player.onground:   
                        player.move_y =- 10
                        player.onground = False
                if event.key == pygame.K_a: 
                    player.move_x = -6
                if event.key == pygame.K_d:  
                    player.move_x = 6
            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_a:
                    player.move_x = 0
                if event.key == pygame.K_d:
                    player.move_x = 0

        morte_hit_list = pygame.sprite.spritecollide(player, all_sprites_list, True)
        if  len(morte_hit_list) > 0:
            livello_3()

        screen.blit(testo,(230, 50))
        screen.blit(testo1,(7, 250))
        draw.update()
        plats.update()
        all_sprites_list.draw(screen)
        pygame.display.update()
        pygame.display.set_caption("Le avventure di Ben, abilità : livello 2")
        clock.tick(60)

def livello_3():
    pygame.init()

    screen = pygame.display.set_mode((900,700), 0, 32)
    clock = pygame.time.Clock()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    Ben = pygame.image.load("img/ben2.png")
    BEN = pygame.transform.scale(Ben,(52, 55))
    draw = pygame.sprite.Group()
    plats = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()


    class Block(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
    
            self.image = pygame.Surface([25, 60])
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = 880
            self.rect.y = 260

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
    block = Block()
    all_sprites_list.add(block)
    
    font = pygame.font.SysFont("brittanic", 30)
    font1 = pygame.font.SysFont("brittanic", 20)
    testo = font.render("VAI SUBITO ALL'USCITA! GUARDATI ATTORNO! ", True, BLACK)
    testo1 = font1.render("EXIT", True, BLACK)

    while True:

        screen.fill(WHITE)
        gravity()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:   
                    if player.onground:   
                        player.move_y =- 10
                        player.onground = False
                if event.key == pygame.K_a: 
                    player.move_x = -6
                if event.key == pygame.K_d:  
                    player.move_x = 6
            if event.type == pygame.KEYUP:  
                if event.key == pygame.K_a:
                    player.move_x = 0
                if event.key == pygame.K_d:
                    player.move_x = 0

        morte_hit_list = pygame.sprite.spritecollide(player, all_sprites_list, True)
        if  len(morte_hit_list) > 0:
            exit()


        draw.update()
        plats.update()
        all_sprites_list.draw(screen)
        screen.blit(testo,(100, 50))
        screen.blit(testo1,(860, 286))
        pygame.display.update()
        pygame.display.set_caption("Le avventure di Ben, abilità : livello 3")
        clock.tick(60)

def livello_4():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    screen_width = 900
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    Cestino = pygame.image.load("img/cestino.png")
    CESTINO = pygame.transform.scale(Cestino,(60, 55))

    all_sprites_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    morte_list = pygame.sprite.Group()

    draw = pygame.sprite.Group()

    class Block1(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.Surface([35, 20])
            self.image.fill(color)
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.y += 2

    class Block2(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.image = pygame.Surface([35, 20])
            self.image.fill(color)
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.y += 2
            
    class Player(pygame.sprite.Sprite):
        move_x = 0
        move_y = 0
        onground=False

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = CESTINO
            self.rect = self.image.get_rect()
            self.rect.x = 600
            self.rect.y = 680
            draw.add(self)

        def update(self):
            self.rect.x += self.move_x
            self.rect.y += self.move_y
            screen.blit(self.image, (self.rect.x, self.rect.y))


    pygame.init()
    pygame.mixer.init()

    score = 0
    player = Player()
    all_sprites_list.add(player)

    crash = pygame.mixer.Sound("img/Punch.wav")
    font = pygame.font.SysFont("brittanic", 25)
    scritta = font.render("Prendi 30 blocchi prima che cadano, ma stai attento a quelli ROSSI!!", True, BLACK)

    clock = pygame.time.Clock()

    player.rect.y = 630

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()
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

        all_sprites_list.update()
        
        n = random.randrange(30)

        if n == 1:
            block = Block1(BLACK)
            block.rect.x = random.randrange(5, 875)
            block.rect.y = 0
            block_list.add(block)
            all_sprites_list.add(block)

        n = random.randrange(120)

        if n == 1:
            morte = Block2(RED)
            morte.rect.x = random.randrange(5, 875)
            morte.rect.y = 0
            morte_list.add(morte)
            all_sprites_list.add(morte)
    
        for blocco in block_list:
            block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
            for giocatore in block_hit_list:
                block_list.remove(blocco)
                all_sprites_list.remove(blocco)
                score += 1
            if blocco.rect.y > 640:
                block_list.remove(blocco)
                all_sprites_list.remove(blocco)  

        for blocco in morte_list:
            morte_hit_list = pygame.sprite.spritecollide(player, morte_list, True)
            for giocatore in morte_hit_list:
                crash.play()
                all_sprites_list.remove(block_list, morte_list)
                morte_list = [ ]
                morte_list = pygame.sprite.Group()
                score = 0
    
                
        if score == 30:
            all_sprites_list.remove(player, block_list, morte_list)
            screen.fill(WHITE)
            livello_5()
            
        screen.fill(WHITE)
        all_sprites_list.draw(screen)
        screen.blit(scritta,(100, 20))
        pygame.display.flip()
        pygame.display.set_caption("Le avventure di Ben, azione : livello 1 " + "Score: " + str(score))
        clock.tick(60)  

def livello_5():
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
    scritta = font.render("SPARA I BLOCCHI, RIESCI AD ARRIVARE A 50 ? ", True, BLACK)

    clock = pygame.time.Clock()
    score = 0
    player.rect.y = 630

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()
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
                bullet.rect.x = player.rect.x + 25
                bullet.rect.y = player.rect.y + 25
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
        all_sprites_list.update()

        for bullet in bullet_list:
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1

            if bullet.rect.y < -5:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

            elif score == 50:
                all_sprites_list.remove(bullet, player, block)
                screen.fill(WHITE)
                livello_6()

        screen.fill(WHITE)
        all_sprites_list.draw(screen)
        screen.blit(scritta,(50, 20))
        pygame.display.flip()
        pygame.display.set_caption("Le avventure di Ben, azione : livello 2" + "  Score: " + str(score))
        clock.tick(60)     
    pygame.quit()

def livello_6():d
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen_width = 900
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    Eroe = pygame.image.load("img/eroe.png")
    EROE = pygame.transform.scale(Eroe,(60, 55))
    velocita = 2.5
    v = 0
    s = 0
    score = 0
    alive = False
    z = -1


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
    build()
    game_over = pygame.mixer.Sound("img/Game Over.wav")
    font = pygame.font.SysFont("brittanic", 25)
    scritta1 = font.render("Schiva più blocchi che puoi !!!", True, BLACK)
    scritta2 = font.render("Premi spazio ed il gioco inizierà!!!", True, BLACK)

    clock = pygame.time.Clock()

    player.rect.x = 150
    player.rect.y = (screen_height / 2) - 30


    while True: 
        if alive:
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
                if event.key == pygame.K_SPACE :
                    if alive == False:
                        alive = True
                        all_sprites_list.add(player)
                        z = 1
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

        if n == z:
            morte = Block(BLACK)
            morte.rect.x = 900
            morte.rect.y = random.randrange(5, 680)
            morte_list.add(morte)
            all_sprites_list.add(morte)

        for blocco in morte_list:
            morte_hit_list = pygame.sprite.spritecollide(player, morte_list, True)
            for giocatore in morte_hit_list:
                game_over.play()
                all_sprites_list.remove(morte_list, player)
                morte_list = [ ]
                morte_list = pygame.sprite.Group()

                alive = False
                velocita = 2
                v = 0
                score = 0
                s = 0
                z = -1
            if blocco.rect.x < 50:
                all_sprites_list.remove(blocco)		
                
        screen.fill(WHITE)
        all_sprites_list.draw(screen)
        plats.update()
        if not alive:
            screen.blit(scritta2,(100, 30))
        else:
            screen.blit(scritta1,(100, 30))
        pygame.display.flip()
        pygame.display.set_caption("Le avventure di Ben, azione : livello 3" + "  Score: " + str(score))
        clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exit()
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if pulsante1.collidepoint(pos) and pressed1:
            livello_4()
        if pulsante2.collidepoint(pos) and pressed1:
            livello_1()
    pygame.display.update()
    screen.blit(testo0, (160, 515))
    screen.blit(testo1, (158, 570))
    screen.blit(testo2, (620, 515))
    screen.blit(testo3, (620, 570))
    screen.blit(testo4, (250, 190))
    screen.blit(testo5, (250, 250))

'''
sfondo
cercare di ridurre al minimo gli errori di vs 
idee per migliorare:
    nel livello 6 una classifica sui tuoi score + data e ora
    tornare alla schermata quando finisci 
    pulsante per tornare alla schermata di scelta
'''
