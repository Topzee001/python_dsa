x = [9, 12, 7, 4, 11]

x.sort()

print(x)

# push
x.append(8)

print(x)

# peek
topElement = x[-1]
print("peek", topElement)

# pop
poppedElement = x.pop()
print('popped:', poppedElement)

# Stack after Pop
print("Stack after Pop: ", x)

# isEmpty
isEmpty = not bool(x)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(x))



my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i
        print('minimum value is:', minVal)