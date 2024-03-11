import pygame

class World:
    def __init__(self, data):
        self.data = data
        self.tiles = []
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
                if tile == 2:
                    img = pygame.image.load('img/grass.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                if tile == 3:
                    img = pygame.image.load('img/lava.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                if tile == 4:
                    img = pygame.image.load('img/wood.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                if tile == 5:
                    img = pygame.image.load('img/exit.png')
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tiles.append((img, img_rect))
                col_count += 1
            row_count += 1
        
        
    def draw(self, display):
        self.display = display
        for tile in self.tiles:
            self.display.blit(tile[0], tile[1])