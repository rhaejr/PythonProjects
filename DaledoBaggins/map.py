import random
import pygame
from pytmx.util_pygame import load_pygame


class Map(object):

    def __init__(self, filename, gameDisplay, tile_size):

        self.filename = None
        self.data = None
        self.gameDisplay = gameDisplay
        self.tile_size = tile_size

        # Get the tile size from a tileset in our map. This is used to calculate the number of tiles
        # in a collision region.
        # self.tile_size = (0, 0)

        # Collision tiles in tmx object format
        self.collisions = []

        # Collision lines (player can walk in tiles, but cannot cross
        # from one to another) Items in this list should be in the
        # form of pairs, signifying that it is NOT possible to travel
        # from the first tile to the second (but reverse may be
        # possible, i.e. jumping) All pairs of tiles must be adjacent
        # (not diagonal)
        self.collision_lines = []
        self.npcs = []
        self.events = []
        self.signs = []
        # Initialize the map
        self.load(filename)


    def load(self, filename):
        # Load the tmx map data using the pytmx library.
        self.filename = filename
        # self.data = pytmx.TiledMap(filename)
        self.data = load_pygame(filename)  # , pixelalpha=True)
        # Get the map dimensions
        self.size = (self.data.width, self.data.height)
        # Get the tile size of the map
        # self.tile_size = (self.data.tilesets[0].tilewidth, self.data.tilesets[0].tileheight)
        # # Get the tile size of the map
        # self.tile_size = (self.data.tilesets[0].tilewidth, self.data.tilesets[0].tileheight)

        # Load all objects from the map file and sort them by their type.
        for obj in self.data.objects:

            if obj.type == 'npc':
                self.npcs.append(obj)

            if obj.type == 'collision':
                # self.collisions.append(obj)
                self.collisions.append((int(obj.x / self.tile_size), int(obj.y / self.tile_size)))

            elif obj.type == 'collision-line':
                self.collision_lines.append(obj)

            elif obj.type == 'event':
                if obj.name == 'start':
                    self.start = (int(obj.x / self.tile_size), int(obj.y / self.tile_size))
                elif obj.name == 'exit':
                    self.events.append((int(obj.x / self.tile_size), int(obj.y / self.tile_size)))
                elif obj.name == 'sign':
                    self.signs.append((int(obj.x / self.tile_size), int(obj.y / self.tile_size)))
                conds = []
                acts = []

                # Conditions & actions are stored as Tiled properties.
                # We need to sort them by name, so that "act1" comes before "act2" and so on..
                keys = sorted(obj.properties.keys())

                for k in keys:
                    if k.startswith('cond'):
                        words = obj.properties[k].split(' ', 2)

                        # Conditions have the form 'operator type parameters'.
                        operator, type = words[0:2]

                        args = ''
                        if len(words) > 2:
                            args = words[2]

                        conds.append({
                            'type': type,
                            'parameters': args,
                            'x': int(obj.x / self.tile_size[0]),
                            'y': int(obj.y / self.tile_size[1]),
                            'width': int(obj.width / self.tile_size[0]),
                            'height': int(obj.height / self.tile_size[1]),
                            'operator': operator
                        })
                    elif k.startswith('act'):
                        acts.append(obj.properties[k].split(' ', 1))

                self.events.append({'conds': conds, 'acts': acts, 'id': obj.id})

    def draw_map(self):
        for layer in self.data.layers[:2]:
            for x, y, image in layer.tiles():
                self.gameDisplay.blit(image, (x * self.tile_size, y * self.tile_size))
        for o in self.data.objects:
            if o.image != None:
                self.gameDisplay.blit(o.image, (o.x, o.y))

    def draw_forground(self):
        layer = self.data.layers[2]
        for x, y, image in layer.tiles():
            self.gameDisplay.blit(image, (x * self.tile_size, y * self.tile_size))