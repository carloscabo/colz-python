from colz import *

c1 = Colz()

# Create from hex
print('# Create from HEX')

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
print('# Create from HSV / HSB')

c1.setHsv( 348, 41, 78 )
print( c1.getRgbInt() )

c1.setHsv( [ 348, 41, 78 ] )
print( c1.getRgbInt() )

c1.setHsv( 0.9666666666666667, 0.41, 0.78 )
print( c1.getRgbInt() )

c1.setHsv( [ 0.9666666666666667, 0.41, 0.78 ] )
print( c1.getRgbInt() )

# Create from HSL
print('# Create from HSL')

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

# Create from RGB
print('# Create from RGB')

c1.setRgb( 199, 117, 134 )
print( c1.hex )

c1.setRgb( [ 199, 117, 134 ] )
print( c1.hex )

c1.setRgb( 0.7803921568627451, 0.4588235294117647, 0.5254901960784314 )
print( c1.hsla )
print( c1.getHslInt() )
print( c1.hex )

c1.setRgba( [ 0.7803921568627451, 0.4588235294117647, 0.5254901960784314 ] )
print( c1.hsla )
print( c1.getHslInt() )
print( c1.hex )

c1.setRgba( 0.7803921568627451, 0.4588235294117647, 0.5254901960784314, 0.35 )
print( c1.hsla )
print( c1.getHslInt() )
print( c1.hex )

c1.setRgba( [ 0.7803921568627451, 0.4588235294117647, 0.5254901960784314, 0.35 ] )
print( c1.hsla )
print( c1.getHslInt() )
print( c1.hex )

# c1.setHsb( 65, 95, 44 )
# c1.setHsb( 65, 95, 44 )
# c1.setHsl( 65, 90, 23 )
# print(c1.rgba)
# print(c1.hex)
# print(c1.hsla)

# print( Colz.hsbToRgb( 65, 90, 23 ) )
# print( Colz.rgbToHsb( 104, 112, 6 ) )
