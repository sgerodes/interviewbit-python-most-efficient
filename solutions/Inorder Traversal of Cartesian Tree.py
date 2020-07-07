class Solution:

    def buildTree(self, inorder_cartesian_traversal: list):
        # cartesian tree and inorder traversal
        # no duplicates
        return self.buildTree_linear(inorder_cartesian_traversal)

    def buildTree_linear(self, inorder_cartesian_traversal: list):
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
