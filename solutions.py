import math
from typing import List


# class Solution:
#     def isHappy(self, n: int) -> bool:
#         freq = { n: 0 }
#         index = 0
#         while True:
#             sum, sqrt, mod = 0, 0, 0
#             while n != 0: 
#                 mod = n % 10
#                 sqrt = mod**2
#                 sum += sqrt
#                 n = n // 10

#             if sum == 1:
#                 return True
#             if sum in freq:
#                 return False
            
#             n = sum
#             index += 1
#             freq[n] = index

#         return False

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0, len(arr), 2 * k):
            l = i
            m = i+k-1
            if m >= len(arr):
                m = len(arr) - 1
            while l < m:
                arr[l], arr[m] = arr[m], arr[l]
                l += 1
                m -= 1
        return ''.join(arr)



if __name__ == "__main__":
    sol = Solution()
    s = "abcdefg"
    k = 2
    print(sol.reverseStr(s, k))
    
            
