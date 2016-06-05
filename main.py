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

c1.setHsla( 348, 42, 62, 0.5 ) # Integer componets with float alpha
print( c1.rgba )
print( c1.rgb )

c1.setHsla( [ 348, 42, 62, 0.5 ] ) # Integer componets with float alpha
print( c1.rgba )
print( c1.rgb )

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
print( c1.getRgbInt() )
print( c1.hex )

c1.setRgba( [ 0.7803921568627451, 0.4588235294117647, 0.5254901960784314 ] )
print( c1.hsla )
print( c1.getHslInt() )
print( c1.getRgbInt() )
print( c1.hex )

c1.setRgba( 199, 117, 134, 0.35 ) # Integer componets with float alpha
print( c1.hsla )
print( c1.getHslInt() )
print( c1.getRgbInt() )
print( c1.hex )

c1.setRgba( [ 199, 117, 134, 0.35 ] ) # Integer componets with float alpha
print( c1.hsla )
print( c1.getHslInt() )
print( c1.getRgbInt() )
print( c1.hex )

c1.setRgba( 0.7803921568627451, 0.4588235294117647, 0.5254901960784314, 0.35 )
print( c1.hsla )
print( c1.getHslInt() )
print( c1.getRgbInt() )
print( c1.hex )

c1.setRgba( [ 0.7803921568627451, 0.4588235294117647, 0.5254901960784314, 0.35 ] )
print( c1.hsla )
print( c1.getHslInt() )
print( c1.getRgbInt() )
print( c1.hex )

# Create from RGB
print('# Modify HSL parameters')

c1.setHsl( 348, 42, 62 )
c1.setHue( 150 )
print( c1.getHslInt() )
c1.setHue( 510 )
print( c1.getHslInt() )
c1.setHue( 0.4166666666666667 )
print( c1.getHslInt() )
c1.setHue( 1.4166666666666667 )
print( c1.getHslInt() )

c1.setHsl( 348, 42, 62 )
c1.setSat( 56 )
print( c1.getHslInt() )
print( c1.hsl )
c1.setSat( 150 ) # Sat over 1.0 / 100 -> 1.0
print( c1.getHslInt() )
print( c1.hsl )
c1.setSat( 0.56 )
print( c1.getHslInt() )
print( c1.hsl )
c1.setSat( 1.5 ) # Sat over 1.0 / 100 -> 1.0
print( c1.getHslInt() )
print( c1.hsl )

c1.setHsl( 348, 42, 62 )
c1.setLum( 56 )
print( c1.getHslInt() )
print( c1.hsl )
c1.setLum( 150 ) # Lum over 1.0 / 100 -> 1.0
print( c1.getHslInt() )
print( c1.hsl )
c1.setLum( 0.56 )
print( c1.getHslInt() )
print( c1.hsl )
c1.setLum( 1.5 ) # Lum over 1.0 / 100 -> 1.0
print( c1.getHslInt() )
print( c1.hsl )

# Create from RGB
print('# Modify Alpha')

c1.setHsla( 0.9666666666666667, 0.42, 0.62, 0.5 )
c1.setAlpha( 0.73 )
print( c1.hsla )
print( c1.rgba )
print( c1.a )
c1.setAlpha( 8.72 ) # Alpha over 1.0 -> 1.0
print( c1.hsla )
print( c1.rgba )
print( c1.a )

# Create from RGB
print('# Rotate hue ( hsl )')

c1.setHsl( 0.9666666666666667, 0.42, 0.62 ) # h = 348 (int)

# CCW

c1.setHue( 348 )
print('Hue inicial en float: '+str( c1.h ))
c1.rotateHue( -20 )
print( c1.h )

c1.setHue( 348 )
c1.rotateHue( -0.05555555555555555 )
print( c1.h )

c1.setHue( 348 )
c1.rotateHue( -380 )
print( c1.h )

c1.setHue( 348 )
c1.rotateHue( -6.05555555555555555 )
print( c1.h )

# CW

c1.setHue( 348 )
c1.rotateHue( 20 )
print( c1.h )

c1.setHue( 348 )
c1.rotateHue( 0.05555555555555555 )
print( c1.h )

c1.setHue( 348 )
c1.rotateHue( 380 )
print( c1.h )

c1.setHue( 348 )
c1.rotateHue( 6.05555555555555555 )
print( c1.h )

# Create from RGB
print('# Interpolate / mix hsl colors')

c1_values = [ 0.75, 0.42, 0.62, 0.5 ]
c2_values = [ 0.1, 0.62, 0.42, 0.1 ]
c1 = Colz()
c1.setHsla( c1_values )
c2 = Colz()
c2.setHsla( c2_values )
cmix1 = Colz.interpolate( c1, c2, 0.5 )
print(cmix1)
cmix1 = Colz.interpolate( c2, c1, 0.5 )
print(cmix1)
cmix1 = Colz.interpolate( c1_values, c2_values, 0.5 )
print(cmix1)
cmix1 = Colz.interpolate( c2_values, c1_values, 0.01 )
print(cmix1)
# print( Colz.hsbToRgb( 65, 90, 23 ) )
# print( Colz.rgbToHsb( 104, 112, 6 ) )
