class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("Grade A")
        elif marks >=70:
            print("Grade B")
        elif marks >=50:
            print("Grade C")
        elif marks >= 35:
            print("Grade D")
        else:
            print("Fail")

solution = Solution()

grade = solution.studentGrade(14)

print(grade)