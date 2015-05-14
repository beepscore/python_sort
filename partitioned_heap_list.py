#!/usr/bin/env python3

import math


class PartitionedHeapList():
    '''

    Properties:
    partitioned_list is a Python list (an array).
    heap_end_index partitions partitioned_list into 2 sections,
    a max heap and a sorted list.

    The max heap occupies range(0, (heap_end_index+1)).
    range is exclusive of second argument.

    The sorted list occupies range((heap_end_index+1), len(partitioned_list)).
    The sorted list is sorted in ascending order.

    This class could be written in a more object oriented way
    e.g. heapA.nodeB.left_child().
    Instead use a Python list to allow for easier conversion to other mappings.

    max_heap represents a heap by mapping array indices to node positions
    from top to bottom, left to right

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

    References
    https://en.wikipedia.org/wiki/Heapsort
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    http://stackoverflow.com/questions/8954564/binary-heap-how-and-when-to-use-max-heapify?rq=1
    http://stackoverflow.com/questions/8130177/am-i-implementing-the-heapify-algorithm-correctly?rq=1

    '''

    def __init__(self, partitioned_list=[], heap_end_index=0):

        self._partitioned_list = partitioned_list

        # protect against instantiating out of bounds
        if ([] == partitioned_list):
            self._heap_end_index = -1
        else:
            assert(heap_end_index >= 0)
            assert(heap_end_index < len(self.partitioned_list))
            self._heap_end_index = heap_end_index

    def get_partitioned_list(self):
        return self._partitioned_list

    def set_partitioned_list(self, partitioned_list):
        self._partitioned_list = partitioned_list

    partitioned_list = property(get_partitioned_list, set_partitioned_list)

    def get_heap_end_index(self):
        '''
        returns heap_end_index
        -1 indicates heap partition is empty,
        and partitioned_list is either empty or completely sorted.

        '''
        return self._heap_end_index

    def set_heap_end_index(self, heap_end_index):
        # protect against assigning out of bounds
        assert(heap_end_index >= -1)
        assert(heap_end_index < len(self.partitioned_list))
        self._heap_end_index = heap_end_index

    heap_end_index = property(get_heap_end_index, set_heap_end_index)

    def number_of_non_leaf_nodes(self):
        '''
        returns number of nodes on levels above lowest level of max_heap tree.
        if heap_length equals one, returns 1.

        '''
        number_of_non_leaf_nodes = 0
        if (None == self.partitioned_list) or ([] == self.partitioned_list) or (-1 >= self.heap_end_index):
            number_of_non_leaf_nodes = 0
        else:
            # number of levels in the heap tree
            # log2 requires Python 3.3
            heap_length = self.heap_end_index + 1
            number_of_levels = int(math.log2(heap_length)) + 1
            number_of_non_leaf_nodes = ((2**(number_of_levels - 1)) - 1)

        return number_of_non_leaf_nodes

    def right_child_index(self, index):
        '''
        returns index of right child node
        if index doesn't have a right child within the max heap partition, returns None

        '''
        right_index = None
        if (index != None) and (self.heap_end_index >= (2*index + 2)):
            right_index = (2*index + 2)
        return right_index

    def left_child_index(self, index):
        '''
        returns index of left child node
        returns None if index doesn't have a left child
        within the max heap partition

        '''
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

    def node_has_a_bigger_child(self, index):
        '''
        returns True if node at index has a bigger child

        '''
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        if ((left_child_index and (self.partitioned_list[index] < self.partitioned_list[left_child_index])) or
            (right_child_index and (self.partitioned_list[index] < self.partitioned_list[right_child_index]))):
            return True
        else:
            return False

    def is_max_heap(self):
        '''
        returns True if heap partition is a max heap.

        '''
        is_max_heap = True
        # Iterate over non leaf nodes. Leaf nodes don't have children, don't need to check them.
        # Python range() is exclusive of final value
        for index in range(0, self.number_of_non_leaf_nodes()):
            if self.node_has_a_bigger_child(index):
                is_max_heap = False
                break

        return is_max_heap

    def index_of_biggest_child(self, index):
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        biggest_child_index = None
        if (not left_child_index and not right_child_index):
            biggest_child_index = None
        elif (left_child_index and not right_child_index):
            biggest_child_index = left_child_index
        elif (right_child_index and not left_child_index):
            biggest_child_index = right_child_index
        else:
            # index has two children
            if (self.partitioned_list[left_child_index] > self.partitioned_list[right_child_index]):
                biggest_child_index = left_child_index
            else:
                biggest_child_index = right_child_index

        return biggest_child_index

    def sift_up(self, start_index):
        '''
        sift_up starts searching at start_index and decrements index.
        If sift_up finds a node with a bigger child, it swaps the nodes.
        To reduce time complexity, it then changes index to parent.
        It does not explore other branches.

        partitioned_list almost represents a max heap, but root node is wrong.

        '''

        index = start_index
        while index != None and index >= 0:

            if self.node_has_a_bigger_child(index):
                biggest_child_index = self.index_of_biggest_child(index)
                self.swap_list_elements(index, biggest_child_index)
                # skip other tree branches, move index to parent
                index = self.parent_index(index)
            else:
                index -= 1

    def sift_down(self, start_index):
        '''
        sift_down starts at start_index
        If the node has a bigger child, it swaps the nodes and moves downward to swapped index.
        It loops until node doesn't have a bigger child.
        It does not explore other branches.

        '''
        index = start_index
        number_of_non_leaf_nodes = self.number_of_non_leaf_nodes()

        while index < number_of_non_leaf_nodes:
            if self.node_has_a_bigger_child(index):
                biggest_child_index = self.index_of_biggest_child(index)
                self.swap_list_elements(index, biggest_child_index)
                # skip other tree branches, move index to biggest_child_index
                index = biggest_child_index
            else:
                return

    def heapify(self, start_index):
        '''
        heapify starts searching at start_index.

        '''
        # decrement index
        # range() is exclusive of end index
        for index in range(start_index, -1, -1):
                self.sift_down(index)

    def heapify_up(self):
        '''
        heapify_up starts at root and increments to last leaf node
        This method is less efficient than heapifying down with heapify().
        Reference
        https://en.wikipedia.org/wiki/Heapsort

        '''
        # increment index
        # range() is exclusive of end index
        number_of_non_leaf_nodes = self.number_of_non_leaf_nodes()
        for index in range(0, number_of_non_leaf_nodes):
                print('index {} partitioned_list {}'.format(index, self.partitioned_list))
                self.sift_up(index)

    def heap_sort(self):
        '''
        heap_sort sorts in place, repeatedly pulling root node from max heap and adding it to sorted list.
        heap_sort assumes heap partition is empty or is a valid max heap.
        When the sort finishes, heap_end_index is -1, indicating the heap partition is empty.

        Could use Python sort() method instead. Wrote heap_sort as a learning exercise.

        '''

        while self.heap_end_index >= 0:
            # In current heap swap root with last leaf node.
            self.swap_list_elements(0, self.heap_end_index)
            # Decrement heap_end_index to move partition and add swapped element to sorted list.
            self.heap_end_index -= 1
            self.sift_down(0)
