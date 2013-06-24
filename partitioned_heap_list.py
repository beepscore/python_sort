#!/usr/bin/env python3

import math

class PartitionedHeapList():
    '''

    Properties:
    # partitioned_list is a Python list (an array).
    # heap_end_index partitions partitioned_list into 2 sections, a max heap and a sorted list.

    The max heap occupies range(0, (heap_end_index+1)). range is exclusive of second argument.

    The sorted list occupies range((heap_end_index+1), len(partitioned_list)).
    The sorted list is sorted in ascending order.

    This class could be written in a more object oriented way e.g. heapA.nodeB.left_child().
    Instead use a Python list to allow for easier conversion to other mappings.

    max_heap represents a heap by mapping array indices to node positions from top to bottom, left to right

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

    def __init__(self, partitioned_list = [], heap_end_index = 0):

        self._partitioned_list = partitioned_list

        # protect against instantiating out of bounds
        if ([] == partitioned_list):
            self._heap_end_index = 0
        else:
            assert(heap_end_index >= 0)
            assert(heap_end_index < len(self.partitioned_list))
            self._heap_end_index = heap_end_index

    def get_partitioned_list(self):
        return self._partitioned_list

    def set_partitioned_list(self, partitioned_list):
        self._partitioned_list = partitioned_list

    partitioned_list = property (get_partitioned_list, set_partitioned_list)

    def get_heap_end_index(self):
        return self._heap_end_index

    def set_heap_end_index(self, heap_end_index):
        # protect against assigning out of bounds
        assert(heap_end_index >= 0)
        assert(heap_end_index < len(self.partitioned_list))
        self._heap_end_index = heap_end_index

    heap_end_index = property (get_heap_end_index, set_heap_end_index)

    def number_of_non_leaf_nodes(self):
        '''
        returns number of nodes on levels above lowest level of max_heap tree.
        if heap_length equals one, returns 1.

        '''
        number_of_non_leaf_nodes = 0
        if (None == self.partitioned_list) or ([] == self.partitioned_list):
            number_of_non_leaf_nodes = 0
        else:
            # number of levels in the heap tree
            # log2 requires Python 3.3
            heap_length = self.heap_end_index + 1
            number_of_levels = int(math.log2(heap_length)) + 1
            number_of_non_leaf_nodes = ((2**(number_of_levels - 1)) - 1)

        return number_of_non_leaf_nodes

    def right_child_index(self, index):
        right_index = None
        if (index != None) and (self.heap_end_index >= (2*index + 2)):
            right_index = (2*index + 2)
        return right_index

    def left_child_index(self, index):
        left_index = None
        if (index != None) and (self.heap_end_index >= (2*index + 1)):
            left_index = (2*index + 1)
        return left_index

    def parent_index(self, index):
        parent_index = None
        if (index != None) and (index > 0) and (index <= self.heap_end_index):
            # use integer division to truncate
            parent_index = (index - 1)//2
        return parent_index

    def swap_list_elements(self, indexA, indexB):
        '''
        swaps elements in partitioned_list

        '''
        # Python can swap in one step
        self.partitioned_list[indexA], self.partitioned_list[indexB] = self.partitioned_list[indexB], self.partitioned_list[indexA]

