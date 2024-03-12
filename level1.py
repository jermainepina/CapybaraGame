import pygame
from os import path
import pickle
from player import Player, Laser
from world import World
from button import Button
import spritesheet
SCREENWIDTH, SCREENHEIGHT = 1280, 720
FPS = 60


class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.level = 1
        
    def run(self):
        run = True
        if path.exists(f'level_data/level{self.level}_data'):
            pickle_in = open(f'level_data/level{self.level}_data', 'rb')
            world_data = pickle.load(pickle_in)
               
            
        lava = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        lasers = pygame.sprite.Group()
        world = World(world_data, enemies, lava)
        player = Player(40, SCREENHEIGHT - 75)
        shootLoop = 0
        game_over = False
        restart_button = Button(SCREENWIDTH // 2 - 50, SCREENHEIGHT // 2, pygame.image.load('img/restart.png'))
        
        
        
        """   GAME LOOP   """
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            
            if game_over == False:
                enemies.update()
            
            """   LASERS   """
            if shootLoop >= 0:
                shootLoop += 1
            if shootLoop > 3:
                shootLoop = 0
                
            # Create a list to store lasers that need to be removed
            lasers_to_remove = []

            # Inside the game loop
            for laser in lasers:
                laser.update(enemies, world)
                
                if (laser.rect.x < SCREENWIDTH and laser.rect.x > 0) and laser.rect.y > 0:
                    laser.rect.x += laser.vel
                else:
                    lasers_to_remove.append(laser)

            # Remove lasers that are off-screen
            for laser in lasers_to_remove:
                lasers.remove(laser)
                    
            if keys[pygame.K_SPACE] and shootLoop == 0:
                if player.left:
                    direction = -1
                    if len(lasers) < 5 :
                        new_laser = Laser(player.rect.x - player.width / 2, round(player.rect.y + player.height // 2) - 10, direction, self.display)
                        lasers.add(new_laser) 
                else:
                    direction = 1
                    if len(lasers) < 5 :
                        new_laser = Laser(player.rect.x + player.width, round(player.rect.y + player.height // 2) - 10, direction, self.display)
                        lasers.add(new_laser) 
                shootLoop = 1
            
            """ UPDATING SCREEN """
            game_over = player.update(keys, world, enemies, lava, game_over)
            self.display.blit(pygame.image.load('img/background.png'), (0, 0))
            
            world.draw(self.display)
            lava.draw(self.display)
            enemies.draw(self.display)
            player.draw(self.display, game_over)
            for laser in lasers:
                laser.draw()
                
            if game_over == True:
                if restart_button.draw(self.display):
                    player.restart(40, SCREENHEIGHT - 75)
                    game_over = False
                
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(FPS)
        self.gameStateManager.set_state('start')
        
        
        

                
        
        
        


            
        
        
    