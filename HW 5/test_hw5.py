import unittest
import hw5

class Test(unittest.TestCase):

    def test_mult(self):
        self.assertEqual(hw5.mult(6,7), 42)
        self.assertEqual(hw5.mult(1.5,28), 42.0)

    def test_update(self):
        self.assertEqual(hw5.update(1,3), 5)
        self.assertEqual(hw5.update(-1,3), -1)
        self.assertEqual(hw5.update(1,10), 3791862310265926082868235028027893277370233152247388584761734150717768254410341175325352026)
        self.assertEqual(hw5.update(-1,10), 0)

    def test_inMSet(self):
        self.assertTrue(hw5.inMSet(0 + 0j, 25))
        self.assertFalse(hw5.inMSet(3 + 4j, 25))
        self.assertTrue(hw5.inMSet(0.3 + -0.5j, 25))
        self.assertFalse(hw5.inMSet(-0.7 + 0.3j, 25))
        self.assertTrue(hw5.inMSet(0.42 + 0.2j, 25))
        self.assertFalse(hw5.inMSet(0.42 + 0.2j, 50))

    def test_scale(self):
        self.assertEqual(hw5.scale(100, 200, -2.0, 1.0), -0.5)
        self.assertEqual(hw5.scale(100, 200, -1.5, 1.5), 0.0)
        self.assertEqual(hw5.scale(100, 300, -2.0, 1.0), -1.0)
        self.assertEqual(hw5.scale(25, 300, -2.0, 1.0), -1.75)
        self.assertAlmostEqual(hw5.scale(299, 300, -2.0, 1.0), 0.99)


if __name__ == "__main__":
    unittest.main()