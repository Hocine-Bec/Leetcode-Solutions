# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:       
        l, r = 0, len(nums)
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 13
    print(sol.search(nums, target))
            
