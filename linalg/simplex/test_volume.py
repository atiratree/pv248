from unittest import TestCase

from simplex.volume import volume


class TestVolume(TestCase):
    def test_invalid_args(self):
        self.assertRaises(ValueError, volume)
        self.assertRaises(ValueError, volume, [5])
        self.assertRaises(ValueError, volume, 15, 0)
        self.assertRaises(ValueError, volume, "asd", 15)
        self.assertRaises(ValueError, volume, [15], [25, 13])
        self.assertRaises(ValueError, volume, [15, 'as'], [25, 13])
        self.assertRaises(ValueError, volume, [15, 30], [25, 13, 35])
        self.assertRaises(ValueError, volume, [15, 30], {'a': 5, 'c': 6})

    def test_2D(self):
        self.assertEqual(10, volume([0, 5], [4, 0], [0, 0]))
        self.assertEqual(21, volume([-3, 0], [3, 0], [0, 7]))
        self.assertEqual(21, volume([-3, -1], [3, -1], [0, 6]))

    def test_3D(self):
        self.assertAlmostEqual(166.66666666, volume([5, 0, 0], [-5, 0, 0], [0, 10, 0], [0, 0, 10]), 5)
        self.assertAlmostEqual(20.66666666, volume([5, -7, 4], [-5, 3, 21], [15, 10, 4], [1, -5, 10]), 5)
