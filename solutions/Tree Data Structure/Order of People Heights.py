from data_structures.Tree import *

class SegmentTreeNode(TreeNode):
    def __init__(self, val=0, interval=None):
        # intervals are inclusive
        # stores only the count, not the value itself
        super().__init__(val)
        self.interval = interval
        self.left: SegmentTreeNode = None
        self.right: SegmentTreeNode = None

    def add_value(self, val):
        if not self.is_leaf():
            if self.right.get_interval_begin() > val:
                self.left.add_value(val)
            else:
                self.right.add_value(val)
        self.val += 1

    def get_count_until_index(self, i):
        if self.get_interval_begin() > i:
            return 0
        if self.get_interval_end() <= i:
            return self.val
        return self.left.get_count_until_index(i) + self.right.get_count_until_index(i)

    def is_leaf(self):
        return self.interval[0] == self.interval[1]

    def get_interval_begin(self):
        return self.interval[0]

    def get_interval_end(self):
        return self.interval[1]


    def __str__(self):
        if self.is_leaf():
            return "{}:{}".format([self.get_interval_begin()], self.val)
        else:
            return "{}:{}".format(self.interval, self.val)

class Solution:
    # @param heights : list of integers
    # @param infronts : list of integers
    # @return a list of integers

    def order(self, heights: list, infronts: list):
        length = len(heights)

        def create_segment_tree(begin=0, end=None):
            if end-begin == 0:
                return SegmentTreeNode(interval=[begin, end])
            node = SegmentTreeNode(val=0, interval=[begin, end])
            half = (end - begin) // 2
            node.left = create_segment_tree(begin, begin+half)
            node.right = create_segment_tree(begin+half+1, end)
            return node
        segnmentTree = create_segment_tree(end=length-1)


        infronts_mapping = {heights[i]: infronts[i] for i in range(length)}
        queue = [None] * length
        heights.sort(reverse=True)
        for i in range(length):
            segnmentTree.print()
            h = heights.pop()
            index = infronts_mapping[h]
            count_before = segnmentTree.get_count_until_index(index-1)  # check indexing if -1 will underflow
            index += count_before
            queue[index] = h
            segnmentTree.add_value(index)

        segnmentTree.print()
        return queue


if __name__ == '__main__':
    s = Solution()
    s.order([5, 3, 2, 6, 1, 4], [0, 1, 2, 0, 3, 2])