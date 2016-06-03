import math

class Colz:
    def __init__( self ):
        """ Class initialization """
        self.reset()

    def reset ( self ):
        """ Cleans all color components """
        self.hex = ''
        self.r = 0.0
        self.g = 0.0
        self.b = 0.0
        self.h = 0.0
        self.s = 0.0
        self.l = 0.0
        self.a = 1.0
        self.rgb = []
        self.hsl = []
        self.rgba = []
        self.hsla = []
        return self

    def setHex ( self, hex ):
        """ Creates color object from hex value """
        self.reset()

        hex = hex.lower().lstrip('#')

        if len(hex) < 2:
            hex = hex[0]*6
        if len(hex) < 6:
            hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
        rgb = []
        for i in range(0, 6, 2):
            rgb.append( int( hex[i:i+2], 16) / 255.0 )

        self.hex = hex
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        self.rgb  = [ rgb[0], rgb[1], rgb[2] ]
        self.rgba = [ rgb[0], rgb[1], rgb[2], self.a ]

        self.updateFromRgb( *rgb )

    def setRgb ( self, r, g, b ):
        """ Creates color object from rgb values """
        self.setRgba( r, g, b )

    def setRgba ( self, r, g, b, a = 1.0 ):
        """Creates color object from rgba values """
        self.reset()

        # If any component is int ( 0 - 255 ) convert to float ( 0 - 1 )
        rgba = [ r, g, b, a ]
        for i in range(len(rgba)):
            if  isinstance( rgba[i], int ):
                rgba[i] = rgba[i] / 255.0

        self.r = rgba[0]
        self.g = rgba[1]
        self.b = rgba[2]
        self.a = rgba[3]
        self.rgb = [ rgba[0], rgba[1], rgba[2] ]
        self.rgba = rgba
        self.hex = Colz.rgbToHex( rgba[0], rgba[1], rgba[2] )

        self.updateFromRgb()

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
                hsla[i] = hsla[i] / 360.0 if i == 0 else hsla[i] / 100.0

        self.h = hsla[0]
        self.s = hsla[1]
        self.l = hsla[2]
        self.a = hsla[3]
        self.hsl  = [ hsla[0], hsla[1], hsla[2] ]
        self.hsla = [ hsla[0], hsla[1], hsla[2], hsla[3] ]

        self.updateFromHsl()

    def setHsv ( self, h, s, b ):
        """ Create color object from hsb / hsv values """
        self.reset()
        rgb = Colz.hsbToRgb( h, s, b )
        self.setRgba( rgb[0], rgb[1], rgb[2] )

    def updateFromRgb ( self ):
        """ Generates hsl equivalencies from rgb """
        hsl = self.rgbToHsl( self.r, self.g, self.b )
        self.h = hsl[0]
        self.s = hsl[1]
        self.l = hsl[2]
        self.hsl  = hsl
        self.hsla = [ hsl[0], hsl[1], hsl[2], self.a ]

    def updateFromHsl ( self ):
        """ Generates rgb equivalencies from hsl """
        rgb = Colz.hslToRgb( self.h, self.s, self.l )
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        self.rgb = rgb
        self.rgba = [ rgb[0], rgb[1], rgb[2], self.a ]
        # Updates Hex
        self.hex = Colz.rgbToHex( rgb[0], rgb[1], rgb[2] )

    # Utils, setters

    def setHue ( self, newhue ):
        """ Modifies hue value of Colz object """
        if  isinstance( newhue, int ):
            newhue /= 360.0
        self.h = newhue
        self.hsl[0]  = newhue
        self.hsla[0] = newhue
        self.updateFromHsl()

    def setSat ( self, newsat ):
        """ Modifies sat value of Colz object """
        if  isinstance( newsat, int ):
            newsat /= 100.0
        self.s = newsat
        self.hsl[1]  = newsat
        self.hsla[1] = newsat
        self.updateFromHsl()

    def setLum ( self, newlum ):
        """ Modifies lum value of Colz object """
        if  isinstance( newlum, int ):
            newlum /= 100
        self.l = newlum
        self.hsl[2]  = newlum
        self.hsla[2] = newlum
        self.updateFromHsl()

    def setAlpha ( self, newalpha ):
        """ Modifies alpha value of Colz object """
        if  isinstance( newalpha, int ):
            raise ValueError('Expects a float value in the [ 0.0 - 1.0 ] range!')
        self.a = newalpha
        self.hsla[3] = newalpha
        self.rgba[3] = newalpha

    def rotateHue ( self, hue_inc ):
        """ Rotates the hue value of Colz object """
        if  isinstance( hue_inc, int ):
            hue_inc /= 360.0
        newhue = self.h + hue_inc
        if newhue > 360.0:
            newhue -= 360.0
        self.h += newhue
        self.hsl[0]  = self.h
        self.hsla[0] = self.h
        self.updateFromHsl()

    # Statioc methods

    @staticmethod
    def hslToRgb ( h, s, l ):
        """ Converts hsl color to rgb list """
        r = l
        g = l
        b = l
        v = l * ( 1.0 + s ) if l <= 0.5 else l + s - l * s
        if ( v > 0 ):
            m = l + l - v
            sv = ( v -  m ) / v
            h *= 6.0
            sextant = int( math.floor( h ) )
            fract = h - sextant
            vsf = v * sv * fract
            mid1 = m + vsf
            mid2 = v - vsf

            # Switch sextant
            if sextant == 0:
                r = v
                g = mid1
                b = m
            elif sextant == 1:
                r = mid2
                g = v
                b = m
            elif sextant == 2:
                r = m
                g = v
                b = mid1
            elif sextant == 3:
                r = m
                g = mid2
                b = v
            elif sextant == 4:
                r = mid1
                g = m
                b = v
            elif sextant == 5:
                r = v
                g = m
                b = mid2

            return [ r, g, b ]

    @staticmethod
    def rgbToHsl( r, g, b ):
        """ Converts rgb color to hsl list """
        _max = max( r, g, b )
        _min = min( r, g, b )
        l = (_max + _min) / 2.0

        if _max == _min:
            h, s = 0.0 # achromatic
        else:
            d = _max - _min
            s = d / ( 2.0 - _max - _min ) if l > 0.5 else d / (_max + _min)

            if _max == r:
                h = ( g - b ) / d + ( 6.0 if g < b else 0.0 )
            elif _max == g:
                h = ( b - r ) / d + 2.0
            else: # max == b
                h = ( r - g ) / d + 4.0
            h /= 6.0
        return [ h, s, l ]

    @staticmethod
    def rgbToHsv ( r, g, b ):
        """ Converts rgb color to hsv list """
        _max = max( r, g, b )
        _min = min( r, g, b )
        v = _max
        d = _max - _min;
        s = 0.0 if _max == 0.0 else d / _max

        if _max == _min:
            h = 0.0 # achromatic
        else:
            if _max == r:
                h = (g - b) / d + ( 6.0 if g < b else 0.0 )
            elif _max == g:
                h = (b - r) / d + 2.0
            elif _max == b:
                h = (r - g) / d + 4.0
            h /= 6.0
        return [ h, s, v ]

    @staticmethod
    def rgbToHex ( r, g, b ):
        """ Converts rgb color to hex string """
        return "%02x%02x%02x" % ( round( r * 255.0 ), round( g * 255.0 ), round( b * 255.0 ))

    @staticmethod
    def rgbToHsv ( r, g, b ):
        """ Converts rgb color to hsv list """
        if  isinstance( r, int ):
            r /= 255.0
        if  isinstance( g, int ):
            g /= 255.0
        if  isinstance( b, int ):
            b /= 255.0

        _max = max( r, g, b )
        _min = min( r, g, b )
        v = _max

        d = _max - _min
        s = 0.0 if max == 0.0 else d / _max

        if _max == _min:
            h = 0.0 # achromatic
        else:
            if _max == r:
                h = ( g - b ) / d + ( 6.0 if g < b else 0.0 )
            elif _max == g:
                h = ( b - r ) / d + 2.0
            elif _max == b:
                h = (r - g) / d + 4.0
            h /= 6.0

            # map top 360, 100, 100
            # h = int( round( h * 360 ) )
            # s = int( round( s * 100 ) )
            # v = int( round( v * 100 ) )

        return [ h, s, v ]

    @staticmethod
    def hsvToRgb ( h, s, v ):
        """ Converts hsv color to rgb list """
        if  isinstance( h, int ):
            h /= 360.0
        if  isinstance( s, int ):
            s /= 100.0
        if  isinstance( v, int ):
            v /= 100.0

        if v == 0.0:
            return [0, 0, 0]

        h = h * 6.0
        i = int( math.floor( h ) )

        f = h - i
        p = v * ( 1.0 - s )
        q = v * ( 1.0 - ( s * f ) )
        t = v * ( 1.0 - ( s * ( 1.0 - f ) ) )

        if i == 0:
            r = v
            g = t
            b = p
        elif i == 1:
            r = q
            g = v
            b = p
        elif i == 2:
            r = p
            g = v
            b = t
        elif i == 3:
            r = p
            g = q
            b = v
        elif i == 4:
            r = t
            g = p
            b = v
        elif i == 5:
            r = v
            g = p
            b = q
        # To return int
        # r = int( math.floor( r * 255 ) )
        # g = int( math.floor( g * 255 ) )
        # b = int( math.floor( b * 255 ) )

        return [ r, g, b ]

    # @staticmethod
    # def hsvToHsl ( h, s, b ):
    #     """ This is an alias to hsbToHsl """
    #     Colz.hsbToHsl ( h, s, b )

    @staticmethod
    def hsbToHsl ( h, s, b ):
        """ Converts hsv / hsb to rgb """
        return Colz.rgbToHsl( Colz.hsbToRgb( h, s, b ) )

    @staticmethod
    def lerp ( v1, v2, amt ):
        """ Generic linear interpolation """
        print('eo')

    @staticmethod
    def mixHslColors ( h1, s1, l1, h2, s2, l2, amt ):
        """ Mixes or interpolates 2 colors in hsl format """
        if isinstance( h1, Colz ):
            s1 = h1.s
            l1 = h1.l
            h1 = h1.h
        if isinstance( h2, Colz ):
            s2 = h2.s
            l2 = h2.l
            h2 = h2.h
        if  isinstance( h1, int ):
            h1 /= 360.0
        if  isinstance( s1, int ):
            s1 /= 100.0
        if  isinstance( l1, int ):
            l1 /= 100.0
        if  isinstance( h2, int ):
            h2 /= 360.0
        if  isinstance( s2, int ):
            s2 /= 100.0
        if  isinstance( l2, int ):
            l2 /= 100.0
