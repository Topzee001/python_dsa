class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # matrix = [[1,2,3], [2,3,4], [5,6,7]]
        rows = len(matrix)
        columns = len(matrix[0])

        if not rows or not columns:
            return []
        # matrix = [
        #      t      r
        #     l[1,2,3],
        #      [2,3,4],
        #      [5,6,7]
        #     b
        # ]
        result = []
        top, left = 0, 0
        bottom, right = rows , columns

        while top < bottom and left < right:
            # traverse from left to right(top row)
            for col in range(left, right):
                result.append(matrix[top][col])
            top += 1
            # traverse from top to bottom(right column)
            for row in range(top, bottom):
                result.append(matrix[row][right-1])
            right -= 1
            # traverse from right to left(bottom row)
            if top < bottom:
                for col in range(right-1, left-1, -1):
                    result.append(matrix[bottom-1][col])
                bottom -= 1
            # traverse from bottom to top
            if left < right:
                for row in range(bottom-1, top-1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result



        
