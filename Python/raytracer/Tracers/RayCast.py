from ..Utilities.RGBColor import RGBColor
from ..Utilities.Ray import Ray
from .Tracer import Tracer
from ..World.World import World
from ..Utilities.ShadeRec import ShadeRec

class RayCast(Tracer):

    def __init__(self, world: World):
        self.world = world

    def trace_ray(self, ray: Ray) -> RGBColor:
        # Query the world if something is hit
        sr: ShadeRec = self.world.hit_objects(ray)

        # If a hit has been detected, return corresponding color
        if sr.hit_an_object:
            sr.ray = ray # Used for Specular Shading
            return sr.material.shade(sr)
        else:
            return self.world.background_color
        

