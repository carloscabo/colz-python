from colz import *

c1 = Colz()

c1.setHex('#e')
print( c1.getRgbInt() )

c1.setHex('#edc')
print( c1.getRgbInt() )

c1.setHex('#d32b46')
print( c1.getRgbInt() )

c1.setHex('000')
print( c1.getHslInt() )

c1.setHex('FFFfff')
print( c1.getRgbInt() )

# Create from HSV / HSB

c1.setHsv( 348, 41, 78 )
print( c1.getRgbInt() )

c1.setHsv( [ 348, 41, 78 ] )
print( c1.getRgbInt() )

c1.setHsv( 0.9666666666666667, 0.41, 0.78 )
print( c1.getRgbInt() )

c1.setHsv( [ 0.9666666666666667, 0.41, 0.78 ] )
print( c1.getRgbInt() )

# Create from HSL

c1.setHsl( 348, 42, 62 )
print( c1.getRgbInt() )

c1.setHsl( [ 348, 42, 62 ] )
print( c1.getRgbInt() )

c1.setHsl( 0.9666666666666667, 0.42, 0.62 )
print( c1.getRgbInt() )

c1.setHsl( [ 0.9666666666666667, 0.42, 0.62 ] )
print( c1.getRgbInt() )

c1.setHsla( 0.9666666666666667, 0.42, 0.62, 0.5 )
print( c1.rgba )
print( c1.rgb )

c1.setHsla( [ 0.9666666666666667, 0.42, 0.62, 0.5 ] )
print( c1.rgba )
print( c1.rgb )



# c1.setHsb( 65, 95, 44 )
# c1.setHsb( 65, 95, 44 )
# c1.setHsl( 65, 90, 23 )
# print(c1.rgba)
# print(c1.hex)
# print(c1.hsla)

# print( Colz.hsbToRgb( 65, 90, 23 ) )
# print( Colz.rgbToHsb( 104, 112, 6 ) )
