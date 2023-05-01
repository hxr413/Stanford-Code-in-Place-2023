from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    cycle()
    move4()
    cycle()

def cycle():
    turn_left()
    put5beepers()
    turn_right()
    move4()
    turn_right()
    put5beepers()
    turn_left()

def put5beepers():
    for i in range(4):
        put_beeper()
        move()
    put_beeper()

def move4():
    for i in range(4):
        move()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()
