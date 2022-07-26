# Created by : @c_4_coding
# Olympic Logo

import turtle as p
def drawCircle(x,y,c='red'):
    p.pu()
    p.goto(x,y)
    p.pd()
    p.color(c)
    p.circle(30,360)
p.pensize(7)
drawCircle(0,0,'blue')
drawCircle(60,0,'black')
drawCircle(120,0,'red')
drawCircle(90,-30,'green')
drawCircle(30,-30,'yellow')
p.done()