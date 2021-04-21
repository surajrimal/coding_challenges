#link https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        stack = []
        stack.append(s[0])
        prev = s[0]
        count = 0
        for i in range(1,len(s)):
            if(s[i]== prev or len(stack)==0):
                stack.append(s[i])
                prev = s[i]
                
            else:
                stack.pop()
                if(len(stack)== 0 ):
                    count = count +1
               
                
        return count
            
        
