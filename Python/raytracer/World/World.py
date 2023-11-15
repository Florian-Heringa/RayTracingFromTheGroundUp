import numpy as np
import sys

import raytracer.Utilities.ShadeRec as ShadeRec

from ..GeometricObjects.GeometricObject import GeometricObject
from ..Lights.Light import Light
from ..World.ViewPlane import ViewPlane
from ..Utilities.RGBColor import RGBColor
from ..Utilities.Ray import Ray
from ..Utilities.Vector3D import Vector3D
from ..Utilities.Point3D import Point3D
from ..Utilities.Normal import Normal

class World:

    def __init__(self, vp: ViewPlane, tracer_type: callable, background_color: RGBColor = RGBColor(0, 0, 0)):
        self.lights = []
        self.objects = []

        self.vp = vp
        self.background_color = background_color
        self.tracer = tracer_type(self)

        self.screen = np.zeros((self.vp.vres, self.vp.vres), dtype=RGBColor)

    def add_object(self, obj: GeometricObject) -> None:
        if isinstance(obj, GeometricObject):
            self.objects.append(obj)

    def add_light(self, light: Light) -> None:
        if isinstance(light, Light):
            self.lights.append(light)

    def render_scene(self):
        pixel_color: RGBColor
        ray : Ray = Ray()
        zw : float = 100.0

        ray.direction = Vector3D(0, 0, -1)

        for r in range(self.vp.vres): # vertical
            for c in range(self.vp.hres): # horizontal
                    x = self.vp.pix_size * (c - 0.5 * (self.vp.hres - 1.0))
                    y = self.vp.pix_size * (r - 0.5 * (self.vp.vres - 1.0))
                    ray.origin = Point3D(x, y, zw)

                    pixel_color = self.tracer.trace_ray(ray)
                    self.display_pixel(r, c, pixel_color)

    def hit_objects(self, ray: Ray):

        sr :ShadeRec.ShadeRec = ShadeRec.ShadeRec.from_world(self)
        normal : Normal = Normal(0, 0, 0)
        local_hit_point = Point3D
        tmin: float = sys.float_info.max
        
        # Check all objects in the scene
        for obj in self.objects:
            # If an object is hit...
            if obj.hit(ray, sr):
                # ... check if it is closer to the screen than the currently closest object
                # if tmin-sr.t != sys.float_info.max and tmin-sr.t > 0:
                #     print(tmin-sr.t)
                if sr.t < tmin:
                    sr.hit_an_object = True
                    tmin = sr.t
                    sr.material = obj.get_material()
                    sr.hit_point = ray.origin + sr.t * ray.direction

                    # Keep track of parameters that are set inside the <hit()> function
                    normal = sr.normal
                    local_hit_point = sr.local_hit_point

        if sr.hit_an_object:
            sr.t = tmin
            sr.normal = normal
            sr.local_hit_point = local_hit_point
    
        return sr
            
    # TODO : Expand
    def display_pixel(self, i: int, j: int, raw_color: RGBColor) -> None:

        mapped_color: RGBColor

        self.screen[self.vp.hres - i - 1, j] = raw_color

    def screen_to_image(self):
        return np.array([c.to_tuple() for c in self.screen.flatten()]).reshape((self.vp.vres, self.vp.hres, 3))