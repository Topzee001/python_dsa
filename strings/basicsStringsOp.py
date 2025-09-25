# Check if two strings are same or not

# Approach - By Using (==) in C++/Python/C#, equals in Java and === in JavaScript
# Function to compare both strings directly
def areStringsSame(s1, s2):
    return s1 == s2

if __name__ == '__main__':
    s1 = "abcd"
    s2 = "abcd"

    # Call the areStringsSame function to compare strings, Tc = O(n), Sc = O(1)
    if areStringsSame(s1, s2):
        print("Yes")
    else:
        print("No")

# Approach - By Using String Comparison Functions
# Function to compare two strings using ==, Tc=O(n), Sc=0(1)

def areStringSame(s1, s2):
    return s1 == s2

s1 = "book"
s2 = "books"

if areStringSame(s1, s2):
    print("yes")
else:
    print('No')

# Approach - By Writing your Own Method, Tc = O(n), Sc= 0(1)

def are_strings_equal(s1, s2):
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

s1 = "tab"
s2 = 'tab'

if are_strings_equal(s1, s2):
    print('true')
else:
    print("false")
        