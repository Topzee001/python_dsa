# # 1. implementing using for loop
# prev2 = 0
# prev1 = 1

# print(prev2)
# print(prev1)

# for fibo in range(18):
#     newFibo = prev1 + prev2
#     print(newFibo)
#     prev2=prev1
#     prev1 = newFibo

# # 2. implemementing using recursion

# print(0)
# print(1)
# count = 2

# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newFibo = prev1 + prev2
#         print(newFibo)
#         prev2=prev1
#         prev1=newFibo
#         count +=1
#         fibonacci(prev1, prev2)
#     else:
#         return
    
# fibonacci(1,0)

# 3. Finding The nth Fibonacci Number Using Recursion

def f(n):
    if n <= 1:
        return n
    else:
        return f(n-2) + f(n-1)
    
print (f(19))