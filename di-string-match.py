# https://leetcode.com/problems/di-string-match/submissions/

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        output = []
        n = len(s)
        iv = 0 #for i
        dv = n #for d
        for i in range(n):
            if(s[i]== 'I'):
                output.append(iv)
                if(i==n-1):
                    output.append(iv+1)
                iv +=1
            else:
                output.append(dv)
                if(i==n-1):
                    output.append(dv-1)
                dv -=1
        
        return output
        
