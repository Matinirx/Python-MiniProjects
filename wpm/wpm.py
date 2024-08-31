import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):

    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Type Test")
    stdscr.addstr("\nPress any Key to Begin")
    stdscr.refresh()
    stdscr.getkey()
        
def display_test(stdscr, target, current, wpm=0):   
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WMP: {wpm}")
    
    for i, char in enumerate(current):
        currect_char = target[i]
        color =  curses.color_pair(1)

        if char != currect_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def load_text():
    with open("text.txt", "r") as text:
        lines = text.readlines()

    return random.choice(lines).strip()

def wmp_test(stdscr):
    target_text = load_text()
    curr_text = []
    wpm = 0
    st_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - st_time, 1)
        wpm = round((len(curr_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_test(stdscr, target_text, curr_text, wpm)
        stdscr.refresh()
        
        try:
            key = stdscr.getkey()
        except:
            continue

        if "".join(curr_text) == target_text:
            stdscr.nodelay(False)
            break

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\f7f"):
            if len(curr_text) > 0:
                curr_text.pop()
        elif len(curr_text) < len(target_text):
            curr_text.append(key)
    
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wmp_test(stdscr)
        stdscr.addstr(2, 0, "You Completed the Text! Press any key to continue...")
        
        key = stdscr.getkey()
        if ord(key) == 27:
            break
        else:
            continue

wrapper(main)