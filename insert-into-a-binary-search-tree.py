#link https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        a = TreeNode(val)
        if(root is None):
            return a
        
        if(val<root.val):
            if(root.left is None):
                root.left = a
            else:
                self.insertIntoBST(root.left, val)
        else:
            if(root.right is None):
                root.right = a
            else:
                self.insertIntoBST(root.right, val)
        return root
            
       
         
