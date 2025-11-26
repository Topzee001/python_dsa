class Solution:
    def palindrome(self, str):
        l = 0
        r = len(str) -1
        while l < r:
            if str[l] != str[r]:
                return False
            l += 1
            r -= 1
        return True

str = "abba"
solution = Solution()
isPalindrome = solution.palindrome(str)
print(isPalindrome)


#longest palindromic string
class Solution:
    def longestPalindrome(self, s):
        res = ""
        resLength = 0

        for i in range(len(s)):
            # odd length
            l, r = i , i # starting from the center


            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    res = s[l:r+1]
                    resLength = r - 1 + 1
                
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    res = s[l: r+1]
                    resLength = r - l + 1

                l -= 1
                r += 1

        return res

s = "cbbd"

solution = Solution()
isLongPalindrome = solution.longestPalindrome(s)
print(isLongPalindrome)
