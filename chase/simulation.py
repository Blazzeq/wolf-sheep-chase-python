import logging
from typing import List

from chase.animal import Animal
from chase.sheep import Sheep
from chase.wolf import Wolf


class Simulation:
    def __init__(self, rounds: int, sheep_number: int, init_pos_limit: float, sheep_move_dist: float,
                 wolf_move_dist: float, wait: bool):
        logging.debug(f'rounds: {rounds}, sheep_number: {sheep_number}, init_pos_limit: {init_pos_limit},'
                      f'sheep_move_dist: {sheep_move_dist}, wolf_move_dist: {wolf_move_dist}, wait: {wait}')
        logging.info('Initialize of the simulation')

        self.rounds = rounds
        self._animal = []

        for _ in range(sheep_number):
            s = Sheep(init_pos_limit, sheep_move_dist)
            logging.info(f'Sheep #{_} start position at {s.position}')
            self.animal.append(s)

        self._wolf = Wolf(wolf_move_dist, self.animal)
        logging.info(f'Wolf start position at {self._wolf.position}')
        self.wait = wait

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, animal):
        if isinstance(animal, List) is False:
            raise TypeError('sheep must be List type!')
        else:
            for _ in animal:
                if isinstance(_, Animal) is False:
                    raise TypeError('animal list can include only Animal type!')
        self._animal = animal

    @property
    def wolf(self):
        return self._wolf

    @wolf.setter
    def wolf(self, wolf):
        if isinstance(wolf, Wolf) is False:
            raise TypeError('wolf must be Wolf type!')
        self._wolf = wolf

    def get_alive_animals(self):
        result = []
        for _animal in self.animal:
            if _animal is not None:
                result.append(_animal)
        return result

    def are_sheep_alive(self) -> bool:
        alive = len(self.get_alive_animals()) != 0
        logging.debug(f'returns: {alive}')
        return alive

    def simulate(self) -> [List, List]:
        turn = 0
        json = []
        csv = []

        logging.info('Start of the simulation\n')
        print('Start of the simulation\n')

        while turn != self.rounds and self.are_sheep_alive():
            logging.info(f'Round #{turn} has started')
            print(f'Round #{turn}')

            for _ in self.animal:
                if _ is not None:
                    _.move()
                    logging.info(f'Sheep #{self.animal.index(_)} moved to {_.position}')

            self.wolf.move()
            logging.info(f'Wolf moved to {self.wolf.position}')

            print('#######')
            print(self.wolf)
            remaining_message = str(len(self.get_alive_animals())) + ' sheep are alive'
            logging.info(remaining_message)
            print(remaining_message)
            print('#######\n')

            logging.debug('Saving animal positions')
            animal_positions = []
            for _ in self.animal:
                animal_positions.append([_.position.x, _.position.y] if _ is not None else None)

            json.append({
                'round_no': turn,
                'wolf_pos': [self.wolf.position.x, self.wolf.position.y],
                'sheep_pos': animal_positions
            })

            csv.append([turn, len(self.get_alive_animals())])

            logging.info(f'Round #{turn} has ended\n')

            if self.wait:
                input()

            turn += 1

        logging.info('End of the simulation')
        print('End of the simulation')

        return [json, csv]
