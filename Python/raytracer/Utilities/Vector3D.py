from typing import Union
from math import sqrt

"""
"""
class Vector3D:

    def __init__(self, _x: float, _y: float, _z: float):
        self.x = _x
        self.y = _y
        self.z = _z

    def norm_sq(self) -> float:
        return self * self

    def norm(self) -> float:
        return sqrt(self * self)
    
    def __mul__(self, other: Union['Vector3D', float]) -> Union['Vector3D', float]:
        if isinstance(other, (float, int)):
            return Vector3D(other * self.x, other * self.y, other * self.z)
        else:
            return self.x * other.x + self.y * other.y + self.z * other.z
        
    def __rmul__(self, other: Union['Vector3D', float]) -> Union['Vector3D', float]:
        return self.__mul__(other)
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)
    
    def __truediv__(self, other: Union[float, int]) -> 'Vector3D':
        return Vector3D(self.x/other, self.y/other, self.z/other)
    
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'
    
    def cross(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.y*other.z - self.z*other.y,
                        self.z*other.x - self.x*other.z,
                        self.x*other.y - self.y*other.x)
    
    def __eq__(self, other):
        return isinstance(other, Vector3D) and self.x == other.x and self.y == other.y and self.z == other.z