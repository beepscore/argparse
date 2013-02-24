#!/usr/bin/env python3

import multiplier
import unittest

class TestMultiplier(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiply(self):
        a = 0
        b = 0
        expected_result = 0
        # module multiplier, class Multiplier, method multiply(a, b)
        result = multiplier.Multiplier.multiply(a, b)
        self.assertEqual(expected_result, result,
                         'multiply({}, {}) expected {} but got {}'.format(a, b, expected_result, result))

        a = 1
        b = 1
        expected_result = 1
        result = multiplier.Multiplier.multiply(a, b)
        self.assertEqual(expected_result, result,
                         'multiply({}, {}) expected {} but got {}'.format(a, b, expected_result, result))

    def test_multiply_iterative(self):
        a = 7
        b = 9
        expected_result = 63
        # module multiplier, class Multiplier, method multiply_iterative(a, b)
        result = multiplier.Multiplier.multiply_iterative(a, b)
        self.assertEqual(expected_result, result,
                         'multiply_iterative({}, {}) expected {} but got {}'.format(a, b, expected_result, result))

if __name__ == "__main__": unittest.main()
