class Solution:
    def isSorted(self, nums):
        #your code goes here
        n = len(nums)
        if n <= 1:
            return True
        for i in range(n -1):
            if nums[i] > nums[i +1]:
                return False
        return True
