# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

import math
from typing import List

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, res = 1, 0
        while i <= n:
            n = n - i
            res = i
            i += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.arrangeCoins(15))
            
