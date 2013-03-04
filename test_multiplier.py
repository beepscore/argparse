#!/usr/bin/env python3

import multiplier
import unittest

class TestMultiplier(unittest.TestCase):

    multiplicand_index = 0
    multiplier_index = 1
    expected_result_index = 2

    test_datas = [
        [0,0,0],
        [1,0,0],
        [0,1,0],
        [1,1,1],
        [2,1,2],
        [1,2,2],
        [2,3,6],
        [6,7,42],
        [-6,7,-42],
        [12,-5,-60],
    ]

    def setUp(self):
        pass

    def test_multiply(self):

        for test_data in self.test_datas:
            # module multiplier, class Multiplier, method multiply(a, b)
            result = multiplier.Multiplier.multiply(test_data[self.multiplicand_index],
                                                    test_data[self.multiplier_index])
            self.assertEqual(test_data[self.expected_result_index], result,
                             'multiply({}, {}) expected {} but got {}'.format(test_data[self.multiplicand_index],
                                                                              test_data[self.multiplier_index],
                                                                              test_data[self.expected_result_index],
                                                                              result))

    def test_multiply_iterative(self):

        for test_data in self.test_datas:
            # module multiplier, class Multiplier, method multiply_iterative(a, b)
            result = multiplier.Multiplier.multiply_iterative(test_data[self.multiplicand_index],
                                                              test_data[self.multiplier_index])
            self.assertEqual(test_data[self.expected_result_index], result,
                             'multiply_iterative({}, {}) expected {} but got {}'.format(test_data[self.multiplicand_index],
                                                                                        test_data[self.multiplier_index],
                                                                                        test_data[self.expected_result_index],
                                                                                        result))

if __name__ == "__main__": unittest.main()
