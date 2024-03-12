import pygame
from enemy import Enemy
class World:
    def __init__(self, data, enemies, lava_group):
        self.data = data
        self.tiles = []
        self.tiles_group = pygame.sprite.Group() 
        tile_size = 40
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.image.load('img/dirt.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                    self.tiles_group.add(Tile(img_rect.x, img_rect.y, img))
                if tile == 2:
                    img = pygame.image.load('img/grass.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                    self.tiles_group.add(Tile(img_rect.x, img_rect.y, img))
                if tile == 3:
                    lava = Lava(col_count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
                if tile == 4:
                    img = pygame.image.load('img/wood.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                    self.tiles_group.add(Tile(img_rect.x, img_rect.y, img))
                if tile == 5:
                    img = pygame.image.load('img/exit.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                if tile == 6:
                    enemy = Enemy(col_count * tile_size, row_count * tile_size)
                    enemies.add(enemy)
                col_count += 1
            row_count += 1
        
        
    def draw(self, display):
        self.display = display
        for tile in self.tiles:
            self.display.blit(tile[0], tile[1])

    def update_tiles(self):
        self.tiles_group.update()
         
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y     
            
class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/lava.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.count = 1
            
class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/exit.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
