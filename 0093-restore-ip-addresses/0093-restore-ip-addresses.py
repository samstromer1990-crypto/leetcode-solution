
from itertools import combinations

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        n = len(s)

        # Choose 3 positions to split the string into 4 parts
        for cuts in combinations(range(1, n), 3):
            points = (0,) + cuts + (n,)
            
            # Convert the string parts into a list
            parts = [
                s[points[i]:points[i + 1]]
                for i in range(4)
            ]

            # Each part must be a valid IP address number
            if all(
                len(part) <= 3
                and (len(part) == 1 or part[0] != '0')
                and int(part) <= 255
                for part in parts
            ):
                result.append(".".join(parts))

        return result
