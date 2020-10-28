#!/usr/bin/env python3

# script that quickly jumps up the file tree

import os
import argparse
import subprocess


def jumper(number_jumps):
    if number_jumps > 0:
        for _ in range(number_jumps):
            if os.getcwd() != os.path.expanduser("/"):
                os.chdir("..")
                current_dir = os.getcwd()
                # sub
            else:
                break


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "number_jumps",
        type=int,
        default=2,
        help="jump up the file tree by number of jumps specified, default is 2",
    )
    parser.add_argument(
        "-v", "--verbosity", action="count", default=0, help="display final directory"
    )
    args = parser.parse_args()
    number_jumps = args.number_jumps
    return args, number_jumps


if __name__ == "__main__":
    args, number_jumps = get_args()

    jumper(number_jumps)

    if args.verbosity >= 2:
        print(os.getcwd())
