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
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            result = self.partitioned_heap_list.right_child_index(test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} right_child_index({}) expected {} but got {}'.format(test_data[list_index],
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
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            result = self.partitioned_heap_list.left_child_index(test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} left_child_index({}) expected {} but got {}'.format(test_data[list_index],
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
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            result = self.partitioned_heap_list.parent_index(test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} parent_index({}) expected {} but got {}'.format(test_data[list_index],
                                                                                                  test_data[list_index_index],
                                                                                                  test_data[expected_result_index],
                                                                                                  result))

    def test_swap_list_elements(self):

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
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            self.partitioned_heap_list.swap_list_elements(test_data[indexA_index], test_data[indexB_index])
            result = self.partitioned_heap_list.partitioned_list
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} swap_list_elements({}, {}) expected {} but got {}'.format(test_data[list_index],
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
            [[49, 38, 35, 10, 20, 37], 2, True],
        ]

        for test_data in test_datas:
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            result = self.partitioned_heap_list.node_has_a_bigger_child(test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} node_has_a_bigger_child({}) expected {} but got {}'.format(test_data[list_index],
                                                                                                             test_data[list_index_index],
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
            # if list is empty, this attempts to set heap_end_index < 0 and throws assertion error.
            #self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            # Instead use initializer, it will set heap_end_index 0
            self.partitioned_heap_list = partitioned_heap_list.PartitionedHeapList(test_data[list_index], (len(test_data[list_index])-1))

            result = self.partitioned_heap_list.is_max_heap()
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} is_max_heap() expected {} but got {}'.format(test_data[list_index],
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
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            result = self.partitioned_heap_list.index_of_biggest_child(test_data[list_index_index])
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} index_of_biggest_child({}) expected {} but got {}'.format(test_data[list_index],
                                                                                                            test_data[list_index_index],
                                                                                                            test_data[expected_result_index],
                                                                                                            result))

    def test_sift_down(self):

        list_index = 0
        start_index_index = 1
        expected_result_index = 2

        # Can check test_datas by hand drawing heap trees
        test_datas = [
            # heap is a max heap, needs no swaps.
            [[5], 0, [5]],
            [[88, 55, 66, 44, 22, 11, 3], 0, [88, 55, 66, 44, 22, 11, 3]],

            # heap needs root node swapped down 1 level
            [[2, 3, 1], 0, [3, 2, 1]],
            [[55, 88, 66, 44, 22, 11, 3], 0, [88, 55, 66, 44, 22, 11, 3]],

            # heap needs root node swapped down 2 levels
            [[33, 88, 66, 44, 22, 11, 3], 0, [88, 44, 66, 33, 22, 11, 3]],
            [[48, 99, 88, 66, 77, 55, 44, 22, 33, 12, 8], 0, [99, 77, 88, 66, 48, 55, 44, 22, 33, 12, 8]],

            # heap needs root node swapped down 3 levels
            [[7, 99, 88, 66, 77, 55, 44, 22, 33, 12, 8], 0, [99, 77, 88, 66, 12, 55, 44, 22, 33, 7, 8]],
        ]

        for test_data in test_datas:
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            self.partitioned_heap_list.sift_down(test_data[start_index_index])
            result = self.partitioned_heap_list.partitioned_list
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} sift_down({}) expected {} but got {}'.format(test_data[list_index],
                                                                                  test_data[start_index_index],
                                                                                  test_data[expected_result_index],
                                                                                  result))

            # this assertion is dependent upon is_max_heap()
            self.assertTrue(self.partitioned_heap_list.is_max_heap(),
                             'partitioned_list {} sift_down({}) expected a max heap'.format(test_data[list_index],
                                                                                               test_data[start_index_index]))

    def test_sift_up(self):

        list_index = 0
        # in test_datas, the index that contains the start_index
        start_index_index = 1
        expected_result_index = 2

        test_datas = [
            # heap is a max heap, needs no swaps.
            # one element
            [[5], 0, [5]],
            [[38, 23, 35, 10, 20, 17, 12], 2, [38, 23, 35, 10, 20, 17, 12]],

            # heap needs one swap
            [[2, 3, 1], 0, [3, 2, 1]],
            [[23, 78, 65, 10, 20, 17, 12], 2, [78, 23, 65, 10, 20, 17, 12]],

            [[78, 43, 65, 10, 57, 37, 12], 2, [78, 57, 65, 10, 43, 37, 12]],
            [[76, 62, 52, 44, 32, 23, 58], 2, [76, 62, 58, 44, 32, 23, 52]],
            # heap needs one element swapped up 2 levels
            [[76, 62, 58, 44, 32, 23, 98], 2, [98, 62, 76, 44, 32, 23, 58]],
        ]

        for test_data in test_datas:
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            self.partitioned_heap_list.sift_up(test_data[start_index_index])
            result = self.partitioned_heap_list.partitioned_list
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} sift_up({}) expected {} but got {}'.format(test_data[list_index],
                                                                                  test_data[start_index_index],
                                                                                  test_data[expected_result_index],
                                                                                  result))

            # this assertion is dependent upon is_max_heap()
            self.assertTrue(self.partitioned_heap_list.is_max_heap(),
                             'partitioned_list {} sift_up({}) expected a max heap'.format(test_data[list_index],
                                                                                             test_data[start_index_index]))

    def test_heapify(self):

        list_index = 0
        start_index_index = 1
        expected_result_index = 2

        test_datas = [
            # heap is a max heap, needs no swaps.
            # one element
            [[5], 0, [5]],
            [[38, 23, 35, 10, 20, 17, 12], 2, [38, 23, 35, 10, 20, 17, 12]],

            # heap needs one swap
            [[2, 3, 1], 0, [3, 2, 1]],
            [[23, 78, 65, 10, 20, 17, 12], 2, [78, 23, 65, 10, 20, 17, 12]],
            [[78, 43, 65, 10, 57, 37, 12], 2, [78, 57, 65, 10, 43, 37, 12]],
            [[76, 62, 52, 44, 32, 23, 58], 2, [76, 62, 58, 44, 32, 23, 52]],

            # heap needs one element swapped up 2 levels
            [[76, 62, 58, 44, 32, 23, 98], 2, [98, 62, 76, 44, 32, 23, 58]],

            # heap needs 2 elements swapped
            [[12, 25, 35, 10, 23, 17, 38], 2, [38, 25, 35, 10, 23, 17, 12]],

            # list is ascending, needs all but one element swapped
            [[10, 20, 30, 40, 50, 60, 70], 2, [70, 50, 60, 40, 20, 10, 30]],
        ]

        for test_data in test_datas:
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            self.partitioned_heap_list.heapify(test_data[start_index_index])
            result = self.partitioned_heap_list.partitioned_list
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} heapify({}) expected {} but got {}'.format(test_data[list_index],
                                                                                             test_data[start_index_index],
                                                                                             test_data[expected_result_index],
                                                                                             result))

            # this assertion is dependent upon is_max_heap()
            self.assertTrue(self.partitioned_heap_list.is_max_heap(),
                             'partitioned_list {} heapify({}) expected a max heap'.format(test_data[list_index],
                                                                                          test_data[start_index_index]))

    def test_heapify_up(self):

        list_index = 0
        expected_result_index = 1

        test_datas = [
            # heap is a max heap, needs no swaps.
            # one element
            [[5], [5]],
            [[38, 23, 35, 10, 20, 17, 12], [38, 23, 35, 10, 20, 17, 12]],

            # heap needs one swap
            [[2, 3, 1], [3, 2, 1]],
            [[23, 78, 65, 10, 20, 17, 12], [78, 23, 65, 10, 20, 17, 12]],
            [[78, 43, 65, 10, 57, 37, 12], [78, 57, 65, 10, 43, 37, 12]],
            [[76, 62, 52, 44, 32, 23, 58], [76, 62, 58, 44, 32, 23, 52]],

            # heap needs one element swapped up 2 levels
            [[76, 62, 58, 44, 32, 23, 98], [98, 62, 76, 44, 32, 23, 58]],

            # heap needs 2 elements swapped
            [[12, 25, 35, 10, 23, 17, 38], [38, 25, 35, 10, 23, 17, 12]],

            # list is ascending, needs all but one element swapped
            # TODO: fix heapify_up() to pass this test
            [[10, 20, 30, 40, 50, 60, 70], [70, 50, 60, 40, 20, 10, 30]],
        ]

        for test_data in test_datas:
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            self.partitioned_heap_list.heapify_up()
            result = self.partitioned_heap_list.partitioned_list
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} heapify_up() expected {} but got {}'.format(test_data[list_index],
                                                                                             test_data[expected_result_index],
                                                                                             result))

            # this assertion is dependent upon is_max_heap()
            self.assertTrue(self.partitioned_heap_list.is_max_heap(),
                             'partitioned_list {} heapify_up() expected a max heap'.format(test_data[list_index]))

    def test_heap_sort(self):

        list_index = 0
        expected_result_index = 1

        test_datas = [
            # one element
            [[5], [5]],

            [[2, 1], [1, 2]],
            [[3, 2, 1], [1, 2, 3]],
            [[88, 55, 66, 44, 22, 11, 3], [3, 11, 22, 44, 55, 66, 88]],
            [[99, 77, 88, 66, 12, 55, 44, 22, 33, 7, 8], [7, 8, 12, 22, 33, 44, 55, 66, 77, 88, 99]],
        ]

        # expected heap_end_index after heap_sort finishes
        expected_heap_end_index = -1

        for test_data in test_datas:
            self.partitioned_heap_list.partitioned_list = test_data[list_index]
            self.partitioned_heap_list.heap_end_index = len(test_data[list_index]) - 1
            self.partitioned_heap_list.heap_sort()
            result = self.partitioned_heap_list.partitioned_list
            self.assertEqual(test_data[expected_result_index],
                             result,
                             'partitioned_list {} heap_sort() expected {} but got {}'.format(test_data[list_index],
                                                                                             test_data[expected_result_index],
                                                                                             result))


            self.assertEqual(expected_heap_end_index, self.partitioned_heap_list.heap_end_index,
                             'partitioned_list {} heap_sort() expected heap_end_index == {}'.format(test_data[list_index], expected_heap_end_index))

if __name__ == "__main__": unittest.main()
