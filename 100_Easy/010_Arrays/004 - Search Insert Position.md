---
Link: https://leetcode.com/problems/search-insert-position/description/
tags:
  - Easy
  - Arrays
  - BinarySearch
---
## First Attempt:
*wrong answer*

```Csharp
public class Solution {
    public int SearchInsert(int[] nums, int target)
    {
        if (nums.Length <= 0)
            return 0;
        if (nums[^1] <= target)
            return nums.Length;
        
        var index = 0;
        for (var i = 0; i < nums.Length; i++)
        {
            if (target == nums[i])
                return i;
            
            index = i;
            if (target - nums[i] < 0)
                break;
        }
        return index;
    }
}
```

## Second Attempt:
*correct answer with O(n)*
```csharp
public class Solution {
    public int SearchInsert(int[] nums, int target)
    {
        if (nums.Length <= 0) return 0;

        for (var i = 0; i < nums.Length; i++)
        {
            if (nums[i] >= target)
                return i;
        }
        return nums.Length;
    }
}
```

## 3rd Attempt:
*correct answer with O(log n)*
I solved with `C#` first then tried to write it in python
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if(nums[mid] == target):
                return mid
            if(target > nums[mid]):
                start = mid + 1
            else:
                end = mid
        return start
```