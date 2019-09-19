#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Roll some dice on the command line.
    Author: Jake Scott
    Date: 9/19/2019
"""

import argparse
import random

VERSION = '0.1'

# roll one die
def roll(n):
    return random.randint(1,n)

# TODO: validate command line input
def validate(D):
    pass

def init_argparser():
    # init argparser
    parser = argparse.ArgumentParser(description = 'Roll some dice on the command line.')
    parser.add_argument('dice', metavar='D', type=str, nargs='+', help='Dice to be rolled (e.g. d20 or 2d6)')
    parser.add_argument('-V', '--version', action='version', version='pyroller version {}'.format(VERSION))
    parser.add_argument('-v', '--verbose', help='show all dice rolls', action='store_true')

    # read arguments form command line
    return parser.parse_args()

def main():
    random.seed()

    args = init_argparser()

    rolls = []

    for die in args.dice:
        if args.verbose:
            print('Rolling {}...'.format(die))

        n = die.split('d')[0]
        d = int(die.split('d')[1])

        for i in range(0, int(n) if n else 1):
            tmp = roll(d)
            if args.verbose:
                print(tmp, end = " ")
            rolls.append(tmp)

        if args.verbose:
            print()

    if args.verbose:
        print("Total:")
    print(sum(rolls))

if __name__ == "__main__":
    main()
