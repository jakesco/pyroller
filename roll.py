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
    parser = argparse.ArgumentParser()
    parser.add_argument('dice', metavar='D', type=str, nargs='*', help='Dice to be rolled (e.g. d12, 2d6, etc). A d20 will be rolled if no arguments given.')
    parser.add_argument('-V', '--version', action='version', version='pyroller version {}'.format(VERSION))
    parser.add_argument('-v', '--verbose', help='show all dice rolls', action='store_true')
    parser.add_argument('-m', '--modifier', type=int, nargs=1, help='adds MODIFIER to result', action='store')

    # read arguments form command line
    return parser.parse_args()

def main():
    random.seed()

    args = init_argparser()

    rolls = []

    if len(args.dice) < 1:
        args.dice = ['d20']

    for die in args.dice:
        if args.verbose:
            print('Rolling {}...'.format(die))

        n, d = die.split('d')

        for i in range(0, int(n) if n else 1):
            tmp = roll(int(d))
            if args.verbose:
                print(tmp, end = " ")
            rolls.append(tmp)

        if args.verbose:
            print()

    total = sum(rolls)

    if args.modifier:
        total += args.modifier[0]

    if args.verbose:
        print("Total:")
    print(total)

if __name__ == "__main__":
    main()
