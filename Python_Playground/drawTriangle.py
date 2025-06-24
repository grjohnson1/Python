"""
drawTriangle.py 

Draw a Triangle with each side a different color

Author: Gregg Johnson
"""

import turtle

def draw_triangle(x1,y1, x2,y2, x3,y3, t):
    # go to start of triangle
    t.up()
    t.setpos(x1,y1)
    t.down()
    t.color('green')
    t.setpos(x2,y2)
    t.color('red')
    t.setpos(x3,y3)
    t.color('blue')
    t.setpos(x1,y1)
    t.up()

def main():
    print('testing turtle graphics...')

    t = turtle.Turtle()
    t.hideturtle()

    draw_triangle(-100,0, 0,-173.2, 100,0, t)
    turtle.mainloop()

# call main
if __name__ == '__main__':
    main()
