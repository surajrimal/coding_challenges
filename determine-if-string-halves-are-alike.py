# link https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        l = len(s)
        first_half = 0
        second_half = 0
        for i in range(0,l):
            if(i<l/2):
                if(s[i] in vowel):
                    first_half +=1
            else:
                if(s[i] in vowel):
                    second_half +=1
        if(first_half == second_half):
            return True
        else:
            return False
                
            
        
