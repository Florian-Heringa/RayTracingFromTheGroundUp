from .GeometricObject import GeometricObject

from ..Utilities.Ray import Ray
from ..Utilities.Normal import Normal
from ..Utilities.Point3D import Point3D
from ..Utilities.ShadeRec import ShadeRec
from ..Materials.Material import Material
from ..Utilities.RGBColor import RGBColor

class Plane(GeometricObject):

    def __init__(self, p: Point3D, n: Normal):
        self.a : Point3D = p
        self.normal : Normal = n

        self._material = Material(RGBColor(1.0, 0, 0))

    def hit(self, ray: Ray, sr: ShadeRec) -> bool:
        t : float = (self.a - ray.origin) * self.normal / (ray.direction * self.normal)

        if t > super().K_EPSILON:
            sr.t = t
            sr.normal = self.normal
            sr.local_hit_point = ray.origin + t * ray.direction
            return True
        return False
    
    def get_material(self) -> Material:
        return self._material
    
    def set_color(self, color: RGBColor) -> None:
        self._material.color = color
    