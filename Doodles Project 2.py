
'''
Project Name: Turtle Patterns
Author: Alyssa Smederovac Simmonds
Due Date: 2022-02-17
Course: CS1400-002

Please set width to 700 and height to 500.
Please enter width first.
Please enter height second.
'''

import turtle
t = turtle.Turtle()

def draw_hexagon():
    """Draws a hexagon
    """
    # turtle.begin_fill()
    count = 0
    while count < 6:
        t.forward(100)
        t.lt(60)
        count += 1
    # turtle.end_fill()

def draw_star():
    """ Draws a star"""
    count = 0
    while count < 5:
        t.forward(155.4)
        t.rt(150)
        t.forward(100)
        t.rt(66)
        t.forward(85.05)
        count +=1
    count = 0
    while count < 5:
        t.begin_fill()
        t.forward(155.4)
        t.lt(150)
        t.forward(100)
        t.lt(66)
        t.forward(85.05)
        t.end_fill()
        count +=1
        
        
def draw_shuriken():
    """ Draws a shuriken"""
    count = 0
    while count < 5:
        t.forward(155.4)
        t.rt(150)
        t.forward(100)
        t.rt(66)
        t.forward(85.05)
        count +=1
    count =0
    while count<5:
        t.forward(85.05)
        t.lt(66)
        t.forward(100)
        t.lt(150)
        t.forward(155.4)
        count +=1
        
def new_pos():
    """ Brings turtle to a new position"""
    t.penup()
    t.rt(180)
    t.forward(275)
    t.rt(90)
    t.forward(50)
    t.pendown()
    
    

def main():
    ''' Program starts here.'''
    # try:
    #     width = int(input())
    #     height = int(input())
    #     turtle.screensize(width,height)
    #     pass
    # except ValueError:
    #     print('Width and height must be positive integers.')
    #     return

    # if width < 1 or height < 1:
    #     print('Width and height must be positive integers.')
    #     return
    
    draw_hexagon()
    new_pos()
    draw_star()
    new_pos()
    draw_shuriken()


if __name__ == "__main__":
    main()
