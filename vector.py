import math

class Vector:
    """Class for a 2 dimensional vector"""
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.threshold = 0.0001

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        Vector(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector(self.x / float(scalar), self.y / float(scalar))
        return None
    
    def __eq__(self, other):
        if abs(self.x - other.x) < self.threshold:
            if abs(self.y - other.y) < self.threshold:
                return True
        return False

    def squaredLength(self):
        return self.x**2 + self.y**2

    def length(self):
        return math.sqrt(self.squaredLength())

    def copy(self):
        return Vector(self.x, self.y)

    def asInt(self):
        return int(self.x), int(self.y)

    def asTuple(self):
        return self.x, self.y

    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+">"