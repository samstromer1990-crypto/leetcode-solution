class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        direction = 1
        current_rows = 0
        for i in s:
            rows[current_rows] += i
            current_rows += direction  
        
    
            if current_rows == 0 or current_rows == numRows - 1:
                direction *= -1
        return"".join(rows)