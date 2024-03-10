import spritesheet
import pygame

class Player(object):
    def __init__(self, x, y):
        spriteSheet = spritesheet.spritesheet('capybara_walking.png')
        self.x = x
        self.y = y
        self.width = 64
        self.height = 35
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.walkRight = spriteSheet.images_at([(0, 0, 64, 35), (64, 0, 64, 35), (128, 0, 64, 35), (192, 0, 64, 35), 
                                    (256, 0, 64, 35), (320, 0, 64, 35), (384, 0, 64, 35), (448, 0, 64, 35)], 'black')
        self.walkLeft = [pygame.transform.flip(image, True, False) for image in self.walkRight]
        
    def draw(self, display):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
            
        if not(self.standing):
            if self.left:
                display.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.right:
                display.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else: 
            if self.left:
                display.blit(self.walkLeft[0], (self.x, self.y))
            else:
                display.blit(self.walkRight[0], (self.x, self.y))

class Laser(object):
    def __init__(self, x, y, direction, display):
        spriteSheet = spritesheet.spritesheet('laser.png')
        self.x = x
        self.y = y
        self.direction = direction
        self.display = display
        self.vel = 10 * direction
        self.laserRight = spriteSheet.image_at((0, 0, 35, 15), 'black')
        self.laserLeft = pygame.transform.flip(spriteSheet.image_at((0, 0, 35, 15), 'black'), True, False) 
    
    def draw(self):
        if self.direction == -1:
            self.display.blit(self.laserLeft, (self.x, self.y))
        else:
            self.display.blit(self.laserRight, (self.x, self.y))