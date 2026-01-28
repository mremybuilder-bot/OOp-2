from turtle import *
class face:
    def __init__(self,xposition,yposition):
        self.size=90
        self.coord=(xposition,yposition)
        self.nosesize="small"
    def setsize(self,radius):
        self.size=radius
    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawoutline()
        self.draweye(135)
        self.draweye(45)
        self.drawmouth()
        self.drawnose()
        pensize(5)
    def gohome(self):
        penup()
        goto(self.coord)
        setheading(0)
    def drawoutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.gohome()
    def draweye(self,turn):
        penup()
        left(turn)
        forward(self.size/2)
        pendown()
        dot(self.size/10)
        self.gohome()
    def drawmouth(self):
        penup()
        right(135)
        forward(self.size/1.7)
        left(90)
        pendown()
        circle(self.size/1.7,90)
        self.gohome()
    def drawnose(self):
        if self.nosesize=="large":
            dot(self.size/2,"gray")
        elif self.nosesize=="small":
            dot(self.size/6,"gray")
        else:
            dot(self.size/4,"grey")
        self.gohome()
object=face(0,0)
object.draw()
showturtle()
done()