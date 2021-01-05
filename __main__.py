import argparse
import csv
import json
import logging
import os.path
from configparser import ConfigParser
from os import mkdir

from simulation import Simulation

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="full_wolf_but_sheep_dead")

    parser.add_argument('-c', '--config',
                        metavar='FILE',
                        dest='config',
                        help='Gets default arguments of simulation from config FILE')

    parser.add_argument('-d', '--directory',
                        dest='directory',
                        type=str,
                        default='logs',
                        help='Choose directory where outcome files will be saved')

    parser.add_argument('-l', '--level',
                        dest='level',
                        type=int,
                        default=0,
                        help='Choose level of logging, must be a number'
                             ' (DEBUG - 10, INFO - 20, WARNING - 30, ERROR - 40, CRITICAL - 50')

    parser.add_argument('-r', '--rounds',
                        metavar='NUM',
                        type=int,
                        default=50,
                        dest='rounds_number',
                        help='Sets a number of rounds (NUM is an integer value)')

    parser.add_argument('-s', '--sheep',
                        metavar='NUM',
                        type=int,
                        default=15,
                        dest='sheep_number',
                        help='Sets a number of sheep (NUM is an integer value)')

    parser.add_argument('-w', '--wait',
                        action='store_true',
                        dest='wait',
                        help='If it is enabled, simulation will stop after each round and wait for pressing any key')

    args = parser.parse_args()

    if args.level != 0 and [10, 20, 30, 40, 50].__contains__(args.level) is False:
        raise ValueError('Level must be equal to either 10 (DEBUG), 20 (INFO), 30 (WARNING), 40 (ERROR) or 50 '
                         '(CRITICAL)')

    if args.directory != '' and args.directory[0] == '/':
        raise ValueError('Simulation data can be only saved in a subdirectory')

    directory = './' + args.directory + ('/' if args.directory != '' and args.directory[-1] != '/' else '')

    if os.path.exists(directory) is False:
        logging.debug('Directory "' + directory + '" does not exist, creating a new one')
        mkdir(directory)

    logging.basicConfig(filename=directory + 'chase.log',
                        level=args.level,
                        filemode='w',
                        format='%(asctime)s.%(msecs)03d [%(levelname)s] [%(module)s -> %(funcName)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    if args.rounds_number <= 0:
        logging.critical('Round number is less than 0!')
        raise ValueError('rounds number must be greater than 0')

    if args.sheep_number <= 0:
        logging.critical('Sheep number is less than 0!')
        raise ValueError('sheep number must be greater than 0')

    if args.config is None:
        init_pos_limit = 10
        sheep_move_dist = 0.5
        wolf_move_dist = 1.0
    else:
        if os.path.exists(args.config) is False:
            logging.error('File does not exists')
            raise IOError('File does not exists')

        config = ConfigParser()
        config.read(args.config)
        init_pos_limit = int(config['Terrain']['InitPosLimit'])
        sheep_move_dist = float(config['Movement']['SheepMoveDist'])
        wolf_move_dist = float(config['Movement']['WolfMoveDist'])

        if init_pos_limit <= 0:
            logging.critical('Init pos limit is less than 0!')
            raise ValueError('init pos limit must be greater than 0')
        if sheep_move_dist <= 0.0:
            logging.critical('Sheep move dist is less than 0!')
            raise ValueError('sheep move dist must be greater than 0')
        if wolf_move_dist <= 0.0:
            logging.critical('Wolf move dist is less than 0!')
            raise ValueError('wolf move dist must be greater than 0')

    simulation = Simulation(args.rounds_number, args.sheep_number, init_pos_limit, sheep_move_dist, wolf_move_dist,
                            args.wait)

    turns_data, alive_animals_data = simulation.simulate()

    logging.debug('Attempting to write pos.json file to ' + directory)
    with open(directory + 'pos.json', 'w') as pos:
        dump = json.dumps(turns_data)
        pos.write(dump.replace('},', '},\n'))
    logging.debug(directory + 'pos.json has been written successfully')

    logging.debug('Attempting to write alive.csv to ' + directory)
    with open(directory + 'alive.csv', 'w') as alive:
        writer = csv.writer(alive)
        writer.writerow(['Rounds number', 'Alive sheep number'])
        writer.writerow(alive_animals_data)
    logging.debug(directory + 'alive.csv has been written successfully')
