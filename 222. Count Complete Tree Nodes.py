"""
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/description/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root) -> int:
        if isinstance(root, list):
            root = self.construct_tree(root)

        if not root:
            return 0

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)

        if left_depth == right_depth:
            return 2 ** left_depth + self.countNodes(root.right)
        else:
            return 2 ** right_depth + self.countNodes(root.left)

    def get_depth(self, root):
        if not root:
            return 0
        return 1 + self.get_depth(root.left)

    @staticmethod
    def construct_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i in range(len(values)):
            if nodes[i] is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(values):
                    nodes[i].left = nodes[left_index]
                if right_index < len(values):
                    nodes[i].right = nodes[right_index]
        return nodes[0]


# Example usage
solution = Solution()
print(solution.countNodes([1, 2, 3, 4]))



