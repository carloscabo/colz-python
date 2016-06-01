import math

class Colz:
    def __init__( self ):
        """ Class initialization """
        self.reset()

    def reset(self):
        """ Cleans all color components """
        self.hex = None
        self.r = None
        self.g = None
        self.b = None
        self.h = None
        self.s = None
        self.l = None
        self.a = 1.0
        self.rgb = None
        self.hsl = None
        self.rgba = None
        self.hsla = None
        return self

    def setHex ( self, hex ):
        """ Creates color from hex value """
        self.reset()

        hex = hex.lower().lstrip('#')

        if len(hex) < 2:
            hex = hex[0]*6
        if len(hex) < 6:
            hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
        rgb = []
        for i in range(0, 6, 2):
            rgb.append( int(hex[i:i+2], 16)/255 )

        self.hex = hex
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        self.rgb = [ *rgb ]
        self.rgba = [ *rgb, self.a ]

        self.calculateHslFromRgb( *rgb )

    def setRgb ( self, r, g, b ):
        """ Create color object from rgb values """
        self.setRgba( r, g, b )

    def setRgba ( self, r, g, b, a = 1.0 ):
        """ Creates color from rgb values value """
        self.reset()

        # If any component is int ( 0 - 255 ) convert to float ( 0 - 1)
        rgba = [ r, g, b, a ]
        for i in range(len(rgba)):
            if  isinstance( rgba[i], int ):
                rgba[i] = rgba[i]/255

        self.r = rgba[0]
        self.g = rgba[1]
        self.b = rgba[2]
        self.a = rgba[3]
        self.rgb = [ rgba[0], rgba[1], rgba[2] ]
        self.rgba = rgba
        self.hex = "%02x%02x%02x" % (int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255))

        self.calculateHslFromRgb( rgba[0], rgba[1], rgba[2] )

    def setHsl ( self, h, s, l ):
        """ Create color object from hsl values """
        self.setHsla( h, s, l )

    def setHsla ( self, h, s, l, a = 1.0 ):
        """ Create color object from hsl values """
        self.reset()

        # If any component is int ( 0 - 255 ) convert to float ( 0 - 1)
        hsla = [ h, s, l, a ]
        for i in range(len(hsla)):
            if  isinstance( hsla[i], int ):
                if i == 0:
                    hsla[i] = hsla[i]/360
                else:
                    hsla[i] = hsla[i]/100

        self.h = hsla[0]
        self.s = hsla[1]
        self.l = hsla[2]
        self.a = hsla[3]
        self.hsl = [ hsla[0], hsla[1], hsla[2] ]
        self.rgba = hsla

        self.calculateRgbFromHsl( h, s, l )

    def hue2rgb (p, q, t):
        if t < 0:
             t += 1
        if t > 1:
            t -= 1
        if t < 1 / 6:
            return p + (q - p) * 6 * t
        if t < 1 / 2:
            return q
        if t < 2 / 3:
            return p + (q - p) * (2 / 3 - t) * 6

    def calculateHslFromRgb( self, r, g, b):
        hsl = self.rgbToHsl( r, g, b )
        self.h = hsl[0]
        self.s = hsl[1]
        self.l = hsl[2]
        self.hsl = [ hsl[0], hsl[1], hsl[2] ]
        self.hsla = [ hsl[0], hsl[1], hsl[2], self.a ]

    def rgbToHsl( self, r, g, b ):
        _max = max(r, g, b)
        _min = min(r, g, b)
        l = (_max + _min) / 2

        if _max == _min:
            h = 0 # achromatic
            s = 0
        else:
            d = _max - _min
            s = d / (2 - _max - _min) if l > 0.5 else d / (_max + _min)

            if _max == r:
                h = (g - b) / d + ( 6 if g < b else 0 )
            elif _max == g:
                h = (b - r) / d + 2
            else: # max == b
                h = (r - g) / d + 4
            h /= 6
        return [ h, s, l ]

    def hslToRgb( h, s, l ):
        if s == 0.0:
            r = g = b = l # achromatic
        else:
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = self.hue2rgb(p, q, h + 1 / 3)
            g = self.hue2rgb(p, q, h)
            b = self.hue2rgb(p, q, h - 1 / 3)
        return [ r, g, b ]
