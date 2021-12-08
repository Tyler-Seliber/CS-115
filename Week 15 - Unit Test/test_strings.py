import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual('fOo'.upper(), 'FOO')
        self.assertNotEqual('FOO'.upper(), 'foo')
        self.assertEqual('Foo'.upper(), 'FOO')
        self.assertEqual('bAr'.upper(), 'BAR')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertFalse('BaR'.isupper())
        self.assertEqual('fOO'.isupper(), False)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()