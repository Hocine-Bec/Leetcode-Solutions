from typing import List

# Original approach using two pointers
# class Solution:
#     def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
#         l, r = 0, 0
#         count = 0
#         while l < len(arr1) and r < len(arr2):
#             distance = abs(arr1[l] - arr2[r])

#             if distance <= d:
#                 r = 0
#                 l += 1
#                 continue
            
#             r += 1
#             if r == len(arr2):
#                 r = 0
#                 l += 1
#                 count += 1

#         return count
    

# Binary search approach using bisect
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for x in arr1:
            pos = bisect.bisect_left(arr2, x)
            is_valid = True

            if pos < len(arr2) and abs(arr2[pos] - x) <= d:
                is_valid = False
            if pos > 0 and abs(arr2[pos - 1] - x) <= d:
                is_valid = False

            if is_valid:
                count += 1

        return count


# Example usage:
sol = Solution()
arr1 = [-131,-623,992,849,-596,-524,-765,203,-734,994,201,36,-750,477,-455,-62,-598,600,-887,-261,970,-66,-315,898,974,258,481,-274,-550,895,909,301,-981,-972,0,-934,-664,-482,840,130,-919,-982,-529,566,817,-827,73,673,-646,-929,937,81,-590,-572,-93,-409,-503,4,36,-240,-335,-198,934,338,-850,-601,217,-629,-616,401,276,-392,956,910,190,-128,256,-30,-256,-953,-2,-958,904,-786,349,281,183,360,269,950]
arr2 = [732,-115,694,449,192,-297,-306,-849,324,-140,-601,436,53,647,12,949,724,704,245,154,352,127,924,26,751,-22,228,393,512,179,853,755,572,-79,236,-36,-662,704,-451,383,678,74,-383,153,566,650,-189,243,105,-470,-477,-365,-970,238,551,-907,601,-63,-63,826,-272,-525,40,-91,-572,432,-26,895,-313,425,281,-704,-214,766,-105,-889,314]
d = 14
print(f"Output: {sol.findTheDistanceValue(arr1, arr2, d)}")