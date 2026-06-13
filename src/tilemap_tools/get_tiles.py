import pygame
from ..objects.tile import Tile
from ..objects.player import Player
from ..globals import *
from .get_images import get_images


def get_tiles(tilemap):
    for layer in tilemap.tmx_data.visible_layers:
        if hasattr(layer,'data'):
            for x,y,img in layer.tiles():
                pos = pygame.Vector2(x * TILE_SIZE * TILE_SCALE, y * TILE_SIZE * TILE_SCALE)
                tilemap.visible_tiles.add(Tile(pos,img))

    for obj in tilemap.tmx_data.objects:
        pos = pygame.Vector2(obj.x,obj.y)
        images = get_images(
            obj.properties['obj_type'],
            obj.properties['images_variation']
            )
        if obj.properties['obj_type'] == 'player':
            tilemap.player.add(Player(pos,images))