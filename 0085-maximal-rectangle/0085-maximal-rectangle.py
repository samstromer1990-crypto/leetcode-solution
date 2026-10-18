class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        def largest_rectangle(heights):
            stack = []
            max_area = 0

            for i in range(len(heights) + 1):
                while stack and (
                    i == len(heights) or heights[stack[-1]] > heights[i]
                ):
                    height = heights[stack.pop()]

                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1

                    max_area = max(max_area, height * width)

                if i < len(heights):
                    stack.append(i)

            return max_area

        cols = len(matrix[0])
        heights = [0] * cols
        area = 0

        for row in matrix:
            for col in range(cols):
                if row[col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            area = max(area, largest_rectangle(heights))

        return area