from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    # handle width 1 (and only odd rows probably)
    if front_is_blocked():
        while left_is_clear():
            put_beeper()
            if left_is_clear():
                move_to_next_row()
            if left_is_clear():
                move_to_next_row()
        put_beeper()
    # handle width > 1 (due to the limitation of IDE, haven't been able to test with even columns)
    else:
        while left_is_clear():
            odd_row()
            if left_is_clear():
                move_to_next_row()
            even_row()
            if left_is_clear():
                move_to_next_row()
        if front_is_clear():
            odd_row()
    back_to_starting_point()


def pattern():
    put_beeper()
    move()
    if front_is_clear():
        move()


def odd_row():
    while front_is_clear():
        pattern()
    check_last_point()


def even_row():
    move()
    while front_is_clear():
        pattern()
    check_last_point()


def check_last_point():
    turn_around()
    move()
    if beepers_present():
        turn_around()
        move()
    else:
        turn_around()
        move()
        put_beeper()


def move_to_next_row():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    

def back_to_starting_point():
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
