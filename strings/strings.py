s = "GeeksforGeeks"
print(s[-10])   # 3rd character
print(s[-5])    # 5th character from end
# slicing string
print(s[::-1]) # reverse string
print(s[3:8])
print(s[:4])
print(s[4:])
# string interation
s = 'Book'
for char in s:
    print(char)

# String Immutability
s = "geeksforGeeks"
s = "G" + s[1:]
print(s)
s = "GdG"
del s
# print(s) # will return nameError
s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)
# Formatting Strings
# Using format()
s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)