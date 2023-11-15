from dataclasses import dataclass
import sys

from .Ray import Ray
from .Point3D import Point3D
from .Normal import Normal
from ..Materials.Material import Material

@dataclass
class ShadeRec:

    hit_an_object : bool = False
    local_hit_point : Point3D = None
    hit_point : Point3D = None
    normal : Normal = None
    material : Material = None
    wr : object = None
    t : float = sys.float_info.max
    ray : Ray = Ray()

    @staticmethod
    def from_world(wr):
        sr = ShadeRec(wr=wr)
        return sr
