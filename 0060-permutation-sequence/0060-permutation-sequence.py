import itertools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = 0
        if n == 0:
            return '0'
        for i in range(0,n+1):
            s = s*10 +i
        s = str(s)
        g = itertools.permutations(s)
        h =[''.join(p) for p in g]
        return h[k-1]



        