from typing import Union
from math import sqrt
from .Vector3D import Vector3D

"""
"""
class Point3D:

    def __init__(self, _x: float, _y: float, _z: float):
        self.x = _x
        self.y = _y
        self.z = _z

    # def norm_sq(self) -> float:
    #     return self * self

    # def norm(self) -> float:
    #     return sqrt(self * self)
    
    def __mul__(self, other: float) -> 'Point3D':
        return Point3D(other * self.x, other * self.y, other * self.z)
        
    def __rmul__(self, other: float) -> 'Point3D':
        return self.__mul__(other)
    
    def __add__(self, other: Vector3D) -> 'Point3D':
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __radd__(self, other: Vector3D) -> 'Point3D':
        return self.__add__(other)
    
    def __sub__(self, other: Union[Vector3D, 'Point3D']) -> Union[Vector3D, 'Point3D']:
        if isinstance(other, Vector3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, Point3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __rsub__(self, other: Union[Vector3D, 'Point3D']) -> Union[Vector3D, 'Point3D']:
        return self.__sub__(other)
    
    def __neg__(self):
        return Point3D(-self.x, -self.y, -self.z)
    
    def __truediv__(self, other: Union[float, int]) -> 'Point3D':
        return Point3D(self.x/other, self.y/other, self.z/other)
    
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'
    
    def __eq__(self, other):
        return isinstance(other, Point3D) and self.x == other.x and self.y == other.y and self.z == other.z