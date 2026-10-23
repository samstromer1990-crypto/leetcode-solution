
from itertools import combinations

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        n = len(s)

        for cuts in combinations(range(1, n), 3):
            points = (0,) + cuts + (n,)
            
            parts = [
                s[points[i]:points[i + 1]]
                for i in range(4)
            ]

            if all(
                len(part) <= 3
                and (len(part) == 1 or part[0] != '0')
                and int(part) <= 255
                for part in parts
            ):
                result.append(".".join(parts))

        return result
