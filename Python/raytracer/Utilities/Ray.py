from .Point3D import Point3D
from .Vector3D import Vector3D

class Ray:

    def __init__(self, origin: Point3D = Point3D(0, 0, 0), direction: Vector3D = Vector3D(0, 0, -1)):
        self.origin : Point3D = origin
        self.direction : Vector3D = direction

    