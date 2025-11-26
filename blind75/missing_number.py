class Solution:
    def missingNumber(self, nums) -> int:
        totalSum = 0
        n = len(nums)
        for i in range(n):
            
            totalSum += nums[i]
        
        actualSum = (n * (n + 1))//2
        missingNum = actualSum - totalSum

        return missingNum


sol = Solution()


arr = [3,0,1]

print(f"Input: {arr} -> Output: {sol.missingNumber(arr)}")

nums = [9,6,4,2,3,5,7,0,1]
print(f"Input: {nums} -> Output: {sol.missingNumber(nums)}")
