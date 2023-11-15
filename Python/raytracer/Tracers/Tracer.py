from abc import ABC

from ..Utilities.Ray import Ray
from ..Utilities.RGBColor import RGBColor

class Tracer(ABC):

    def __init__(self):
        ...

    def trace_ray(self, ray: Ray) -> RGBColor:
        ...