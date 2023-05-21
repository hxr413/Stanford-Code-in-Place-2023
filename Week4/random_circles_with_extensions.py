"""
Possible Extensions:
1. Draw a random number of circles between 1 and 20
2. Draw circles of a random size 
3. Draw the circles such that all parts of the circle are within the canvas 
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    no_of_circles = random.randint(1, N_CIRCLES)
    for i in range (no_of_circles):
        draw_random_circles(canvas)


def draw_random_circles(canvas):
    circle_size = random.randint(1, CIRCLE_SIZE)
    
    left_x = random.randint(1, CANVAS_WIDTH - circle_size)
    top_y = random.randint(1, CANVAS_HEIGHT - circle_size)
    right_x = left_x + circle_size
    bottom_y = top_y + circle_size
    
    canvas.create_oval(left_x, top_y, right_x, bottom_y, random_color())
    
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()
