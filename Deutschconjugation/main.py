import time
import curses
import fuzzy as fzf
import csvinterface

collections = csvinterface.verbreturns()

def clearbreak(stdscr):
    curses.flushinp()
    stdscr.clear()
    return 1

def main(stdscr, text: str, ind: int, collections:list) -> str:
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
            x = fzf.fuzzyfinder(text, collection=collections)
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

            for val in fzf.fuzzyfinder(text, collection=collections):
                try:
                    stdscr.addstr("\n" + val, curses.color_pair(4))
                except:
                    break
            tempcount = 0

        time.sleep(0.1)

    return text, ind, halt, backspace

def lauf(coll:list):
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

text, ind = lauf(collections)

print("You chose: " + str(fzf.fuzzyfinder(text, collections)[ind]))