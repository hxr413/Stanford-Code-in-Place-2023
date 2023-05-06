from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

# put down a row of beeper
# turn around, return to where there is a beeper, pick it up
# turn around, repeat the process

def main():
    put_beeper_row()
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    while beepers_present():
        pick_end_beeper()
    # deal with midpoint
    turn_around()
    move()
    put_beeper()
    if not_facing_east():
        turn_around()


def put_beeper_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def pick_end_beeper():
    while front_is_clear():
        move()
    turn_around()
    while no_beepers_present():
        move()
    pick_beeper()
    move()


def turn_around():
    turn_left()
    turn_left()
    

if __name__ == '__main__':
    main()
