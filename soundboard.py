#!/usr/bin/env python3

import argparse
import configparser
import logging
import subprocess

import serial

logger = logging.getLogger(__name__)


def main(port, sounds):
    ser = serial.Serial(port, 9600, parity='N', stopbits=1, timeout=1)
    logger.info(f'Opened {ser}')
    while True:
        press = ser.read(4)
        logger.debug(f'Received {press=}')
        code = press.decode('ascii').replace('\r', '').replace('\n', '')
        logger.debug(f'{code=}')

        if len(code) == 0:
            pass
        elif code in sounds.keys():
            p = subprocess.Popen(['play', sounds[code]])
            logger.debug(f'Spawned {p.pid=}')
        else:
            logger.info(f'{code=} not handled')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='/dev/ttyUSB0')
    parser.add_argument('-c', '--config-path', default='soundboard.ini')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logger.debug(args)

    config = configparser.ConfigParser()
    config.read(args.config_path)
    logger.debug(config)

    main(args.port, config['sounds'])
