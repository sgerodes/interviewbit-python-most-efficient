# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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