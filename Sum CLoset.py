class Solution:
    def threeSumClosest(self, num, target):
        minval = 100000
        num.sort()
        for i in range(len(num)):
            left = i+1
            right = len(num) -1
            while left<right:
                val = num[i]+num[left] + num[right]
                if abs(val-target)<minval:
                    minval = abs(val-target)
                    result = val
                if val == target:
                    return target
                if val<=target:
                    left += 1
                else:
                    right += 1
        return result