# native approach, Tn = O(n^2)
def nextGreaterELement(arr):
    n = len(arr)
    # res default value is -1
    res = [-1] * n

    # iterate through each element in the array
    for i in range(n):
        # check for the NGE in d rest of d array
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res
    

if __name__ == "__main__":
    arr = [6, 8, 0, 1, 3]

    res = nextGreaterELement(arr)
    print(" ".join(map(str, res)))

# stack approach
def nextGreaterElement(arr):
    n = len(arr)
    # the result array contains -1 all through, will be replaced witht the proper value
    res = [-1] * n
    stk = []

    # Traverse the array from right to left
    for i in range(n-1, -1, -1):
        # pop elements from the stack that are less than or equal to the current value
        while stk and arr[stk[-1]] <= arr[-1]:
            stk.pop()
        
        # if stack is not empty, the element at the
        # top of the stack is the next greater element
        if stk:
            res[i] = arr[stk[-1]]

        # push the current index onto the stack
        stk.append(i)

    return res

if __name__ == "__main__":
  
    arr = [6, 8, 0, 1, 3]
    res = nextGreaterElement(arr)
    print(" ".join(map(str, res)))

# Next Greater Element 1 problem
# nums 1 is a subset of nums2
# find NGE of nums1
# using brute force, hashmap method
n1 = [4,1,2]
n2=[1,3,4,2]
res= []

# convert n1 to hashman
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # O(n * m)
        map1idx = {n:i for i, n in enumerate(nums1)}
        n1 = len(nums1)
        n2 = len(nums2)
        res = [-1] * n1

        for i in range(len(nums2)):
            if nums2[i] not in map1idx:
                continue
            for j in range(i +1, n2):
                if nums2[j] > nums2[i]:
                    idx = map1idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

# using stack
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # O(n)
        map1idx = {n:i for i, n in enumerate(nums1)}
        n1 = len(nums1)
        n2 = len(nums2)
        res = [-1] * n1
        stack = []

        for i in range(n2):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = map1idx[val]
                res[idx] = cur
            if cur in map1idx:
                stack.append(cur)
        return res