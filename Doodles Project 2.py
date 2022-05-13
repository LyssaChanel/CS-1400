
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
wn = t.getscreen()

colors = ["white", "#F7CAC9",  "pink", "#B76E79","#a24857", "#8d1919", "#dc2f02", "#f37a48", "orange", "#f5e65e", "#bbf261", "#36D457",  "green", "#3eb489", "#5dc9b6", "#6495ed","#002366","#30106b", "#673147","purple"]

def set_up_scene():
    """Fills background and changes size"""
    wn.screensize(800,800)
    t.speed(10)
    wn.bgcolor("gray")
    t.penup()


def draw_hexagon(color, scale):
    """Draws a hexagon"""
    t.color("black")
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    # turtle.begin_fill()
    count = 0
    while count < 6:
        t.forward(100 * scale)
        t.lt(60)
        count += 1
    t.end_fill()
    t.penup()
    # turtle.end_fill()

def draw_star():
    """ Draws a star"""
    t.color("pink")
    t.pendown()
    count = 0
    t.fillcolor("#c23e8f")
    while count < 5:
        t.begin_fill()
        t.forward(155.4)
        t.rt(150)
        t.forward(100)
        t.rt(66)
        t.forward(85.05)
        t.end_fill()
        count +=1
    count = 0
    t.color("#B76E79")
    t.fillcolor("#912668")
    while count < 5:
        t.begin_fill()
        t.forward(155.4)
        t.lt(150)
        t.forward(100)
        t.lt(66)
        t.forward(85.05)
        t.end_fill()
        count +=1
    t.penup()
        
        
def draw_shuriken():
    """ Draws a shuriken"""
    t.color("black")
    t.pendown()
    count = 0
    t.fillcolor("#B76E79")
    t.begin_fill()
    while count < 5:
        t.forward(155.4)
        t.rt(150)
        t.forward(100)
        t.rt(66)
        t.forward(85.05)
        count +=1
    t.end_fill()
    count =0
    t.fillcolor( "white")
    t.begin_fill()
    while count<5:
        t.forward(85.05)
        t.lt(66)
        t.forward(100)
        t.lt(150)
        t.forward(155.4)
        count +=1
    t.end_fill()
    t.penup()
    

def main():
    ''' Program starts here.'''
    set_up_scene()
    t.goto(100,150)
    count = 0
    scale = 1
    while scale > 0:
        draw_hexagon(colors[count], scale)
        t.rt(30)
        scale -= .05
        count += 1
    t.goto(-200,100)
    draw_star()
    t.goto(0,-150)
    draw_shuriken()
    wn.exitonclick()
    


if __name__ == "__main__":
    main()
