import logging
from math import sqrt, pow
from typing import List, Tuple

from animal import Animal
from point import Point


class Wolf(Animal):
    def __init__(self, wolf_move_dist: float, animal: List[Animal]):
        super().__init__(Point(), wolf_move_dist)
        self.animal = animal

    def look_back(self, animal: List[Animal]) -> Tuple[Animal, bool, float]:
        dist = []
        alive_animals = []
        for _animal in animal:
            if _animal is not None:
                alive_animals.append(_animal)
                dist.append(sqrt(
                    pow(self.position.x - _animal.position.x, 2) +
                    pow(self.position.y - _animal.position.y, 2)
                ))

        dist_to_victim = min(dist)
        victim = alive_animals[dist.index(dist_to_victim)]

        return victim, dist_to_victim <= self.distance, dist_to_victim

    def update_distance(self) -> Point:

        victim, can_be_killed, dist_to_victim = self.look_back(self.animal)
        victim_index = self.animal.index(victim)

        if can_be_killed:
            kill_message = f'Sheep #{victim_index} has been killed'
            logging.info(kill_message)
            print(kill_message)
            self.position.set(victim.position)
            self.animal[victim_index] = None
            return Point()

        chase_message = f'Wolf is chasing sheep #{victim_index}'
        logging.info(chase_message)
        print(chase_message)

        result = self.distance / (dist_to_victim - self.distance)

        return Point(result * (victim.position.x - self.position.x) / (1 + result),
                     result * (victim.position.y - self.position.y) / (1 + result))

    def __str__(self):
        return f'Wolf is at {self.position}'
