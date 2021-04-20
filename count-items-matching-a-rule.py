#link https://leetcode.com/problems/count-items-matching-a-rule/submissions/

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        result = 0
        for item in items:
            if(ruleKey == "type"):
                if(ruleValue == item[0]):
                    result = result+1
            elif(ruleKey == "color"):
                if(ruleValue == item[1]):
                    result = result+1
            else:
                if(ruleValue == item[2]):
                    result = result+1
        return result
