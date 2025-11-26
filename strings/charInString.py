# Using Built-In Methods, Tn= O(n)
def insertChar(s, c, pos):

    return s[:pos] + c + s[pos:]

s = "international"
c = 'K'
pos = 5

print(insertChar(s,c,pos))

# Using Custom Method

def insertCharr(s, c, pos):
    res = ""
    for i in range(len(s)):
        if i == pos:
            res +=c
            # print(f'result at c added: {res}')
        res += s[i]
        # print(f'result at s[i] added: {res}')
    
    # if pos is > the length of the string
    if pos >= len(s):
        res += c
        # print(f'res is pos > len: {res}')

    return res

s = "international"
c = 'K'
pos = 30

print(insertCharr(s,c,pos))