from turtle import*
import random
title("jugando")
bgcolor("black")
"""""""
forward(100)
right(90)
forward(100)
left(90)
forward(100)
backward(50)
right(90)
forward(100)
"""""""
#cuadrado
pencolor("red")
forward(100)
right(90)
penup()
pencolor("green")
forward(100)
right(90)
pendown()
pencolor("yellow")
forward(100)
right(90)
penup()
pencolor("blue")
forward(100)
"""""""
fillcolor("green")
begin_fill()
for i in range(4):
    fillcolor("red")
    begin_fill()
    forward(100)
    right(90)
    end_fill()
"""""""
speed(0)
x=1
while x<400:
    r=random.randit(0,225)
    g=random.randit(0,225)
    b=random.randit(0,225)
    colormode(255)
    pencolor(r,g,b)
    forward(5+x)
    right(200)
    x+=1


mainloop()