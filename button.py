import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.clicked = False
        
    def draw(self, display):
        is_clicked = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                is_clicked = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0]:
            self.clicked = False
        
        display.blit(self.image, self.rect)
        
        return is_clicked