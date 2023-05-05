from karel.stanfordkarel import *

"""
Karel should paint the whole world, any color you want. 
As an extension, have karel randomly paint each corner.
"""


def main():
    while left_is_clear():
        move_one_row()
        return_to_start()
        move_to_next_row()
    move_one_row()

def move_one_row():
    while front_is_clear():
        paint()
        move()
    paint()
    

def return_to_start():
    turn_around()
    while front_is_clear():
        move()


def move_to_next_row():
    turn_right()
    move()
    turn_right()


def paint():
    if random():
        paint_corner("grey")
    else:
        paint_corner("salmon")


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
