# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniqSet = set(nums1)
        res = []
        i = 0
        for n in nums2:
            if n in uniqSet:
                res.append(n)
                uniqSet.remove(n)
            
        return res; 
    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = sol.intersection(nums1, nums2)
    for n in res:
        print(n)
            
