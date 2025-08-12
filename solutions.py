from typing import List

# class Solution:
#   def shortestToChar(self, s: str, c: str) -> List[int]:
#     prevIndx, currIndx = 0, 0
#     answer = [0] * len(s) 
#     j = 0
#     while currIndx < len(s):
#       if s[currIndx] != c:
#         currIndx += 1
#         continue
      
#       shortest = min((j - currIndx), (j - prevIndx))
#       answer[j] = abs(shortest)
#       if s[j] == c:
#         prevIndx = currIndx
#         currIndx += 1
      
#       j += 1

#     return answer

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [n] * n 
        
        last_c_pos = -n  
        for i in range(n):
            if s[i] == c:
                last_c_pos = i
            answer[i] = i - last_c_pos
        
        last_c_pos = 2 * n  
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_c_pos = i
            answer[i] = min(answer[i], last_c_pos - i)
        
        return answer

# Alternative one-pass solution
# class SolutionOnePass:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         # Find all positions of character c
#         c_positions = [i for i, char in enumerate(s) if char == c]
#         answer = []
        
#         for i in range(len(s)):
#             # Find minimum distance to any occurrence of c
#             min_dist = min(abs(i - pos) for pos in c_positions)
#             answer.append(min_dist)
        
#         return answer

# Test both solutions
print("Two-pass solution:")
solution1 = Solution()
result1 = solution1.shortestToChar("loveleetcode", "e")
print(f"Output: {result1}")

# print("\nOne-pass solution:")
# solution2 = SolutionOnePass()
# result2 = solution2.shortestToChar("loveleetcode", "e")
# print(f"Output: {result2}")

# print(f"\nExpected: [3,2,1,0,1,0,0,1,2,2,1,0]")

# # Verify they match
# print(f"Both solutions match: {result1 == result2}")
# print(f"Match expected: {result1 == [3,2,1,0,1,0,0,1,2,2,1,0]}")