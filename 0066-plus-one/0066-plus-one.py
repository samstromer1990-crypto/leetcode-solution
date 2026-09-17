class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = 0
        for i in digits:
            s = s * 10 + i
            
        s += 1
        
        output = []
        while s > 0:
            output.append(s % 10)
            s = s // 10
            
        return output[::-1]