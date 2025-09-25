class Solution:
    def threeSum(self, nums, target):
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            l , r = i + 1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]]) 
                    l += 1  # Move left pointer to find next potential triple
                    # skip duplicates for left pointer
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    # print([a, nums[l], nums[r]])
        return result

solution = Solution()

array = [3, 1, 2, 5, -7, 5, -3]
# print(array)
target = 9

threeSum = solution.threeSum(array, target)

print(threeSum)