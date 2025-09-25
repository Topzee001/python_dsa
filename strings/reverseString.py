class Solution:
    def reverseString(self, str):
        revStr = []
        n = len(str) -1
        for i in range(n, -1, -1):
             revStr.append(str[i])
        
        return "".join(revStr)
    
solution = Solution()
str = "books"
reverse = solution.reverseString(str)

print(reverse)