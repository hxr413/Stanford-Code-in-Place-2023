from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # TODO: your code here
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, 'blue')
    goal = canvas.create_rectangle(CANVAS_WIDTH - 2 * SIZE, CANVAS_HEIGHT - 2 * SIZE, CANVAS_WIDTH - SIZE, CANVAS_HEIGHT - SIZE, 'salmon')
    
    while True:
        # move player
        x_move = SIZE
        y_move = 0
        
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            x_move = -SIZE
            y_move = 0
        if key == 'ArrowRight':
            x_move = SIZE
            y_move = 0
        if key == 'ArrowUp':
            x_move = 0
            y_move = -SIZE
        if key == 'ArrowDown':
            x_move = 0
            y_move = SIZE
        
        canvas.move(player, x_move, y_move)
        
        # determine if hit goal
        x_player = canvas.get_left_x(player)
        y_player = canvas.get_top_y(player)
        
        x_goal = canvas.get_left_x(goal)
        y_goal = canvas.get_top_y(goal)
        
        # change goal when hit
        if (x_player == x_goal) and (y_player == y_goal):
            x_count = random.randint(0, CANVAS_WIDTH / SIZE - 1)
            y_count = random.randint(0, CANVAS_HEIGHT / SIZE - 1)
            x_start = x_count * SIZE
            y_start = y_count * SIZE
            canvas.moveto(goal, x_start, y_start)
        
        time.sleep(DELAY)


if __name__ == '__main__':
    main()
