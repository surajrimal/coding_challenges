https://leetcode.com/problems/matrix-diagonal-sum/submissions/
#author Suraj Rimal
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        dsum = 0
        l = len(mat)
        for i in range(l):
            for j in range(l):
                if(i == j):
                    dsum += mat[i][j]
                    if(i != l-i-1):
                        dsum+=mat[i][l-i-1]
        return dsum
                
                    
        
