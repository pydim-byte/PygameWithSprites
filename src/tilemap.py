import pygame,os
from pytmx import load_pygame
from .globals import *
from .objects.tile import Tile
from .objects.player import Player
from .objects.barrier import Barrier
from .tilemap_tools.get_tiles import get_tiles



class Tilemap:
    def __init__(self,level_num=1):
        self.all_sprites = pygame.sprite.Group()
        self.visible_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.skull = pygame.sprite.GroupSingle()
        self.hearts = pygame.sprite.Group()
        self.skull_eyes = pygame.sprite.Group()
        self.xmarks = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.barriers = []
        self.static_objects = []
        self.dynamic_objects = []

        if os.path.isfile(f'assets/tilemap/level_{level_num}.tmx'):
            self.tmx_data = load_pygame(f'assets/tilemap/level_{level_num}.tmx')
            get_tiles()