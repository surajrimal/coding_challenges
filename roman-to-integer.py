
#https://leetcode.com/problems/roman-to-integer/submissions/
class Solution(object):
    def romanToInt(self, s):
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        prev = 0
        for digit in s:
            if(prev < dict[digit]):
                result = result - 2*prev
            result += dict[digit]
            prev = dict[digit]
        return result
    
    
