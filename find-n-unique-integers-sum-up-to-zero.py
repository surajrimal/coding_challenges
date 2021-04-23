# link https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/submissions/

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if(n%2!=0):
            res.append(0)
        for i in range(1,(n+2)/2):
            res.append(i)
            res.append(-i)
        return res
            
        
