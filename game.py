import pygame
import sys
import spritesheet
from player import Player, Laser
from level1 import Level1
pygame.init()
FONT = pygame.font.SysFont("arial", 30)
SCREENWIDTH, SCREENHEIGHT = 1280, 720
FPS = 60


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
    
        self.gameStateManager = gameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level1(self.screen, self.gameStateManager)
    
        self.states = {'start': self.start, 'level1': self.level}
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
    
            self.states[self.gameStateManager.get_state()].run()   
                    
            pygame.display.update()
            self.clock.tick(27)
            

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        start_text = FONT.render("start", 1, "white")
        self.display.fill('red')
        self.display.blit(start_text, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('level1')
    
class gameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state
    
    
            
if  __name__ == '__main__':
    game = Game()
    game.run()