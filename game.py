import pygame
import sys
import spritesheet
from player import Player, Laser
from level1 import Level1
from level2 import Level2
from button import Button
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
        self.level1 = Level1(self.screen, self.gameStateManager)
        self.level2 = Level2(self.screen, self.gameStateManager)
        self.states = {'start': self.start, 'level1': self.level1, 'level2': self.level2}
    
        
        
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
        start = Button(SCREENWIDTH // 2 - 150, SCREENHEIGHT // 2 + 100, pygame.image.load('img/start.png'))
        exit = Button(SCREENWIDTH // 2 + 50, SCREENHEIGHT // 2 + 100, pygame.image.load('img/exit.png'))
       
        self.display.blit(pygame.image.load('img/background.png'), (0, 0))
        if start.draw(self.display):
             self.gameStateManager.set_state('level1')
        elif exit.draw(self.display):
            pygame.quit()
            sys.exit()
        
       
    
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