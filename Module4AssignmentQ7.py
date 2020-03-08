class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x-value: " + str(self.x) + " y-value: " + str(self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(3,4)
p2 = Point(2,3)

p1and2 = p1+p2

print (p1+p2)
