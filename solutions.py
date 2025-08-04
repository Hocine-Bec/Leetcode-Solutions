import math
from typing import List

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if len(needle) > len(haystack):
#             return -1
        
#         l, firstIndex = 0, 0
#         while l < len(haystack):
#             r = 0
#             if haystack[l] != needle[r]:
#                 l += 1  
#             else:
#                 firstIndex = l
#                 while l < len(haystack) and r < len(needle):
#                     if haystack[l] != needle[r]:
#                         break
#                     l += 1
#                     r += 1

#                 if r == (len(needle)):
#                     return firstIndex
  
#                 l = firstIndex + 1
        
#         return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        l = 0
        while l <= len(haystack) - len(needle):
            if haystack[l] == needle[0]:
                i = l
                r = 0
                while r < len(needle) and haystack[i] == needle[r]:
                    i += 1
                    r += 1
                if r == len(needle):
                    return l
            l += 1
        
        return -1


if __name__ == "__main__":
    sol = Solution()
    haystack = "mississippi"
    needle = "issippi"
    print(sol.strStr(haystack, needle))
            
