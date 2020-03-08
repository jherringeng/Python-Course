import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.distance = math.sqrt( x**2 + y**2 )

    def __str__(self):
        return "Distance between x and y = " + str(self.distance)

    def __add__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)

p1 = Point(3,4)
p2 = Point(2,3)

print (p1+p2)
