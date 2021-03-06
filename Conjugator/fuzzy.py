"""
This application conjugates the verbs of multiple languages
Copyright (C) 2020 Shynn Lawrence, Govind Gnanakumar
See LICENSE for more information
"""

from Conjugator.Deutschconjugation import conjugator
from Conjugator import deutschCLI

import time
import os
import re
import csv
import platform

def allverbs() -> list:
    infinitives = []
    this_dir, this_filename = os.path.split(__file__)
    path = os.path.join(this_dir, "res/germanverbs.csv")
    with open(path, "r", newline="") as file:
        verblist = csv.reader(file)
        for row in verblist:
            try:
                infinitives.append(row[0])
            except:
                pass
    return infinitives


# Implemented by Govind Gnanakumar
def fuzzyfinder(user_input, collection) -> list:
    suggestions = []
    pattern = ".*?".join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]


def clearbreak(stdscr) -> None:
    curses.flushinp()
    stdscr.clear()
    return 1


def main(
    stdscr, text: str, ind: int, collections: list
) -> tuple([str, int, bool, bool]):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)

    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.clear()
    curses.cbreak()
    tempcount = 2
    if ind == -1:
        stdscr.addstr(text, curses.color_pair(3))
    else:
        stdscr.addstr(text)
    halt = False
    backspace = False
    while not halt:
        c = stdscr.getch()

        if c == 263:
            clearbreak(stdscr)
            backspace = True
            break

        if c == 258:
            ind += clearbreak(stdscr)
            break

        if c == 259 and ind >= -1:
            ind -= clearbreak(stdscr)
            break

        if c == 261:
            halt = bool(clearbreak(stdscr))
            break

        if tempcount == 2:
            x = fuzzyfinder(text, collection=collections)
            for val in x:
                try:
                    if ind == x.index(val):
                        stdscr.addstr("\n->" + val, curses.color_pair(3))
                    else:
                        stdscr.addstr("\n" + val, curses.color_pair(4))
                except:
                    break
            tempcount = 0

        elif c != -1:
            text += str(chr(c))
            tempcount = 1

        if tempcount == 1:
            stdscr.clear()
            if ind == -1:
                stdscr.addstr(text, curses.color_pair(3))
            else:
                stdscr.addstr(text)

            for val in fuzzyfinder(text, collection=collections):
                try:
                    stdscr.addstr("\n" + val, curses.color_pair(4))
                except:
                    break
            tempcount = 0

        time.sleep(0.1)

    return text, ind, halt, backspace


def lauf(coll: list) -> tuple([str, int]):
    text = ""
    ind2 = -1
    ind = 0
    halt = False
    while not halt:
        try:
            text, ind, halt, backspace = curses.wrapper(main, text, ind2, coll)
            if ind2 != ind:
                text = text
            elif ind2 == ind and backspace == True:
                text = text[:-1]
                ind = -1
            ind2 = ind
        except KeyboardInterrupt:
            break

    return text, ind2


def start() -> None:
    if platform.system() == "Windows":
        raise OSError(
            "You must be on a *nix system to use the fuzzy finder"
        )
    else:
        global curses
        import curses
    verbsCollections = allverbs()
    text, ind = lauf(verbsCollections)
    verb = str(fuzzyfinder(text, verbsCollections)[ind])
    print("You chose: " + verb)

    x = input("Type a pronoun here: ")
    y = input("Type the tense here: ")
    print(conjugator.conjugate(verb, x, y))
    
