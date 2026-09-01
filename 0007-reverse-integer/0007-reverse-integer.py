class Solution:
    def reverse(self, x: int) -> int:
        
        s =0
        if x>0:
            while x>0:
                a = x%10
                s = s*10 + a
                x = x//10
            
            
        else:
            x = x*-1
            while x>0:
                a = x%10
                s = s*10 + a
                x = x//10
            s = s*-1
        
        if s < -2**31 or s > 2**31 - 1:
            return 0

        return s
    
        