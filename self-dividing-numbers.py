#https://leetcode.com/problems/self-dividing-numbers/
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output = []
        for i in range(left,right+1):
            div = str(i)
            temp = 0
            for j in div:
                j = int(j)
                if(j == 0):
                    temp = 1
                    break
                if(i%j != 0):
                    temp = 1
                    break
            if(temp !=1):
                output.append(i)
        return output
        
