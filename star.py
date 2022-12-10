import turtle
def estrella(self,n,side):
    for _ in range(n):
        self.forward(side)
        self.right(360/ n)
        self.forward(side)
        self.left(720 / n)