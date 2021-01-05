import logging
from abc import abstractmethod

from point import Point


class Animal:
    def __init__(self, position: Point, distance: float):
        logging.debug(f'position: {position}, distance: {distance}')
        self._position = position
        self._distance = distance

    @property
    def position(self) -> Point:
        return self._position

    @position.setter
    def position(self, position: Point):
        logging.debug(str(position))
        if isinstance(position, Point):
            self._position = position
        else:
            logging.error('position must be Point type!')
            raise TypeError('position must be Point type!')

    @property
    def distance(self) -> float:
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        logging.debug(distance)
        if isinstance(distance, float):
            self._distance = distance
        else:
            logging.error('distance must be float type!')
            raise TypeError('distance must be float type!')

    def move(self):
        logging.debug(f'{type(self).__name__} is moving from {self._position}')
        self._position += self.update_distance()

    @abstractmethod
    def update_distance(self):
        logging.error('move() method must be implemented!')
        raise NotImplementedError('move() method must be implemented!')
