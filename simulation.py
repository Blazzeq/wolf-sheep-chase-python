import logging
from msvcrt import getch
from typing import List

from animal import Animal
from sheep import Sheep
from wolf import Wolf


class Simulation:
    def __init__(self, turns: int, sheep_number: int, init_pos_limit: float, sheep_move_dist: float,
                 wolf_move_dist: float, wait: bool):

        self.turns = turns
        self._animal = []

        for _ in range(sheep_number):
            s = Sheep(init_pos_limit, sheep_move_dist)
            logging.info('Sheep #' + str(_) + 'start position' + str(s.position))
            self.animal.append(s)

        self._wolf = Wolf(wolf_move_dist, self.animal)
        logging.info(str(self.wolf))
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
        killed = 0
        for _animal in self.animal:
            if _animal is None:
                killed += 1
        return killed != len(self.animal)

    def simulate(self) -> [List, List]:
        turn = 0
        json = []
        csv = []

        logging.info('Start of the simulation\n')
        print('Start of the simulation\n')

        while turn != self.turns and self.are_sheep_alive():
            logging.info('Tour #' + str(turn) + 'has started')
            print('Tour #' + str(turn))

            for _ in self.animal:
                if _ is not None:
                    logging.info('Sheep #' + str(self.animal.index(_)) + ' is moving')
                    _.move()
                    logging.info('Its position is' + str(_.position))

            self.wolf.move()

            print('#######')
            print(self.wolf)
            remaining_message = str(len(self.get_alive_animals())) + ' animals are alive'
            logging.info(remaining_message)
            print(remaining_message)
            print('#######\n')

            animal_positions = []
            for _ in self.animal:
                animal_positions.append([_.position.x, _.position.y] if _ is not None else None)

            json.append({
                'turn number': turn,
                'wolf position': [self.wolf.position.x, self.wolf.position.y],
                'sheep positions': animal_positions
            })

            csv.append([turn, len(self.get_alive_animals())])

            turn += 1

            if self.wait:
                getch()

        logging.info('End of the simulation')
        print('End of the simulation')

        return [json, csv]
