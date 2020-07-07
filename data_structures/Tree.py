import re
from operator import xor

class TreeNode:

    interviewbit_representation_regex = r" *(-?\d+ *)+ *"

    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return TreeNode.is_same_tree(self, other)
        return False

    def print(self):
        TreeNode.print_tree(self)

    @staticmethod
    def print_tree(head):
        indent = "\t"
        full_level = TreeNode.full_level_order_traversal(head)
        length = len(full_level)
        for i in range(length):
            print(indent * (length-i) + indent.join([str(node) if
                                                     node else "_" for node in full_level[i]]))

    @staticmethod
    def full_level_order_traversal(head):
        # level Order traversal with empty nodes represented as None
        def traverse_recc(node, traversal=[], level=0, curr_index=0):
            if node is None:
                return
            if len(traversal) < level+1:
                traversal.append([None]*2**level)
            traversal[level][curr_index] = node
            traverse_recc(node.left, traversal, level + 1, curr_index * 2)
            traverse_recc(node.right, traversal, level + 1, curr_index * 2 + 1)
            return traversal
        return traverse_recc(head)

    @staticmethod
    def depth(self, node):
        return 0 if node is None else 1 + max(self.depth(node.left), self.depth(node.right))

    @staticmethod
    def is_same_tree(node1, node2):
        if not isinstance(node1, TreeNode) or not isinstance(node2, TreeNode):
            raise ValueError("At least one of the Objects provided has an invalid type")
        def is_same_tree_rec(n1, n2):
            if xor(n1 is None, n2 is None):
                return False
            if n1 is None and n2 is None:
                return True
            if n1.val != n2.val:
                return False
            return is_same_tree_rec(n1.left, n2.left) and is_same_tree_rec(n1.right, n2.right)
        return node1 is node2 or is_same_tree_rec(node1, node2)

    # There are 3 lines in the input
    #
    # Line 1 ( Corresponds to arg 1 ) : First number represents the number of integers in input line. Then follows serialized representation of the tree. The serialization of a binary tree follows a level order description of left and right child of nodes, where -1 signifies a NULL child.
    # For example,
    #        1
    #       / \
    #      2    3
    #          /
    #         4
    #          \
    #            5
    # will have representation as {1 2 3 -1 -1 4 -1 -1 5 -1 -1}
    # The first integer on the line indicates the number of integers to follow in the serialized representation of the tree.
    #
    # Line 2 ( Corresponds to arg 2 ) : A single integer
    # For example, Integer: 2 will be written as "2"(without quotes).
    #
    # Line 3 ( Corresponds to arg 3 ) : A single integer
    # For example, Integer: 2 will be written as "2"(without quotes).
    @staticmethod
    def deserialize_from_interviewbit_representation(str_repr):
        if not re.match(TreeNode.interviewbit_representation_regex, str_repr):
            raise ValueError("representation has a not acceptable format. Acceptable example: '1 2 3 -1 -1 4 -1 -1 5 -1 -1'")
        def recc_deserialise(split, this_index, this_node):
            pass
        split = str_repr.split()
        if len(split) < 1:
            return None
        root_value = split[0]
        root = TreeNode(root_value)
        recc_deserialise(split, 0, root)
        return root


def create_tree_from_interviewbit_repr(str_repr):
    repr_arr = str_repr.strip().split(' ')
    

def small_Tree():
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    return a

def middle_Tree():
    a = TreeNode(1)

    a.left = TreeNode(2)
    a.left.left = TreeNode(3)
    a.left.right = TreeNode(4)

    a.right = TreeNode(30)
    a.right.left = TreeNode(40)
    a.right.right = TreeNode(50)

    a.right.right.right = TreeNode(60)
    return a

def middle_Tree_2():
    a = TreeNode(1)

    a.left = TreeNode(2)
    a.left.left = TreeNode(3)

    a.right = TreeNode(4)
    a.right.right = TreeNode(5)
    return a



def main():
    #print(Solution().prefix(["abcd", "ttr", "tcd", "abtu"]))
    s = middle_Tree()
    #s2 = 2
    s.print_tree(s)
    #print(s == s2)

if __name__ == '__main__':
    main()
