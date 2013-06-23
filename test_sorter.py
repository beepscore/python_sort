#!/usr/bin/env python3

import sorter
import unittest

class TestSorter(unittest.TestCase):

    def setUp(self):
        # instantiate object from module sorter, class Sorter
        self.sorter = sorter.Sorter()

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
            result = self.sorter.number_of_non_leaf_nodes(test_data[list_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'number_of_non_leaf_nodes({}) expected {} but got {}'.format(test_data[list_index],
                                                                                      test_data[expected_result_index],
                                                                                      result))

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

    def test_list_elements_swapped(self):

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
            result = self.sorter.list_elements_swapped(test_data[list_index],
                                                       test_data[indexA_index],
                                                       test_data[indexB_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'list_elements_swapped({}, {}, {}) expected {} but got {}'.format(test_data[list_index],
                                                                                               test_data[indexA_index],
                                                                                               test_data[indexB_index],
                                                                                               test_data[expected_result_index],
                                                                                               result))

    def test_is_max_heap(self):

        list_index = 0
        expected_result_index = 1

        test_datas = [
            [[], True],
            [[3], True],
            [[3, 2], True],
            [[3, 2, 1], True],
            [[38, 23, 35, 10], True],
            [[38, 23, 35, 10, 20], True],
            [[38, 23, 35, 10, 20, 17], True],
            [[38, 23, 35, 10, 20, 17, 12], True],
            [[38, 23, 35, 10, 20, 17, 12, 8], True],
            [[38, 23, 35, 10, 20, 17, 12, 8, 9], True],

            # test with repeated values
            [[3, 3], True],

            # test non max heaps
            [[3, 4], False],
            [[38, 99, 35, 10, 20, 17, 12, 8, 9], False],
            [[38, 23, 35, 10, 99, 17, 12, 8, 9], False],
            [[38, 23, 35, 10, 20, 17, 12, 99, 9], False],
        ]

        for test_data in test_datas:
            result = self.sorter.is_max_heap(test_data[list_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'is_max_heap({}) expected {} but got {}'.format(test_data[list_index],
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
            [[49, 38, 35, 10, 20, 37], 2, True],
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

    def test_index_of_biggest_child(self):

        list_index = 0
        # in test_datas, the index that contains the list_index
        list_index_index = 1
        expected_result_index = 2

        test_datas = [
            [[23], 0, None],
            [[23, 38, 35, 10, 20, 17, 12], None, None],
            [[23, 38, 35, 10, 20, 17, 12], 0, 1],
            [[23, 38, 35, 10, 20, 17, 12], 1, 4],
            [[23, 38, 35, 10, 20, 17, 12], 2, 5],
            [[49, 38, 35, 10, 20, 37], 2, 5],
        ]

        for test_data in test_datas:
            result = self.sorter.index_of_biggest_child(test_data[list_index],
                                                        test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'index_of_biggest_child({}, {}) expected {} but got {}'.format(test_data[list_index],
                                                                                             test_data[list_index_index],
                                                                                             test_data[expected_result_index],
                                                                                             result))

    def test_heapify(self):

        almost_heap_index = 0
        # in test_datas, the index that contains the list_index
        list_index_index = 1
        expected_result_index = 2

        test_datas = [
            # one element
            [[5], 0, [5]],
            # heap needs one swap
            [[2, 3, 1], 0, [3, 2, 1]],
            [[23, 78, 65, 10, 20, 17, 12], 2, [78, 23, 65, 10, 20, 17, 12]],
            [[78, 43, 65, 10, 57, 37, 12], 2, [78, 57, 65, 10, 43, 37, 12]],
            [[76, 62, 52, 44, 32, 23, 58], 2, [76, 62, 58, 44, 32, 23, 52]],

            # heap needs one element swapped up 2 levels
            [[76, 62, 58, 44, 32, 23, 98], 2, [98, 62, 76, 44, 32, 23, 58]],

            # heap needs 2 elements swapped, heapify doesn't handle this
            #[[12, 25, 35, 10, 23, 17, 38], 2, [38, 25, 35, 10, 35, 17, 23]],

            # heap is a max heap, needs no swaps.
            [[38, 23, 35, 10, 20, 17, 12], 2, [38, 23, 35, 10, 20, 17, 12]],
            [[38, 23, 35, 10, 20, 17, 12], 2, [38, 23, 35, 10, 20, 17, 12]],
            [[38, 23, 35, 10, 20, 17, 12], 2, [38, 23, 35, 10, 20, 17, 12]],
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
