import spritesheet
import pygame

class Player(object):
    def __init__(self, x, y):
        self.restart(x, y)
        
    def update(self, keys, world, enemies, lava, game_over): 
        dx = 0
        dy = 0
        SCREENWIDTH = 1280
        
        if game_over == False:
            """   PLAYER MOVEMENT   """
            if keys[pygame.K_LEFT] and self.rect.x - self.x_vel > 0:
                dx -= self.x_vel
                self.left = True
                self.right = False
                self.standing = False
            elif keys[pygame.K_RIGHT] and self.rect.x + self.width + self.x_vel < SCREENWIDTH:
                dx += self.x_vel
                self.left = False
                self.right = True
                self.standing = False
            else:
                self.standing = True
                
            """   SPRINT    """
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.x_vel = 14 
            else:
                self.x_vel = 8
            
            """   JUMP   """
            if keys[pygame.K_UP] and self.isJump == False and self.in_air == False:
                self.y_vel = -17
                self.isJump = True
            if keys[pygame.K_UP] == False:
                self.isJump = False
            
                    
            self.y_vel += 1
            if self.y_vel > 10:
                self.y_vel = 10
            dy += self.y_vel
            
            """ TERRAIN COLLISION """
            self.in_air = True
            for tile in world.tiles:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.y_vel < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.y_vel = 0
                    elif self.y_vel >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.y_vel = 0
                        self.in_air = False
            
            """ ENEMY/LAVA COLLISION """
            if pygame.sprite.spritecollide(self, enemies, False):
                game_over = True
            
            if pygame.sprite.spritecollide(self, lava, False):
                game_over = True
            
            self.rect.x += dx
            self.rect.y += dy
        elif game_over:
            self.image = self.dead
            if self.rect.y > 200:
                self.rect.y -= 5 
        
        return game_over
        
    def draw(self, display, game_over):
        if game_over:
            display.blit(self.image, (self.rect.x, self.rect.y))
            return
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                display.blit(self.walkLeft[self.walkCount // 3], (self.rect.x, self.rect.y))
                self.walkCount += 1
            if self.right:
                display.blit(self.walkRight[self.walkCount // 3], (self.rect.x, self.rect.y))
                self.walkCount += 1
        else:
            if self.left:
                display.blit(self.walkLeft[0], (self.rect.x, self.rect.y))
            else:
                display.blit(self.walkRight[0], (self.rect.x, self.rect.y))
        
    def restart(self, x, y):
        spriteSheet = spritesheet.spritesheet('img/capybara_walking.png')
        self.width = 64
        self.height = 35
        self.x_vel = 8
        self.y_vel = 0
        self.isJump = False
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.walkRight = spriteSheet.images_at([(0, 0, 64, 35), (64, 0, 64, 35), (128, 0, 64, 35), (192, 0, 64, 35), 
                                    (256, 0, 64, 35), (320, 0, 64, 35), (384, 0, 64, 35), (448, 0, 64, 35)], 'black')
        self.walkLeft = [pygame.transform.flip(image, True, False) for image in self.walkRight]
        self.image = self.walkRight[self.walkCount]
        self.dead = pygame.image.load('img/dead.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.in_air = True
        
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, display):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/laser.png')
        self.direction = direction
        self.display = display
        self.vel = 10 * direction
        self.laserRight = self.image
        self.laserLeft = pygame.transform.flip(self.image, True, False) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, enemies, world):
        """ ENEMY/LAVA COLLISION """
        hit_enemies = pygame.sprite.spritecollide(self, enemies, False)
        for enemy in hit_enemies:
            print("Hit!")
            enemy.hit(self.display)  # Call the method in the Enemy class for handling the hit.
        if hit_enemies:
            self.kill()  # Remove the laser when it hits an enemy.

        hit_tiles = pygame.sprite.spritecollide(self, world.tiles_group, False)
        for tile in hit_tiles:
            self.kill()  
        
    
    def draw(self):
        if self.direction == -1:
            self.display.blit(self.laserLeft, (self.rect.x, self.rect.y))
        else:
            self.display.blit(self.laserRight, (self.rect.x, self.rect.y))
            