# https://leetcode.com/problems/count-good-triplets/submissions/

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = []
        l = len(arr)
        count = 0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    res.append((arr[i], arr[j],arr[k]))
        for i in range(len(res)):
            if(abs(res[i][0]-res[i][1]) <= a):
                if(abs(res[i][1]-res[i][2]) <= b):
                    if(abs(res[i][0]-res[i][2]) <=c):
                        count+=1
        return count
            
        
