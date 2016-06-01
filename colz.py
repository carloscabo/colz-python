
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
        self.rgba = [ *rgb, self.a ]
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]

        self.calculateHsl()

    def setRgb ( self, r, g, b ):
        """ Create color object from rgb values """
        self.reset()
        self.setRgba( r, g, b )

    def setRgba ( self, r, g, b, a = 1.0 ):
        """ Creates color from rgb values value """
        self.reset()

        # If any component is int ( 0 - 255 ) convert to float ( 0 - 1)
        rgba = [ r, g, b, a ]
        for i in range(len(rgba)):
            if  isinstance( rgba[i], int ):
                rgba[i] = rgba[i]/255

        self.rgba = rgba
        self.r = rgba[0]
        self.g = rgba[1]
        self.b = rgba[2]
        self.a = rgba[3]
        self.hex = "%02x%02x%02x" % (int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255))

        self.calculateHsl()

    def calculateHsl( self ):
        print('calculate HSL')
        return self
