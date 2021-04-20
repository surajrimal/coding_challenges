#link https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        i = nums.index(m)
        nums.pop(i)
        n = max(nums)
        return (m-1)*(n-1)
