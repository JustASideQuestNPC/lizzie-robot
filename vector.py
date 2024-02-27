from math import sqrt, atan2, degrees, cos, sin, radians

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # determines what appears when the vector is printed - without this, it'll print something along
    # the lines of "<Vector object at 0x000001F4D7DFB5E0>"
    def __repr__(self) -> str:
        return f'({round(self.x, 3)}, {round(self.y, 3)})'

    # overloads the comparison (==) operator
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    # overloads the addition (+) and addition assignment (+=) operators
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # overloads the subtraction (-) and subtraction assignment (-=) operators
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # returns a copy of this vector if we want to assign it to another variable - "vec_1 = vec_2"
    # copies by reference, not by value. that means a lot of things, but the important one is that
    # they're actually the same object and changing one will also change the other
    def copy(self):
        return Vector(self.x, self.y)
    
    # returns the length of the vector
    def mag(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)
    
    # returns the rotation angle of the vector in degrees
    def heading(self) -> float:
        return degrees(atan2(self.y, self.x))
    
    def set_mag(self, new_mag: float) -> None:
        angle = self.heading()
        self.x = new_mag * cos(radians(angle))
        self.y = new_mag * sin(radians(angle))
  
# returns a vector constructed from a radius (r) and an angle in degrees (theta)
def vec_from_polar(r: float, theta: float) -> Vector:
    return Vector(
        r * cos(radians(theta)),
        r * sin(radians(theta))
    )