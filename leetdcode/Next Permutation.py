class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i <=len(nums):
            if nums[-i] > a[-(i+1)]:
                a[-i],a[-(i+1)] = a[-(i+1)], a[-i]
                break
            else:
                i+=1
        return nums