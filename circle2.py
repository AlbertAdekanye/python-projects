import turtle
t = turtle.Turtle()
s = turtle.Screen()
s. bgcolor("black")
t.speed(0)
col = ("blue", "green", "pink", "red", "yellow", "cyan")
for i in range (150):
    t.pencolor(col[i%6])
    t.circle(190-i/2,90)
    t.lt(90)
    t.circle(190-i/3,90)
    t.lt(60)
turtle.done()