class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        st = [] # Will store indices instead of values

        # Iterate through the array twice (2 * n)
        for i in range(2*n):
            # Use modulo to get the actual index in circular array
            curr_idx = i % n
            curr_val = nums[curr_idx]
            # While we have elements in stack and current element is greater than stack's top element
            while st and curr_val > nums[st[-1]]:
                # This current element is the next greater for the stack's top element
                idx = st.pop()
                res[idx] = curr_val
            
            # Only push to stack during first pass (i < n)
            if i < n:
                st.append(curr_idx)

        return res 
    
# Using reverse array order

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        st =[]
        # Iterate through circular array (2 * n)
        for i in range(2 * n-1, -1, -1):
            curr_idx = i % n
            curr_val = nums[curr_idx]

            # Remove elements from stack that are smaller than current
            while st and st[-1] <= curr_val:
                st.pop()

            # If stack is not empty, top is the next greater element
            if st:
                res[curr_idx] = st[-1]

            # Add current element to stack
            st.append(curr_val)

        return res

