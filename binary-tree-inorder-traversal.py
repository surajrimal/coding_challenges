
# link https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        output = []
        if (root.left):
            result = (self.inorderTraversal(root.left))
            for item in result:
                output.append(item)
        output.append(root.val)
        if( root.right):
            result =self.inorderTraversal(root.right)
            for item in result:
                output.append(item)
        return output
        
        
