#link https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]<0):
                    count +=1
        return count
        
