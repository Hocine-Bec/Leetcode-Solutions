from typing import List

# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         l, r = 0, len(nums) - 1     
#         while l < r:
#             if nums[l] % 2 == 0:
#                 l += 1
#                 continue
#             elif nums[r] % 2 != 0:
#                 r -= 1
#                 continue
            
#             temp = nums[l]
#             nums[l] = nums[r]
#             nums[r] = temp  
            
#             l += 1
#             r -= 1

#         return nums
    

# Alternative solution using list Bitwise AND operation
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1     
        while l < r:
            if (nums[l] & 0x1) == 0:
                l += 1
                continue
            elif (nums[r] & 0x1) != 0:
                r -= 1
                continue
            
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums
    
# Test both solutions
sol = Solution()
nums = [2, 4, 6, 3, 5, 8]
print(f"Output: {sol.sortArrayByParity(nums)}")