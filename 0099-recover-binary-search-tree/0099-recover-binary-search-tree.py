# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right        
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        first = None
        second = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if not first:
                    first = nodes[i]
                second = nodes[i + 1]
                
        if first and second:
            first.val, second.val = second.val, first.val 



    
        
         
        