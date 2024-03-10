import spritesheet
import pygame
ss = spritesheet.spritesheet('capybara_walking.png')
image = []
images = ss.images_at([(0, 0, 64, 35), (64, 0, 64, 35), (128, 0, 64, 35), (192, 0, 64, 35), (256, 0, 64, 35), (320, 0, 64, 35), (384, 0, 64, 35), (448, 0, 64, 35)], 'black')
screen = pygame.display.set_mode((500, 500))

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

man = player(300, 410, 64, 35)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("white")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel 
        man.left = True
        man.right = False
        man.standing = False 
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    
    
    
    
    pygame.display.update()
    """              windows shut               """
pygame.quit()