# Program to Search a Character in a String
# finding the first occurence
def findChar(s, ch):
    n = len(s)
    for i in range(n):
        if s[i] == ch:
            return i
    return -1

string = "book"
ch = "k"

find =findChar(string, ch)

print(find)

# Approach - By Using in-built library functions - O(n) Time and O(1) Space

def find_char_index(s, ch):
    idx = s.find(ch)
    return idx

s = "trouble"
ch = "b"

search = find_char_index(s, ch)
print(search)