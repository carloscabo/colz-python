import unittest
from colz import Colz

class TestColz(unittest.TestCase):

    def test_hex_one_letter(self):
        expected = [255, 255, 255]
        colz = Colz()
        colz.setHex('#f')
        self.assertEqual(colz.getRgbInt(), expected)

    def test_hex_three_letters(self):
        expected = [0, 0, 0]
        colz = Colz()
        colz.setHex('#000')
        self.assertEqual(colz.getRgbInt(), expected)

    def test_hex_six_letters(self):
        expected = [255, 255, 255]
        colz = Colz()
        colz.setHex('#ffFfff')
        self.assertEqual(colz.getRgbInt(), expected)

    def test_hex_one_letter_no_hash(self):
        expected = [0, 0, 0]
        colz = Colz()
        colz.setHex('0')
        self.assertEqual(colz.getRgbInt(), expected)

    def test_hex_three_letters_no_hash(self):
        expected = [255, 255, 255]
        colz = Colz()
        colz.setHex('fFf')
        self.assertEqual(colz.getRgbInt(), expected)

    def test_hex_six_letters_no_hash(self):
        expected = [255, 255, 255]
        colz = Colz()
        colz.setHex('FfFfFf')
        self.assertEqual(colz.getRgbInt(), expected)



if __name__ == '__main__':
    unittest.main()
