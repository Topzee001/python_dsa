# array = [3,5,7,8,6]
# target = 9

# # using brute force
# n = len(array)
# found = False

# for i in range(n):
#     # print (i)
#     for j in range(i +1, n):
#         if array[i] == array[j]:
#             break
#         if array[i] + array[j] == target:
#             print(i,j)
#             found= True
#             break
#     if found:
#         break
# if not found:
#         print(-1, -1)

# # using better method
# map = {}
# for i, num in enumerate(array):
#      diff = target - num
#      if diff in map:
#           print(map[diff], i)
#           break
#      map[num] = i
# else:
#      print(-1, -1)



# using Hash map(better)
# class Solution:
#     def twoSum(self, nums, target):
#         map = {}
#         for i, num in enumerate(nums):
#             difference = target - num
#             if difference in map:
#                 return [map[difference], i]
                
#             map[num] = i
            
# solution = Solution()

# array = [1, 3, 5, -7, 6, -3]
# target = 0

# twoSum = solution.twoSum(array, target)

# print(twoSum)

# 2 sum ii using pointers (optimal)
class Solution:
    def twoSum(self, nums, target):
        i, j = 0, len(nums) -1

        while i < j:
            curSum = nums[i] + nums[j]
            if curSum > target:
                j -= 1
            elif curSum < target:
                i += 1
            else:
                return [i +1, j+1]

solution = Solution()

array = [1, 3, 5, -7, 6, -3]
array.sort()
print(array)
target = 9

twoSum = solution.twoSum(array, target)

print(twoSum)