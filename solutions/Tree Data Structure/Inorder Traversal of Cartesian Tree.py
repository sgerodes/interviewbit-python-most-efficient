try:
    from data_structures.Tree import *
except:
    pass


# O(n) solution
class Solution:

    def buildTree(self, inorder_cartesian_traversal: list):
        length = len(inorder_cartesian_traversal)
        if length == 0:
            return None

        stack = []
        previous_larger = [None] * length
        for i, value in enumerate(inorder_cartesian_traversal):
            while len(stack) > 0 and stack[-1] < value:
                stack.pop()
            if len(stack) > 0:
                previous_larger[i] = stack[-1]
            stack.append(value)

        head = TreeNode(inorder_cartesian_traversal[0])
        last_node = head
        nodes = {head.val: head}

        for i in range(1, length):
            val = inorder_cartesian_traversal[i]
            current = TreeNode(val)

            if val < last_node.val:
                last_node.right = current
            else:
                if val < head.val:
                    prev_larger_val = previous_larger[i]
                    prev_larger_node = nodes[prev_larger_val]
                    current.left = prev_larger_node.right
                    prev_larger_node.right = current
                else:
                    current.left = head
                    head = current

            nodes[val] = current
            last_node = current
        return head
#
# The algorithm is pretty simple.
#
# create and store head (at begin it is the first element) time:O(1)
#
# create map “nodes” {number -> TreeNode} (add there the first node) time:O(1)
#
# store last node in “last” (at begin it is the first element) time:O(1)
#
# Iterate through array: time:O(n)
# Create a node for current value time:O(1)
# if current.value is < last.value, then current will be the right child of last time:O(1)
# else find the last node of already visited that is greater than current (we will name it “prev_larger” ) (how to do it in time:O(1) I will show later). time:O(1)
# The prev_larger right child will be the left child of current. prev_larger will be the parent of current, current will be the right child of prev_larger. Basically we “insert” current between prev_larger and his right child. time:O(1)
# if no prev_larger exist (means if current is the biggest) it becomes the head. The previous head becomes its left child. time:O(1)
#
# dont forget to update “nodes” and “last_node”
#
# Done. Tree created in time:O(n). Congrats.
# For the part of calculating the prev_larger:
#
# We can precalculate an array of prev_larger for every number. This could be done in O(n). An becausei it is done outside the loop, the complexities does not stack up. “inorder_cartesian_traversal” is our initial array.
#
# stack = []
# previous_larger = [None] * length
# for i, value in enumerate(inorder_cartesian_traversal):
#     while len(stack) > 0 and stack[-1] < value:
#         stack.pop()
#     if len(stack) > 0:
#         previous_larger[i] = stack[-1]
#     stack.append(value)
#
# More about the explanation here:
# https://stackoverflow.com/questions/62651215/given-array-of-unique-ints-when-iterating-through-is-it-possible-to-know-the/62660453#62660453
#
