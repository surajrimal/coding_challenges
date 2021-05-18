#link https://leetcode.com/problems/perfect-number/submissions/

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 3:
            return False
        i = 2
        divsum = 0
    
        while i*i <= num:
            if num%i == 0:
                divsum += i + num//i        
            i += 1

        divsum += 1
    
        return divsum == num
