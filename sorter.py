#!/usr/bin/env python3

import math

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

    def number_of_leaf_nodes(self, heap_list):
        '''
        returns number of nodes on lowest level of heap_list tree.
        if heap_list has one node, returns 1.

        '''
        number_of_leaf_nodes = 0
        if (None == heap_list) or (0 == len(heap_list)):
            number_of_leaf_nodes = 0
        else:
            # log2 requires Python 3.3
            # number of levels in the heap tree
            number_of_levels = int(math.log2(len(heap_list))) + 1
            number_of_leaf_nodes = len(heap_list) - ((2**(number_of_levels - 1)) - 1)
            # print('heap_list {}'.format(heap_list))
            # print('number_of_levels {} number_of_leaf_nodes {}'.format(number_of_levels, number_of_leaf_nodes))
        return number_of_leaf_nodes

    def right_child_index(self, heap_list, index):
        right_index = None
        if (index != None) and len(heap_list) >= ((2*index + 2) + 1):
            right_index = (2*index + 2)
        return right_index

    def left_child_index(self, heap_list, index):
        left_index = None
        if (index != None) and len(heap_list) >= ((2*index + 1) + 1):
            left_index = (2*index + 1)
        return left_index

    def parent_index(self, heap_list, index):
        parent_index = None
        if (index != None) and (index >  0) and (index < len(heap_list)):
            # use integer division to truncate
            parent_index = (index - 1)//2
        return parent_index

    def list_elements_swapped(self, heap_list, indexA, indexB):
        '''
        returns a list with elements swapped

        '''
        # Python can swap in one step
        #temp = heap_list[indexA]
        #heap_list[indexA] = heap_list[indexB]
        #heap_list[indexB] = temp
        heap_list[indexA], heap_list[indexB] = heap_list[indexB], heap_list[indexA]
        return heap_list

    # TODO: consider eliminate this method, just use index_of_biggest_child
    def node_has_a_bigger_child(self, heap_list, index):
        '''
        returns True if node at index has a bigger child

        '''
        left_child_index = self.left_child_index(heap_list, index)
        right_child_index = self.right_child_index(heap_list, index)

        if ((left_child_index and (heap_list[index] < heap_list[left_child_index])) or
            (right_child_index and (heap_list[index] < heap_list[right_child_index]))):
            return True;
        else:
            return False;

    def index_of_biggest_child(self, heap_list, index):
        left_child_index = self.left_child_index(heap_list, index)
        right_child_index = self.right_child_index(heap_list, index)

        biggest_child_index = None
        if (not left_child_index and not right_child_index):
            biggest_child_index = None
        elif (left_child_index and not right_child_index):
            biggest_child_index = left_child_index
        elif (right_child_index and not left_child_index):
            biggest_child_index = right_child_index
        else:
            # index has two children
            if (heap_list[left_child_index] > heap_list[right_child_index]):
                biggest_child_index = left_child_index
            else:
                biggest_child_index = right_child_index

        return biggest_child_index;

    def heapify(self, heap_list, index):
        '''
        heap_list is a list that almost represents a max heap, but one node is wrong.
        returns a list with node swapped

        '''
        if ((len(heap_list) > 1) and
            self.node_has_a_bigger_child(heap_list, index)):
            self.list_elements_swapped(heap_list,
                                       index,
                                       self.index_of_biggest_child(heap_list, index))

        return heap_list

