#!/usr/bin/env python3

import sorter
import unittest

class TestSorter(unittest.TestCase):

    def setUp(self):
        pass

    def test_heapify(self):

        # module sorter, class Sorter, method heapify()
        # root is 2, children are 3, 1
        test_almost_max_heap = [2, 3, 1]
        expected_heap = [3, 2, 1]
        result = sorter.Sorter.heapify(test_almost_max_heap)

        self.assertEqual(expected_heap, result,
                            'heapify({}) expected {} but got {}'.format(test_almost_max_heap,
                                                                        expected_heap,
                                                                        result))

if __name__ == "__main__": unittest.main()
