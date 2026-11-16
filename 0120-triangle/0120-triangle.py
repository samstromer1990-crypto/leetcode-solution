class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        def min_num(i, j):
            a = triangle[i+1][j]
            b = triangle[i+1][j+1]
            if a < b:
                return a
            else:
                return b
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min_num(i, j)
                
        return triangle[0][0]