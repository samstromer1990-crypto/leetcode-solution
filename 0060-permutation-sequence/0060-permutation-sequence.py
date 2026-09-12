import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-indexed
        
        factorial = math.factorial(n - 1)
        result = []
        
        for i in range(n - 1, 0, -1):
            index = k // factorial
            result.append(numbers.pop(index))
            k %= factorial
            factorial //= i
            
        result.append(numbers[0])
        return ''.join(result)