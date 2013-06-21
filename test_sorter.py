#!/usr/bin/env python3

import sorter
import unittest

class TestSorter(unittest.TestCase):

    def setUp(self):
        pass

    def test_heapify(self):

        almost_heap_index = 0
        expected_result_index = 1

        test_datas = [
            [[5], [5]],
            [[2, 3, 1], [3, 2, 1]],
        ]

        for test_data in test_datas:
            # module sorter, class Sorter, method heapify()
            result = sorter.Sorter.heapify(test_data[almost_heap_index])
            self.assertEqual(test_data[expected_result_index],
                            result,
                            'heapify({}) expected {} but got {}'.format(test_data[almost_heap_index],
                                                                        test_data[expected_result_index],
                                                                        result))

if __name__ == "__main__": unittest.main()
