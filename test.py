__author__ = 'Dylan Gill'

# Steps of creating test suite
import unittest

class testAssertions(unittest.TestCase):
    def setup(self):
        print("\nSetting up resources or performing setup tasks")

    def tearDown(self):
        print("\nTearing down or cleaning up resources")

    def test_assertEqual(self):
        self.assertEqual(2 + 2, 4)

    def testAssertNotEqual(self):
        self.assertNotEqual(2 + 2, 5)

    def testAssertTrue(self):
        self.assertTrue(2 * 2 == 4, "Assertion should fail")

    def testAssertFalse(self):
        self.assertFalse(4 + 4 != 8, "Assertion should pass")

    def testAssertIs(self):
        self.assertIs("Hello", "Hello")

    def testAssertIsNot(self):
        self.assertIsNot("Hello", "World!")

    def testAssertIsNone(self):
        self.assertIsNone(None)

    def testAssertIsNotNone(self):
        self.assertIsNotNone("Something")

    def testAssertIn(self):
        self.assertIn(8, [1, 2, 3, 8])

    def testAsserNotIn(self):
        self.assertNotIn(4, [1, 2, 3])

    def testAssertIsInstance(self):
        self.assertIsInstance("42", str)

    def testAsserNotIsInstance(self):
        self.assertNotIsInstance(42, str)

    def testAssertAlmostEqual(self):
        self.assertAlmostEqual(22.0/7,3.14 , places = 2)

    def testAssertNotAlmostEqual(self):
        self.assertNotAlmostEqual(10.0 / 3, 3, places = 2)

    def testAssertGreater(self):
        self.assertGreater(7, 2)

    def testAssertLess(self):
        self.assertLess(2, 7)

    def testAssertGreaterEqual(self):
        self.assertGreaterEqual(9, 9)

    def testAssertLessEqual(self):
        self.assertLessEqual(2, 2)

    def testAssertListEqual(self):
        self.assertListEqual([1, 2, 3, 4], [1, 2, 3, 4])

    def testAssertSetEqual(self):
        self.assertSetEqual(set([1,2,3,4]), set([4,3,2,1]))

    def testAssertDictEqual(self):
        self.assertDictEqual({'a': 1, 'b': 2}, {'b': 2, 'a': 1})

if __name__ == 'main':
    unittest.main()

# 6. Let's write one more problem: Create basic test on employee class Employee class has three parameters
# firstname, last name and pay.
# 7. Improve the test file for employee with fixtures.

