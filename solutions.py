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
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            current, sum = n, 0
        
            while current > 0:
                digit = current % 10
                sum += digit ** 2
                current //= 10

            if sum in seen:
                return False
            
            seen.add(sum)
            n = sum

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(20))
            
