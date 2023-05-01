from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    move_twice()
    pick_beeper()
    move()
    turn_left()
    move_twice()
    put_beeper()
    turn_around()
    move_twice()
    turn_right()
    move_twice()
    move()
    turn_around()

    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def turn_around():
    turn_left()
    turn_left()
    
    
def move_twice():
    move()
    move()

    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
