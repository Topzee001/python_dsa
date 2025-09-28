s1 = 'Hello, '
s2 = 'World!'

new_str = s1 + s2

print(new_str)



# manual fxn
def concatenate(s1, s2):
    new_string = ''

    for c in s1:
        new_string += c
    
    for c in s2:
        new_string += c
    
    return new_string



s1 = 'Hello, '
s2 = 'World!'

# Call the function to concatenate the strings
res = concatenate(s1, s2)

print(res)