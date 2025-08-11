

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        l, r = 0, 0  
        curr_count, prev_count = 1, 0 
        res = 0
        while l < len(s) and r < len(s):
            if s[l] == s[r]:
                curr_count += 1
                r += 1
            else:
                res += min(groups[l], groups[r])
                count = 1 
                l = r
                r += 1  
        groups.append(count)
        l, r, res = 0, 1, 0
        while r < len(groups):
            
            l += 1
            r += 1

        return res

# Test with your example
solution = Solution()
result = solution.countBinarySubstrings("10101")
print(f"Final result: {result}")  # Should be 6