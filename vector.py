import math

class Vector:
    """Class for a 2 dimensional vector which makes the movement in the game a lot easier """
    
    def __init__(self, x = 0, y = 0):
        """create vector 

        Args:
            x (int): x-value of the vector. Defaults to 0.
            y (int): y-value of the vector. Defaults to 0.
        """
        self.x = x
        self.y = y
        self.threshold = 0.0001

    def __add__(self, other):
        """overwrite normal addition

        Args:
            other (Vector): Vector that should be added

        Returns:
            Vector: result
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """overwrite normal substraction

        Args:
            other (Vector): Vector that should be substracted

        Returns:
            Vector: result
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """negation"""
        return Vector(-self.x, -self.y)

    def __mul__(self, scalar):
        """multiplication

        Args:
            scalar (number): number which should be multiplied with the vector

        Returns:
            Vector: result
        """
        return Vector(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        """division

        Args:
            scalar (number): number which the vector should be divided with

        Returns:
            Vector: result
            None: if scalar = 0
        """
        if scalar != 0:
            return Vector(self.x / float(scalar), self.y / float(scalar))
        return None
    
    def __eq__(self, other):
        """equality

        Args:
            other (Vector): Vector which should be checked if it is equal

        Returns:
            bool: true if equal
        """
        if abs(self.x - other.x) < self.threshold:
            if abs(self.y - other.y) < self.threshold:
                return True
        return False

    def squaredLength(self):
        """squared length of the vector

        Returns:
            number: squared length of the vector
        """
        return self.x**2 + self.y**2

    def length(self):
        """length of the vector

        Returns:
            float: length of the vector
        """
        return math.sqrt(self.squaredLength())

    def copy(self):
        """copy a vector

        Returns:
            Vector: copy
        """
        return Vector(self.x, self.y)

    def asInt(self):
        """returns vector components as integers

        Returns:
            int: x and y as integers
        """
        return int(self.x), int(self.y)

    def asTuple(self):
        """tuple 

        Returns:
            tuple: x and y as tuple
        """
        return self.x, self.y