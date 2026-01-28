#create a rectangle with properties length and width and a method that calculate area of rectangle
class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculatearea(self):
        area=self.width*self.height
        print(f"area of rectangle is {area}")
ob=rectangle(19,12)
ob.calculatearea()