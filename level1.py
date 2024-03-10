import pygame
from player import Player, Laser
SCREENWIDTH, SCREENHEIGHT = 1280, 720
FPS = 60


class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
    def drawScreen(self, player, lasers):
        self.display.blit(pygame.image.load('background.png'), (0, 0))
        player.draw(self.display)
        for laser in lasers:
            laser.draw()
        pygame.display.update()
        

    def run(self):
        run = True
        player = Player(SCREENWIDTH / 2, 670)
        lasers = []
        shootLoop = 0
        """   GAME LOOP   """
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            
            """   LASERS   """
            
            if shootLoop >= 0:
                shootLoop += 1
            if shootLoop > 3:
                shootLoop = 0
                
            for laser in lasers:
                if (laser.x < SCREENWIDTH and laser.x > 0) and laser.y > 0:
                    laser.x += laser.vel
                else:
                    lasers.pop(lasers.index(laser))
            if keys[pygame.K_SPACE] and shootLoop == 0:
                if player.left:
                    direction = -1
                    if len(lasers) < 5 :
                        lasers.append(Laser(player.x - player.width / 2, round(player.y + player.height // 2) - 10, direction, self.display))
                else:
                    direction = 1
                    if len(lasers) < 5 :
                        lasers.append(Laser(player.x + player.width, round(player.y + player.height // 2) - 10, direction, self.display))
                shootLoop = 1
            
            # Hit logic here
            
            """   PLAYER MOVEMENT   """
            if keys[pygame.K_LEFT] and player.x - player.vel > 0:
                player.x -= player.vel
                player.left = True
                player.right = False
                player.standing = False
            elif keys[pygame.K_RIGHT] and player.x + player.width + player.vel < SCREENWIDTH:
                player.x += player.vel
                player.left = False
                player.right = True
                player.standing = False
            else:
                player.standing = True
                
            """   SPRINT    """
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                player.vel = 14 
            else:
                player.vel = 7
            
            """   JUMP   """
            if not(player.isJump): 
                if keys[pygame.K_UP]:
                    player.isJump = True
                    player.walkCount = 0
            else:
                if player.jumpCount >= -10:
                    neg = 1
                    if player.jumpCount < 0:
                        neg = -1
                    player.y -= (player.jumpCount ** 2) * 0.5 * neg
                    player.jumpCount -= 1
                else:
                    player.isJump = False
                    player.jumpCount = 10
                    
                    
            """ UPDATING SCREEN """
            self.drawScreen(player, lasers)
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
            
        self.gameStateManager.set_state('start')
            
            
        
    