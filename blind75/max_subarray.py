class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = 0
        max_sum=nums[0]

        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(cur_max, max_sum)

        return max_sum


