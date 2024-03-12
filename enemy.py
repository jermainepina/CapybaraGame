import pygame
import spritesheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.count = 1
        self.hit_animation_frames = spritesheet.spritesheet('img/explosion.png').images_at(
            [(0, 0, 96, 96), (96, 0, 96, 96), (192, 0, 96, 96), (288, 0, 96, 96), 
             (384, 0, 96, 96), (480, 0, 96, 96), (576, 0, 96, 96), (672, 0, 96, 96), 
             (768, 0, 96, 96), (864, 0, 96, 96), (960, 0, 96, 96), (1056, 0, 96, 96)], 'black')
        self.hit_animation_index = 0
        self.hit_animation_speed = 10
        self.hit_once = False

    def update(self):
        self.rect.x += self.direction
        self.count += 1
        if abs(self.count) > 50:
            self.direction *= -1
            self.count *= -1

    def hit(self, display):
        if not self.hit_once:
            self.kill()
            for frame in self.hit_animation_frames:
                display.blit(frame, (self.rect.x - 40, self.rect.y + 40))
                pygame.display.flip()
                pygame.time.delay(self.hit_animation_speed)
            
            self.hit_once = True
