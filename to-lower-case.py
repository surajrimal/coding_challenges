#ref https://leetcode.com/problems/to-lower-case/submissions/

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for i in str:
            asc = ord(i)
            if(asc < 91 and asc >64):
                asc = asc + 32
            res += chr(asc)
        return res
        
