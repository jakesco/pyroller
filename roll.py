#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Roll some dice on the command line. """

import argparse
import random

def roll(n):
    return random.randint(1,n)

def main():
    random.seed()

    # init argparser
    parser = argparse.ArgumentParser(description = 'Roll some dice on the command line.')
    parser.add_argument('dice', metavar='D', type=str, nargs='+', help='Dice to be rolled (e.g. d20 2d6)')
    parser.add_argument('-v', '--version', help='show program version', action='store_true')

    # read arguments form command line
    args = parser.parse_args()

    if args.version:
        print("pyroller version 0.1")

    rolls = []
'''
    #n = sys.argv[1].split('d')[0]
    #d = int(sys.argv[1].split('d')[1])

    for i in range(0, int(n) if n else 1):
        rolls.append(roll(d))

    print(rolls, "=", sum(rolls))
'''
if __name__ == "__main__":
    main()
