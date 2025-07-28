from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        res = 0

        while l <= h:
            m = l + ((h - l) // 2)
            if (m * m) > x:
                h = m - 1
            elif (m * m) < x:
                l = m + 1
                res = m
            else:
                return m
        
        return res
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(816))
            
