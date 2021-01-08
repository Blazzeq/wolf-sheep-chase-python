import logging
from enum import Enum, auto
from math import floor
from random import uniform

from chase.animal import Animal
from chase.point import Point


class WindRose(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Sheep(Animal):
    sides = {
        WindRose.NORTH: [0, 1],
        WindRose.SOUTH: [0, -1],
        WindRose.EAST: [1, 0],
        WindRose.WEST: [-1, 0]
    }

    def __init__(self, init_pos_limit: float = 10, sheep_move_dist: float = 0.5):
        super().__init__(Point(uniform(-init_pos_limit, init_pos_limit),
                               uniform(-init_pos_limit, init_pos_limit)),
                         sheep_move_dist)
        logging.debug(f'init_pos_limit: {init_pos_limit}, sheep_move_dist: {sheep_move_dist}')

    def update_distance(self):
        side = [WindRose.NORTH,
                WindRose.SOUTH,
                WindRose.WEST,
                WindRose.EAST][floor(uniform(0, 4))]
        logging.info(f'Sheep is headed {side.name}')
        updated_point = Point(self.distance * Sheep.sides[side][0],
                              self.distance * Sheep.sides[side][1])
        logging.debug(f'returns: {updated_point}')
        return updated_point
