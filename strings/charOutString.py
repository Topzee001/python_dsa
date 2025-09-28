# By Using Built-In Methods
def removeCharInString(s, pos):
    if pos < 0 or pos >= len(s):
        return s
    
    return s[:pos] + s[pos + 1:]

s = 'books'
p = 4
removeChar = removeCharInString(s, p)

print(removeChar)

# By Writing Your Own Method
# Remove character at specified position using a loop

def remove_char_at_position(s, pos):
  
    # Check for valid position
    if pos < 0 or pos >= len(s): 
        return s

    # Convert string to list for mutable operations
    s_list = list(s)  
    
    # Shift characters to the left from the position
    for i in range(pos, len(s) - 1):
        s_list[i] = s_list[i + 1]

    # Remove the last character
    s_list.pop()  
    
    return ''.join(s_list) 
  
s = "abcde" 
pos = 1 
s = remove_char_at_position(s, pos)  
print(s)