from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    while left_is_clear():
        fill_row()
        return_outset()
        next_row()
    fill_row()


def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def return_outset():
    turn_around()
    while front_is_clear():
        move()


def next_row():
    turn_right()
    move()
    turn_right()
    

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
