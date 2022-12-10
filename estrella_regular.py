from turtle import*
import random
title("jugando")
bgcolor("black")
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