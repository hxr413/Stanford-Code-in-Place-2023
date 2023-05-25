"""
As an extension, only draw a circle if the mouse is on the canvas. To do this, check that the mouse_x and mouse_y are within the boundaries of CANVAS_WIDTH and CANVAS_HEIGHT. 
"""

from graphics import Canvas
import time

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # your animation code here :) 
    while True:
        left_x = canvas.get_mouse_x()
        top_y = canvas.get_mouse_y()
        right_x = left_x + CIRCLE_SIZE
        bottom_y = top_y + CIRCLE_SIZE
        
        if (left_x >= 0) and (top_y >= 0) and (right_x <= CANVAS_WIDTH) and (bottom_y <= CANVAS_HEIGHT):
            canvas.create_oval(left_x, top_y, right_x, bottom_y, "salmon")
        
        time.sleep(DELAY)
    

if __name__ == "__main__":
    main()
