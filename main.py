import pygame, sys
from src.globals import *
from src.tilemap import Tilemap
from src.player_controller import PlayerController
from src.physic_manager import PhysicManager


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.inputs = {pygame.K_LEFT : False, pygame.K_RIGHT : False, pygame.K_UP : False, pygame.K_DOWN : False, pygame.K_SPACE : False}
        self.tilemap = Tilemap()
        self.physic_manager = PhysicManager(self.tilemap)

    def handle_events(self,event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type in [pygame.KEYUP, pygame.KEYDOWN]:
            self.handle_key_events(event) 

    def handle_key_events(self, event):
        if event.type == pygame.KEYDOWN:
            for inpput_key in self.inputs:
                if event.key == inpput_key:
                    self.inputs[inpput_key] = True

        if event.type == pygame.KEYUP:
            for inpput_key in self.inputs:
                if event.key == inpput_key:
                    self.inputs[inpput_key] = False

    def handle_inputs(self):
        self.inputs = {k:False for k in self.inputs}

    def fixed_update(self):
        self.physic_manager.fixed_update()

    def update(self,dt):
        self.tilemap.all_sprites.update(dt)

    def draw(self,alpha):
        for sprite in self.tilemap.all_sprites:
            sprite.draw(self.screen,alpha)
        self.display.blit(pygame.transform.scale(self.screen,self.display.get_size()),(0,0))
        pygame.display.flip()

    def run(self):
        accumulator = 0
        while True:
            dt = self.clock.tick(FPS) / 1000
            dt = min(dt,0.1)
            accumulator += dt

            while accumulator >= dt:
                for event in pygame.event.get() : self.handle_events(event)
                self.handle_inputs()
                self.fixed_update()
                accumulator -= 1/FIXED_TPS

            alpha = accumulator / dt

            self.update(dt)
            self.draw(alpha)

game = Game()
game.run()