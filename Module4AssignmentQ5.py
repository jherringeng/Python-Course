class Box:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
# Create an instance of
x = Box(10, 2)
# Print
print(x.area())
