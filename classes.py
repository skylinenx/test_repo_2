class location():
    #IMPORTANT: self must be the first parameter of any function inside the class
    def __init__(self, x, y):
        self.xCoordinate = x
        self.yCoordinate = y

    def __str__(self):
        return f"x: {self.xCoordinate}, y: {self.yCoordinate}"
    
    def coordinatesToList(self):
        return [self.xCoordinate, self.yCoordinate]

pinPoint = location(-12.3, 56.8)

print(pinPoint) #output determined by what specified inside __str__() function
print(pinPoint.coordinatesToList())

pinPoint.xCoordinate = -67.9
print(f"x: {pinPoint.xCoordinate}")

