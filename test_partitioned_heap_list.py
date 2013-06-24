#!/usr/bin/env python3

import partitioned_heap_list
import unittest

class TestPartitionedHeapList(unittest.TestCase):

    def setUp(self):
        # instantiate object from module partitioned_heap, class PartitionedHeapList
        self.partitioned_heap_list = partitioned_heap_list.PartitionedHeapList()

    def test_number_of_non_leaf_nodes(self):

        list_index = 0
        expected_result_index = 1

        test_datas = [
            [[], 0],
            [[3], 0],
            [[3, 2], 1],
            [[3, 2, 1], 1],
            [[38, 23, 35, 10], 3],
            [[38, 23, 35, 10, 20], 3],
            [[38, 23, 35, 10, 20, 17], 3],
            [[38, 23, 35, 10, 20, 17, 12], 3],
            [[38, 23, 35, 10, 20, 17, 12, 8], 7],
            [[38, 23, 35, 10, 20, 17, 12, 8, 9], 7],
        ]

        for test_data in test_datas:
            self.partitioned_heap_list = partitioned_heap_list.PartitionedHeapList(test_data[list_index], (len(test_data[list_index])-1))
            result = self.partitioned_heap_list.number_of_non_leaf_nodes()
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'number_of_non_leaf_nodes({}) expected {} but got {}'.format(test_data[list_index],
                                                                                      test_data[expected_result_index],
                                                                                      result))

if __name__ == "__main__": unittest.main()
