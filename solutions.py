# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

from typing import List

def guess(num : int) -> int:
    picked = 4
    if num == picked:
        return 0
    if num < picked: 
        return 1
    if num > picked:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        # if n == 1:
        #     return 1
        
        l, r = 0, n
        while l <= r:
            m = l + ((r - l) // 2)
            if guess(m) == 0:
                return m
            if guess(m) == 1:
                l = m + 1
            if guess(m) == -1:
                r = m - 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.guessNumber(25))
            
