from typing import Union
from math import sqrt

from .Vector3D import Vector3D

"""
"""
class Normal:

    def __init__(self, _x: float, _y: float, _z: float):
        self.x = _x
        self.y = _y
        self.z = _z

        # norm = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        # if norm != 0:
        #     self.x /= norm
        #     self.y /= norm
        #     self.z /= norm        

    def norm(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def normalize(self) -> 'Normal':
        return self / self.norm()
    
    def __mul__(self, other: Union[Vector3D, float]) -> Union[Vector3D, float]:
        if isinstance(other, (float, int)):
            return Normal(other * self.x, other * self.y, other * self.z)
        else:
            return self.x * other.x + self.y * other.y + self.z * other.z
        
    def __rmul__(self, other: Union['Normal', int, float]) -> Union['Normal', float]:
        return self.__mul__(other)
    
    def __add__(self, other: Union['Normal', Vector3D]) -> Union['Normal', Vector3D]:
        if isinstance(other, Normal):
            return Normal(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    # def __sub__(self, other):
    #     return Normal(self.x - other.x, self.y - other.y, self.z - other.z)
    
    # def __rsub__(self, other):
    #     return self.__sub__(other)
    
    def __neg__(self) -> 'Normal':
        return Normal(-self.x, -self.y, -self.z)
    
    def __truediv__(self, other: Union[float, int]) -> 'Normal':
        return Normal(self.x/other, self.y/other, self.z/other)
    
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Normal) and self.x == other.x and self.y == other.y and self.z == other.z