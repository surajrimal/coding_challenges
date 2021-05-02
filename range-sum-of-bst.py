# https://leetcode.com/problems/range-sum-of-bst/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if(root is None):
            return 0
        if(root.val >= low and root.val<=high):
            return root.val + self.rangeSumBST(root.left, low,high) + self.rangeSumBST(root.right, low,high)
        else:
            return self.rangeSumBST(root.left, low,high) + self.rangeSumBST(root.right, low,high)
            
        
