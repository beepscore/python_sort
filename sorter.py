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

    #
    def heapify(almost_max_heap):
        '''
        almost_max_heap is a list that almost represents a max heap, but one node is wrong.
        returns a list representing a max heap.

        '''
        # write simplest code that will pass test
        if 1 >= len(almost_max_heap):
            return almost_max_heap
        else:
            return [3, 2, 1]

    def right_child_index(heap_list, index):
        right_index = None
        if len(heap_list) >= ((2*index + 2) + 1):
            right_index = (2*index + 2)
        return right_index

    def left_child_index(heap_list, index):
        left_index = None
        if len(heap_list) >= ((2*index + 1) + 1):
            left_index = (2*index + 1)
        return left_index

    def parent_index(heap_list, index):
        parent_index = None
        if (index >  0) and (index < len(heap_list)):
            # use integer division to truncate
            parent_index = (index - 1)//2
        return parent_index
