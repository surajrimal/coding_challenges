#link https://leetcode.com/problems/third-maximum-number/submissions/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 3
        maxi = max(nums)
        nums = list(set(nums))
        while(1):
            maxv = max(nums)
            i = nums.index(maxv)
            count-=1
            if(count == 0):
                return maxv
            nums.pop(i)
            if(len(nums) == 0):
                return maxi
            
                
        
