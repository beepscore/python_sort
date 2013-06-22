#!/usr/bin/env python3

import sorter
import unittest

class TestSorter(unittest.TestCase):

    def setUp(self):
        # instantiate object from module sorter, class Sorter
        self.sorter = sorter.Sorter()

    def test_right_child_index(self):

        list_index = 0
        # in test_datas, the index that contains the list_index
        list_index_index = 1
        expected_result_index = 2

        test_datas = [
            [[3], 0, None],
            [[3, 2, 1], 0, 2],
            [[3, 2, 1], 1, None],
            [[38, 23, 35, 10, 20, 17, 12], 0, 2],
            [[38, 23, 35, 10, 20, 17, 12], 1, 4],
            [[38, 23, 35, 10, 20, 17, 12], 2, 6],
            [[38, 23, 35, 10, 20, 17, 12], 3, None],
            [[38, 23, 35, 10, 20, 17, 12], 4, None],
            [[38, 23, 35, 10, 20, 17, 12], 5, None],
            [[38, 23, 35, 10, 20, 17, 12], 6, None],
        ]

        for test_data in test_datas:
            result = self.sorter.right_child_index(test_data[list_index],
                                                   test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'right_child_index({}, {}) expected {} but got {}'.format(test_data[list_index],
                                                                                      test_data[list_index_index],
                                                                                      test_data[expected_result_index],
                                                                                      result))

    def test_left_child_index(self):

        list_index = 0
        # in test_datas, the index that contains the list_index
        list_index_index = 1
        expected_result_index = 2

        test_datas = [
            [[3], 0, None],
            [[3, 2, 1], 0, 1],
            [[3, 2, 1], 1, None],
            [[38, 23, 35, 10, 20, 17, 12], 0, 1],
            [[38, 23, 35, 10, 20, 17, 12], 1, 3],
            [[38, 23, 35, 10, 20, 17, 12], 2, 5],
            [[38, 23, 35, 10, 20, 17, 12], 3, None],
            [[38, 23, 35, 10, 20, 17, 12], 4, None],
            [[38, 23, 35, 10, 20, 17, 12], 5, None],
            [[38, 23, 35, 10, 20, 17, 12], 6, None],

            # test with index beyond array bounds
            [[38, 23, 35, 10, 20, 17, 12], 73, None],
        ]

        for test_data in test_datas:
            result = self.sorter.left_child_index(test_data[list_index],
                                                  test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'left_child_index({}, {}) expected {} but got {}'.format(test_data[list_index],
                                                                                      test_data[list_index_index],
                                                                                      test_data[expected_result_index],
                                                                                      result))

    def test_parent_index(self):

        list_index = 0
        # in test_datas, the index that contains the list_index
        list_index_index = 1
        expected_result_index = 2

        test_datas = [
            [[3], 0, None],
            [[3, 2, 1], 0, None],
            [[3, 2, 1], 1, 0],
            [[3, 2, 1], 2, 0],
            [[38, 23, 35, 10, 20, 17, 12], 0, None],
            [[38, 23, 35, 10, 20, 17, 12], 1, 0],
            [[38, 23, 35, 10, 20, 17, 12], 2, 0],
            [[38, 23, 35, 10, 20, 17, 12], 3, 1],
            [[38, 23, 35, 10, 20, 17, 12], 4, 1],
            [[38, 23, 35, 10, 20, 17, 12], 5, 2],
            [[38, 23, 35, 10, 20, 17, 12], 6, 2],

            # test with index beyond array bounds
            [[38, 23, 35, 10, 20, 17, 12], 73, None],
        ]

        for test_data in test_datas:
            result = self.sorter.parent_index(test_data[list_index],
                                              test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'parent_index({}, {}) expected {} but got {}'.format(test_data[list_index],
                                                                                  test_data[list_index_index],
                                                                                  test_data[expected_result_index],
                                                                                  result))

    def test_swap_list_elements_at_indices(self):

        list_index = 0
        indexA_index = 1
        indexB_index = 2
        expected_result_index = 3

        test_datas = [
            # swap an element with itself
            [[23, 38, 35, 10, 20, 17, 12], 0, 0, [23, 38, 35, 10, 20, 17, 12]],

            [[23, 38, 35, 10, 20, 17, 12], 0, 1, [38, 23, 35, 10, 20, 17, 12]],
            [[23, 38, 35, 10, 20, 17, 12], 0, 2, [35, 38, 23, 10, 20, 17, 12]],
            [[23, 38, 35, 10, 20, 17, 12], 3, 6, [23, 38, 35, 12, 20, 17, 10]],
        ]

        for test_data in test_datas:
            result = self.sorter.swap_list_elements_at_indices(test_data[list_index],
                                                               test_data[indexA_index],
                                                               test_data[indexB_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'swap_list_elements_at_indices({}, {}, {}) expected {} but got {}'.format(test_data[list_index],
                                                                                                       test_data[indexA_index],
                                                                                                       test_data[indexB_index],
                                                                                                       test_data[expected_result_index],
                                                                                                       result))

    def test_node_has_a_bigger_child(self):

        list_index = 0
        # in test_datas, the index that contains the list_index
        list_index_index = 1
        expected_result_index = 2

        test_datas = [
            [[23], 0, False],
            [[23, 38, 35, 10, 20, 17, 12], 0, True],
            [[23, 38, 35, 10, 20, 17, 12], 1, False],
            [[23, 38, 35, 10, 20, 17, 12], 2, False],
        ]

        for test_data in test_datas:
            result = self.sorter.node_has_a_bigger_child(test_data[list_index],
                                                               test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'node_has_a_bigger_child({}, {}) expected {} but got {}'.format(test_data[list_index],
                                                                                             test_data[list_index_index],
                                                                                             test_data[expected_result_index],
                                                                                             result))

    def test_heapify(self):

        almost_heap_index = 0
        # in test_datas, the index that contains the list_index
        list_index_index = 1
        expected_result_index = 2

        test_datas = [
            [[5], 0, [5]],
            [[2, 3, 1], 0, [3, 2, 1]],
        ]

        for test_data in test_datas:
            result = self.sorter.heapify(test_data[almost_heap_index],
                                         test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'heapify({}, {}) expected {} but got {}'.format(test_data[almost_heap_index],
                                                                             test_data[list_index_index],
                                                                             test_data[expected_result_index],
                                                                        result))

if __name__ == "__main__": unittest.main()
