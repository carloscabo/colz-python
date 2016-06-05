import unittest
from colz import Colz

class TestColz(unittest.TestCase):

    def test_hex_one_letter(self):
        colz = Colz()
        colz.setHex('#f')
        self.is_white(colz.getRgbInt())

    def test_hex_three_letters(self):
        colz = Colz()
        colz.setHex('#000')
        self.is_black(colz.getRgbInt())

    def test_hex_six_letters(self):
        colz = Colz()
        colz.setHex('#ffFfff')
        self.is_white(colz.getRgbInt())

    def test_hex_one_letter_no_hash(self):
        colz = Colz()
        colz.setHex('0')
        self.is_black(colz.getRgbInt())

    def test_hex_three_letters_no_hash(self):
        colz = Colz()
        colz.setHex('fFf')
        self.is_white(colz.getRgbInt())

    def test_hex_six_letters_no_hash(self):
        colz = Colz()
        colz.setHex('FfFfFf')
        self.is_white(colz.getRgbInt())


    def test_hsv_simple_black(self):
        colz = Colz()
        colz.setHsv(0,0,0)
        self.is_black(colz.getRgbInt())

    def test_hsv_simple_white(self):
        colz = Colz()
        colz.setHsv(0,0,100)
        self.is_white(colz.getRgbInt())

    def test_hsv_simple_blue(self):
        colz = Colz()
        colz.setHsv(240,100,100)
        self.is_blue(colz.getRgbInt())

    def test_hsv_array_red(self):
        colz = Colz()
        colz.setHsv([0,100,100])
        self.is_red(colz.getRgbInt())

    def test_hsv_array_green(self):
        colz = Colz()
        colz.setHsv([120,100,100])
        self.is_green(colz.getRgbInt())


    def is_white(self, rgb):
        self.assertEqual(rgb, [255, 255, 255])

    def is_black(self, rgb):
        self.assertEqual(rgb, [0, 0, 0])

    def is_red(self, rgb):
        self.assertEqual(rgb, [255, 0, 0])

    def is_green(self, rgb):
        self.assertEqual(rgb, [0, 255, 0])

    def is_blue(self, rgb):
        self.assertEqual(rgb, [0, 0, 255])


if __name__ == '__main__':
    unittest.main()
