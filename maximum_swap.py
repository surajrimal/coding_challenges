#question link https://leetcode.com/problems/maximum-swap/submissions/
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        arr = []
        sarr = []
        for s in num:
            arr.append(s)
        sarr = sorted(arr, reverse=True)
        for i in range(len(arr)):
            if(arr[i] != sarr[i]):
                z = arr[i]
                index = len(arr) - 1 - arr[::-1].index(sarr[i])
                arr[i] = sarr[i]
                arr[index] = z
                break
        listToStr = ''.join(map(str, arr))
        return listToStr
            
       
