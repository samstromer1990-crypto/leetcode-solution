# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):

        def findMax(node):
            if not node:
                return float('-inf')

            return max(
                node.val,
                findMax(node.left),
                findMax(node.right)
            )

        def findMin(node):
            if not node:
                return float('inf')

            return min(
                node.val,
                findMin(node.left),
                findMin(node.right)
            )

        def check(node):
            if not node:
                return True

            left_max = findMax(node.left)
            right_min = findMin(node.right)

            if left_max >= node.val:
                return False

            if right_min <= node.val:
                return False

            return check(node.left) and check(node.right)

        return check(root)