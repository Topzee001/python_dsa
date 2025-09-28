class Solution:
    def printNumber(self):
        value= input('Enter an integer value: ')

        try:
            int_value = int(value)
            print(f"this is the inputed value: {int_value}")
        except ValueError:
            print(f"the inputed {value} is not an integer value")

solution = Solution()

solution.printNumber()
