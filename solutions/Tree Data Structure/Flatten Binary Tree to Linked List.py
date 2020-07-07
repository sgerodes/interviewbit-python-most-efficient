# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# in place linear algorithm
# O(n) time, O(1) space
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, head):
        def is_leaf(node):
            return node is not None and node.left is None and node.right is None
        def flatten_recc(node):
            # flattens tree and returns the tail of a flatten list
            if is_leaf(node):
                return node
            if node.right is None:
                node.right = node.left
                node.left = None
            tail = flatten_recc(node.right)
            if node.left is not None:
                left_end = flatten_recc(node.left)
                left_end.right = node.right
                node.right = node.left
                node.left = None
            return tail


        flatten_recc(head)
        return head


# The algorithm
#
# - convert right subtree to a flatten list
# - if left is present convert left to a flatten tree. squash the left subtree between current node and the right subtree. (current.right= left, left.tail = right). You need to store the tail (the last leaf node) of the left subtree for that.
#
# Start from bottom, going up. A single leaf node is already flattened (obviously).


if __name__ == '__main__':
    s = Solution()
    from data_structures.Tree import *
    head = TreeNode(3)
    head.left = TreeNode(47)
    head.right = TreeNode(4)
    head = middle_Tree()
    head.print()
    print()
    flattened = s.flatten(head)
    flattened.print()