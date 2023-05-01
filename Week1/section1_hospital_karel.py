from karel.stanfordkarel import *


def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        if front_is_clear():
            move()


def build_hospital():
    turn_left()
    for i in range (2):
        build()
    turn_right()
    build()
    turn_right()
    for i in range(2):
        build()
    turn_left()


def build():
    move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()
    

if __name__ == '__main__':
    main()
