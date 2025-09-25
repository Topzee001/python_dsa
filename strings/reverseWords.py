class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        reverse_words = words[::-1]
        return " ".join(reverse_words)
            
solution = Solution()

str = "this is a valid task and it's simple as well"

reverseWords = solution.reverseWords(str)

print(reverseWords)