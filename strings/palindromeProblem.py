class Solution:
    def palindrome(self, str):
        l = 0
        r = len(str) -1
        while l < r:
            if str[l] != str[r]:
                return 0
            l += 1
            r -= 1
        return 1

str = "abbwa"
solution = Solution()
isPalindrome = solution.palindrome(str)
print(isPalindrome)