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
    
    p1 = LinkedPolynomial()
    t0 = Term(1,0)
    t1 = Term(1,1)
    t2 = Term(-2,2)
    t3 = Term(3,3)


    def test_init(self):
        self.assertIsNotNone(self.p1)
    
    def test_addTerm(self):
        self.p1.addTerm(self.t3)
        self.assertEqual(str(self.p1), str(self.t3))

        self.p1.addTerm(self.t2)
        self.assertEqual(str(self.p1), str(self.t3) + ' - ' + str(-self.t2))

        self.p1.addTerm(self.t1)
        self.assertEqual(str(self.p1), str(self.t3) + ' - ' + str(-self.t2) + ' + ' + str(self.t1))

        self.p1.addTerm(self.t0)
        self.assertEqual(str(self.p1), str(self.t3) + ' - ' + str(-self.t2) + ' + ' + str(self.t1) + ' + ' + str(self.t0))

    def test_createFromNumbers(self):
        n = [(3,3), (2,2), (-1,1), (1,0)]
        p2 = LinkedPolynomial()
        p2.createFromNumbers(n)
        self.assertEqual(str(p2), str(Term(3,3)) + ' + ' + str(Term(2,2)) + ' - ' + str(-Term(-1,1)) + ' + ' + str(Term(1,0)))

    def test_len(self):
        self.assertEqual(len(self.p1), 4)

    def test_eq(self):
        p3 = LinkedPolynomial()
        self.assertNotEqual(self.p1, p3)
        p3.addTerm(self.t3)
        self.assertNotEqual(self.p1, p3)
        p3.addTerm(self.t2)
        self.assertNotEqual(self.p1, p3)
        p3.addTerm(self.t1)
        self.assertNotEqual(self.p1, p3)
        p3.addTerm(self.t0)
        self.assertEqual(self.p1, p3)
        p3.addTerm(Term(4,4))
        self.assertNotEqual(self.p1, p3)

    def test_call(self):
        self.assertEqual(self.p1(0), 1)
        self.assertEqual(self.p1(1), 3)
        self.assertEqual(self.p1(5), 331)
        self.assertEqual(self.p1(-1), -5)
        self.assertEqual(self.p1(-10), -3209)

    def test_neg(self):
        p4 = -self.p1
        self.assertEqual(str(p4), str(-self.t3) + ' + ' + str(-self.t2) + ' - ' + str(self.t1) + ' - ' + str(self.t0))

    def test_sub(self):
        p5 = LinkedPolynomial()
        p5.addTerm(Term(1,3))

        p6 = LinkedPolynomial()
        n = [(2,3), (-2,2), (1,1), (1,0)]
        p6.createFromNumbers(n)

        self.assertEqual(self.p1 - p5, p6)

        p5.addTerm(Term(1,2))
        p5.addTerm(Term(2,1))
        p5.addTerm(Term(-3,0))

        p7 = LinkedPolynomial()
        n = [(2,3), (-3,2), (-1,1), (4,0)]
        p7.createFromNumbers(n)
        self.assertEqual(self.p1 - p5, p7)

if __name__ == '__main__':
    unittest.main()