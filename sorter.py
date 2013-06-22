#!/usr/bin/env python3

class Sorter():
    '''
    Sort a list using heap sort.

    This class could be written in a more object oriented way e.g. heapA.nodeB.left_child().
    Instead use array (Python list) to allow for easier conversion to other mappings.

    To represent a heap as an array, map node positions to array index
    For a zero based array,

                0
              /   \
             /     \
            1       2
           / \     / \
          3   4   5   6

    A[0] root
    A[1] left child of root
    A[2] right child of root
    In general, for heap node at index i,
    A[(i-1)//2] parent node index, using integer division to truncate
    A[2i+1] left child
    A[2i+2] right child

    '''

    def __init__(self):
        pass

    def heapify(self, almost_max_heap):
        '''
        almost_max_heap is a list that almost represents a max heap, but one node is wrong.
        returns a list representing a max heap.

        '''
        max_heap = []

        # write simplest code that will pass test
        if 1 >= len(almost_max_heap):
            max_heap = almost_max_heap
        else:
            current_index = 0
            if almost_max_heap[self.left_child_index(almost_max_heap, current_index)] > almost_max_heap[current_index]:
                # swap_list_elements_at_indices(list, indexA, indexB)
                pass

        return max_heap
    def right_child_index(self, heap_list, index):
        right_index = None
        if len(heap_list) >= ((2*index + 2) + 1):
            right_index = (2*index + 2)
        return right_index

    def left_child_index(self, heap_list, index):
        left_index = None
        if len(heap_list) >= ((2*index + 1) + 1):
            left_index = (2*index + 1)
        return left_index

    def parent_index(self, heap_list, index):
        parent_index = None
        if (index >  0) and (index < len(heap_list)):
            # use integer division to truncate
            parent_index = (index - 1)//2
        return parent_index

    def swap_list_elements_at_indices(self, heap_list, indexA, indexB):
        temp = heap_list[indexA]
        heap_list[indexA] = heap_list[indexB]
        heap_list[indexB] = temp
        return heap_list

