class Solution:
    def reverseString(self, str):
        revStr = []
        n = len(str) -1
        for i in range(n, -1, -1):
             revStr.append(str[i])
        
        print(f"test string {revStr}")
        
        return "".join(revStr)
    
solution = Solution()
str = "books"
reverse = solution.reverseString(str)

print(reverse)


#class Solution:
 #   def reverseString(self, s):
  #      return s.reverse()

class Solution:
    def reverseString(self, s):
        new_string = []
        for ch in range(len(s) -1, -1, -1):
            new_string.append(s[ch])

        print(f"newString: {new_string}")
        return new_string
    
solution = Solution()
str = ["h","e","l","l","o"]
reverse = solution.reverseString(str)

print(reverse)

# new

class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            # Swap characters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
solution = Solution()
str = ["h","e","l","l","o"]
reverse = solution.reverseString(str)

print(reverse)