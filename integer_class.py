# direct way without a class in python
integer = input('Enter an integer value:')

print(integer)


# with a class based on the task:
class Solution:
    def printNumber(self):
        value = int(input('Enter an integer value: '))
        print(value)

# create am instance of the class
solution = Solution()

# call the function
solution.printNumber()

# with exceptions
class Solution:
    def printNumber(self):
        value= input('Enter an integer value: ')

        try:
            int_value = int(value)
            print(int_value)
        except ValueError:
            print(f"the inputed {value} is not an integer value")

solution = Solution()

solution.printNumber()



