# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right        
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        first = second = prev = None
        
        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return
            
            inorder(node.left)
            
            # If this node is smaller than the previous one, we found a violation
            if prev and prev.val > node.val:
                if not first:
                    first = prev  # The first time it happens, 'prev' is the wrong node
                second = node     # The second time (or final update), 'node' is the wrong node
            prev = node
            
            inorder(node.right)
            
        inorder(root)
        
        # Swap the values of the two misplaced nodes
        if first and second:
            first.val, second.val = second.val, first.val