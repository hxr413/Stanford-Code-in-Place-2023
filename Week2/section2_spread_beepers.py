from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?
"""


def main():
    move()
    while beepers_present():
        put_a_beeper()
        return_to_beeper()
        check_for_one_beeper()
    

def put_a_beeper():
    pick_beeper()
    while beepers_present():
        move()
    put_beeper()
    

def return_to_beeper():
    turn_around()
    while beepers_present():
        move()
    turn_around()


def check_for_one_beeper():
    move()
    pick_beeper()
    if no_beepers_present():
        put_beeper()
        turn_around()
        move()
        turn_around()
    else:
        put_beeper()
    

def turn_around():
    turn_left()
    turn_left()
    

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
