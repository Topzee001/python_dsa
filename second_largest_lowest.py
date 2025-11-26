class Solution:
    def secondLargestElement(self, nums):
        if not nums:
            raise ValueError("Array is Empty")
        if len(nums) < 2:
            return None
        largest = nums[0]
        slargest = -1
        
        
        for num in nums:
            if num > largest:
                slargest = largest
                largest = num
            elif num < largest and num > slargest:
                slargest = num
        return slargest

array = [1,5,6,8,9]

solution = Solution()

slargest = solution.secondLargestElement(array)

print(f"second largest: {slargest}")
    
class Solution:
    def secondSmallestElement(self, nums):
        if not nums:
            raise ValueError("Array is empty")
        smallest = nums[0]
        ssmallest = float('inf')
        # max(nums) #maximum number in the array
        for num in nums:
            if num < smallest:
                ssmallest = smallest
                smallest = num
            elif num != smallest and num < ssmallest:
                ssmallest = num
        return ssmallest if ssmallest != float("inf") else None

array = [1,5,6,8,9]
# array = [2]
array = [2,2,2,2,2]

solution = Solution()

ssmallest = solution.secondSmallestElement(array)

print(f"second smallest: {ssmallest}")