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

    def number_of_non_leaf_nodes(self, heap_list):
        '''
        returns number of nodes on levels above lowest level of heap_list tree.
        if heap_list has one node, returns 1.

        '''
        number_of_non_leaf_nodes = 0
        if (None == heap_list) or ([] == heap_list):
            number_of_non_leaf_nodes = 0
        else:
            # number of levels in the heap tree
            # log2 requires Python 3.3
            number_of_levels = int(math.log2(len(heap_list))) + 1
            number_of_non_leaf_nodes = ((2**(number_of_levels - 1)) - 1)
        return number_of_non_leaf_nodes

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

    def is_max_heap(self, heap_list):
        '''
        returns True if heap_list is a max heap.

        '''
        is_max_heap = True
        # Iterate over non leaf nodes. Leaf nodes don't have children, don't need to check them.
        # Python range() is exclusive of final value
        for index in range(0, self.number_of_non_leaf_nodes(heap_list)):
            if self.node_has_a_bigger_child(heap_list, index):
                is_max_heap = False
                break

        return is_max_heap

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

    def heapify(self, heap_list, start_index):
        '''
        heapify starts searching at start_index and decrements index.
        If heapify finds a node with a bigger child, it swaps the nodes.
        To reduce time complexity, it then changes index to parent.
        It does not explore other branches.

        argument heap_list is a list that almost represents a max heap, but one node is wrong.

        returns a max heap list

        '''
        # decrement index
        # range() is exclusive of end index
        for index in range(start_index, -1, -1):

            if self.node_has_a_bigger_child(heap_list, index):
                print('heap_list {}'.format(heap_list))
                print('index {}'.format(index))

                parent_index = self.parent_index(heap_list, index)
                print('parent_index {}'.format(parent_index))
                biggest_child_index = self.index_of_biggest_child(heap_list, index)
                print('biggest_child_index {}'.format(biggest_child_index))

                heap_list = self.list_elements_swapped(heap_list,
                                                       index,
                                                       biggest_child_index)

                # skip other tree branches, move index to parent
                index = parent_index

        return heap_list

    def heap_sort(self, heap_list):
        '''
        argument heap_list is a max heap
        returns a list sorted in ascending order
        Could use Python sort() method instead. Wrote heap_sort as a learning exercise.

        '''

        # sort in place
        # partition list into 2 sections
        # range(0, sorted_start_index) contains a max heap. range is exclusive.
        # range(sorted_start_index, len(heap_list)) contains the sorted list.
        heap_length = len(heap_list)
        # In current heap swap root with last leaf node.
        # Then adjust sorted_start_index
        heap_list = self.list_elements_swapped(heap_list, 0, (heap_length - 1))


        return heap_list

