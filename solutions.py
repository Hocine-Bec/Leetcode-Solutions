from typing import List

# Two Pointer Approach
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         chIndex = -1
#         for i in range(len(word)):
#             if word[i] == ch:
#                 chIndex = i
#                 break
#         if chIndex == -1:
#             return word
        
#         l = 0 
#         chars = list(word)
#         while l <= chIndex:
#             chars[l], chars[chIndex] = chars[chIndex], chars[l]
#             l += 1
#             chIndex -= 1

#         return "".join(chars)

# Stack Approach:
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        for i in range(len(word)):
            stack.append(word[i])
            if word[i] == ch:
                prefix = []
                while stack:
                    prefix.append(stack.pop())  
                return "".join(prefix) + word[i+1:]
        
        return word



# Example usage:
sol = Solution()
word = "abcdefd"
print(f"Output: {sol.reversePrefix(word, "d")}")