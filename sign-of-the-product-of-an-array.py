#link https://leetcode.com/problems/sign-of-the-product-of-an-array/submissions/

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        neg_count = len(list(filter(lambda x: (x < 0), nums)))
        if(neg_count%2 == 0):
            return 1
        else:
            return -1
        
        
