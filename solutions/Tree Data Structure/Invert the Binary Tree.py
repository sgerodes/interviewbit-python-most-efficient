# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, node):
        def recc_invert(node):
            if node:
                node.right, node.left = node.left, node.right
                recc_invert(node.left)
                recc_invert(node.right)
        recc_invert(node)
        return node