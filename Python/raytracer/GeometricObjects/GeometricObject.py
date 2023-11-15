from abc import ABC
from ..Utilities.Ray import Ray
from ..Utilities.ShadeRec import ShadeRec
from ..Utilities.RGBColor import RGBColor

from ..Materials.Material import Material

class GeometricObject(ABC):

    K_EPSILON : float = 1e-6

    def hit(self, ray: Ray, sr: ShadeRec) -> bool:
        ...

    def get_material(self) -> Material:
        ...

    def set_color(self, color: RGBColor) -> None:
        ...
