from typing import Tuple
from math import sqrt

class RGBColor:

    def __init__(self, r: int = None, g: int = None, b: int = None, c: int = None, ):
        if c is not None:
            self.r = self.g = self.b = c
        if r is not None and g is not None and b is not None:
            self.r : int = r
            self.g : int = g
            self.b : int = b

    def to_tuple(self) -> Tuple[int]:
        return (self.r, self.g, self.b)
    
    def norm(self):
        return sqrt(self.r*self.r + self.g*self.g + self.b*self.b)
    
    def normalize(self):
        return self / self.norm()
    
    def __mul__(self, other: ['RGBColor', float]) -> 'RGBColor':
        if isinstance(other, (float, int)):
            return RGBColor(self.r*other, self.g*other, self.b*other)
        return RGBColor(self.r*other.r, self.g*other.g, self.b*other.b)
    
    def __truediv__(self, other):
        if other != 0:
            return self.__mul__(1/other)
    
    def clamp(self):
        if self.r > 1:
            self.r = 1
        if self.g > 1:
            self.g = 1
        if self.b > 1:
            self.b = 1