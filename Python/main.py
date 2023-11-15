from datetime import datetime
import matplotlib.pyplot as plt

from raytracer.GeometricObjects.Plane import Plane
from raytracer.GeometricObjects.Sphere import Sphere

# from raytracer.Utilities.Ray import Ray
from raytracer.Utilities.RGBColor import RGBColor
from raytracer.Utilities.Point3D import Point3D
# from raytracer.Utilities.Vector3D import Vector3D
from raytracer.Utilities.Normal import Normal
# from raytracer.Utilities.ShadeRec import ShadeRec

from raytracer.World.World import World

from raytracer.World.ViewPlane import ViewPlane
from raytracer.Tracers.RayCast import RayCast


vp = ViewPlane(hres = 300, vres = 300, pix_size=1.0, num_samples=1.0, gamma=1.0)

world = World(vp=vp, tracer_type=RayCast)

s1 = Sphere(radius=80.0, center=Point3D(0, -25, 0))
s1.set_color(RGBColor(1.0, 0.0, 0.0))

s2 = Sphere(radius=60.0, center=Point3D(0, 30, 0))
s2.set_color(RGBColor(1.0, 1.0, 0.0))

p1 = Plane(Point3D(0, 0, 0), Normal(0, 1, 1))
p1.set_color(RGBColor(0.0, 0.3, 0.0))

p2 = Plane(Point3D(0, 0, 0), Normal(0, 0, 1))
p2.set_color(RGBColor(0.0, 0, 0.3))

world.add_object(p1)
world.add_object(s2)
world.add_object(s1)
#world.add_object(p2)


world.render_scene()
image = world.screen_to_image()

plt.imshow(image)
plt.show()

plt.imsave(f"renders/{datetime.now().strftime('%y%m%d-%H%M%S')}.png", image)


##===================================== TESTS
exit()
class testClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{self.a} -- {self.b}"

def change(tcl: testClass):
    tcl.b = 10000
    tcl.a = 93218745


mcl = testClass(5, 6)
print(mcl)
change(mcl)
print(mcl)
