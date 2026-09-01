class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        f = 0
        while x>0:
            s = x%10
            f = f*10 +s
            x = x//10
        if f == a:
        
            return True
        else:
            
            return False