from karel.stanfordkarel import *

# File: warmup.py
# -----------------------------
# The warmup program defines a "main"
# function which currently just has one
# Command. Add two more commands to make karel: move(), pick_beeper(), move()

def main():
    # TODO: your code here
    for i in range(3):
        one_wave()
        move()
        move()
    one_wave()

    
def one_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    # return to bottom line
    turn_around()
    move()
    turn_left()

    
def turn_right():
    for i in range(3):
        turn_left()

        
def turn_around():
    for i in range(2):
        turn_left()
        
        
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
