# using built-in fxn method:
s = "ababca"
c = "a"

s = s.replace(c, "")

print(s)

# using list compression method

s = "".join([ch for ch in s if ch != c])

print(f"list compression: {s}")

# using translate method

trans_tab = str.maketrans("", "", c)
s = s.translate(trans_tab)
print(f"translate method: {s}")

# using manual method

def removeChar(s, c):
    s = list(s) # convert to string, since strings are immutable
    n = len(s)
    j = 0
    for i in range(n):
        if s[i] != c:
            s[j] = s[i]
            j += 1
    return "".join(s[:j])

s = "ababca"
c = "a"

charRem = removeChar(s,c)
print(f"manual method: {charRem}")

# append manual method
def removeCharApp(s,c):
    result = []
    for char in s:
        if char != c:
            result.append(char)
    return "".join(result)

# using filter:
def removeChar(s, c):
    return ''.join(filter(lambda x: x != c, s))