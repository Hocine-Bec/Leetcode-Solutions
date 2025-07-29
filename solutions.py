# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
        return version >= 7

class Solution:    
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = l + ((r - l)//2)
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstBadVersion(51))
            
