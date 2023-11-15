from dataclasses import dataclass

import raytracer.Utilities.ShadeRec
from ..Utilities.RGBColor import RGBColor

@dataclass
class Material:

    color : RGBColor

    def shade(self, sr):
        return self.color