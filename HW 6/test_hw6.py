import unittest
from hw6 import Term
from hw6 import LinkedPolynomial

class TestTerm(unittest.TestCase):
    t1 = Term(1,2)
    t2 = Term(2,3)

    def test_init(self):
        self.assertEqual(self.t1.coef, 1)
        self.assertEqual(self.t1.exp, 2)
        self.assertEqual(self.t2.coef, 2)
        self.assertEqual(self.t2.exp, 3)

    def test_str(self):
        self.assertEqual(str(self.t1), '1*x^2')
        self.assertEqual(str(self.t2), '2*x^3')

    def test_repr(self):
        self.assertEqual(repr(self.t1), 'Term(1,2)')
        self.assertEqual(repr(self.t2), 'Term(2,3)')

    def test_eq(self):
        self.assertEqual(self.t1, Term(1,2))
        self.assertEqual(self.t2, Term(2,3))
        self.assertNotEqual(self.t1, Term(1,3))
        self.assertNotEqual(self.t2, Term(2,2))
        t3 = Term(1,2)
        self.assertEqual(self.t1, t3)
        self.assertNotEqual(self.t2, t3)

    def test_call(self):
        self.assertEqual(self.t1(2), 4)
        self.assertEqual(self.t2(2), 16)
        self.assertEqual(Term(2,4)(3), 162)

    def test_neg(self):
        n1 = -self.t1
        n2 = -self.t2
        self.assertEqual(-self.t1, n1)
        self.assertEqual(-self.t2, n2)

    def test_copy(self):
        c1 = self.t1.copy()
        c2 = self.t2.copy()
        self.assertEqual(self.t1, c1)
        self.assertEqual(self.t2, c2)
        self.assertNotEqual(id(self.t1), id(c2))
        self.assertNotEqual(id(self.t2), id(c1))


class TestLinkedPolynomial(unittest.TestCase):
    def test_get_data(self):
        pass

if __name__ == '__main__':
    unittest.main()