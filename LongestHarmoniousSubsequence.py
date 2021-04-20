class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}  
		## or use Counter()  
        for i in nums: 
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        
        max_length = 0
        
		##linear scan to check the max_length
        for i in ans:
            if i+1 in ans:
                max_length = max(ans[i]+ans[i+1], max_length)
        
        return max_length
