# # Example 1:
# # using optimal method to find the largest number in an array
# array = [2,3,5,6,9,7,8]

# maxValue = array[0]

# for i in array:
#     if i > maxValue:
#         maxValue = i

# print(f"max value: {maxValue}")


# # we can also use the brute force method, using bubble sort and then taking the array[n-1] as the largest value

# # Example 2
# # finding the min val

# minVal = array[0]

# for i in array:
#     if i < minVal:
#         minVal = i

# print(f"min value: {minVal}")

# finding max value using class
class Solution:
    def largestElement(self, nums):
        if not nums:
            return None
        max_value = nums[0]
        for num in nums:
            if num > max_value:
                max_value = num
        return max_value
solution = Solution()
array = [3, 3, 6, 1]

max_value = solution.largestElement(array)
print(max_value)

# # Example 3
# # finding the second largest number in an array


