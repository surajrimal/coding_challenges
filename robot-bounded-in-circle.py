#link https://leetcode.com/problems/robot-bounded-in-circle/submissions/


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        count = 0
        point = [[0,1],[1,0],[0,-1],[-1,0]]
        ptr = 1
        unitx = 0
        unity = 0
        while(count<5):
            for i in instructions:
                if(i == "L"):
                    ptr = (ptr+1)%4
                elif(i=="R"):
                    ptr = (ptr-1)%4
                else:
                    unitx = unitx + point[ptr][0]
                    unity = unity + point[ptr][1]
            if(unitx ==0 and unity ==0):
                return True
            count+=1
        else:
            return False
       
