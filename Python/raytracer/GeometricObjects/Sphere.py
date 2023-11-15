from math import sqrt

from ..Utilities.Ray import Ray
from ..Utilities.ShadeRec import ShadeRec
from .GeometricObject import GeometricObject
from ..Utilities.Point3D import Point3D
from ..Utilities.RGBColor import RGBColor
from ..Materials.Material import Material

class Sphere(GeometricObject):
    
    def __init__(self, radius: float, center: Point3D) -> None:
        self.r = radius
        self.center = center

        self._material = Material(RGBColor(1.0, 0, 0))

    def hit(self, ray: Ray, sr: ShadeRec) -> bool:
        
        vTemp = ray.origin - self.center
        a = ray.direction * ray.direction
        b = 2.0 * vTemp * ray.direction
        c = vTemp * vTemp - self.r * self.r
        disc = b * b - 4.0 * a * c

        if (disc < 0.0):
            return False
        else:
            e = sqrt(disc)
            denom = 2.0 * a

            t = (-b - e) / denom # Smaller Root

            if t > super().K_EPSILON:
                sr.t = t
                sr.normal = (vTemp + t * ray.direction) / self.r
                sr.local_hit_point = ray.origin + t * ray.direction
                return True
            
            t = (-b + e) / denom # Larger Root

            if t > super().K_EPSILON:
                sr.t = t
                sr.normal = (vTemp + t * ray.direction) / self.r
                sr.local_hit_point = ray.origin + t * ray.direction
                return True
        
        return False
    
    def get_material(self) -> Material:
        return self._material
    
    def set_color(self, color: RGBColor):
        self._material.color = color