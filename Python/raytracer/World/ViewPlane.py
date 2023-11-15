		# int 			hres;   					// horizontal image resolution 
		# int 			vres;   					// vertical image resolution
		# float			s;							// pixel size
		# int				num_samples;				// number of samples per pixel
		
		# float			gamma;						// gamma correction factor
		# float			inv_gamma;					// the inverse of the gamma correction factor
		# bool			show_out_of_gamut;			// display red if RGBColor out of gamut
from ..Utilities.RGBColor import RGBColor

class ViewPlane:

    def __init__(self, hres, vres, pix_size, num_samples, gamma):
        self.hres = hres
        self.vres = vres
        self.pix_size = pix_size
        self.num_samples = num_samples
        self._gamma = gamma
        self._inv_gamma = 1/ gamma
        self.out_of_gamut = RGBColor(1.0, 0, 0)

    def set_gamma(self, gamma):
        self._gamma = gamma
        self._inv_gamma = 1/gamma

    def get_gamma(self):
        return self._gamma
    
    def get_inv_gamma(self):
        return self._inv_gamma