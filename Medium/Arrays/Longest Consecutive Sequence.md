---
Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
tags:
  - Arrays
  - Medium
  - HashTable
  - Union-Find
---
## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive sequence of numbers (i.e., numbers that can be arranged in a sequence where each number increases by 1). You must write an algorithm that runs in O(n) time.

**Example:**
```csharp
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4], with a length of 4.
```

---

## Initial Thoughts

- **Array-Based Approach (Sorting)**:
  - Sort the array and iterate to find the longest sequence of consecutive numbers.
  - Simple but O(n log n) due to sorting, which violates the O(n) requirement.
- **HashSet Approach**:
  - Use a `HashSet` to store all numbers and check for consecutive numbers using `Contains(num + 1)`.
  - Intuition: Count how many numbers follow consecutively from any starting point.

---
## Mistakes

- **Sorting Attempt**:
  - Sorted the array and incremented a counter only when `nums[i] + 1 == nums[i + 1]`.
  - **Issues**:
    - **Time Complexity**: O(n log n) — failed the O(n) constraint.
    - **Incorrect Count**: Returned `count` (number of transitions) instead of sequence length (e.g., `[1, 2, 3]` should return 3, not 2).
    - Missed duplicates handling (e.g., `[1, 1, 2]`).
- **Incorrect HashSet Approach**:
  - Checked `num + 1` for every number and incremented a counter.
  - **Issues**:
    - Didn’t ensure a proper sequence starting from a minimal number.
    - Overcounted disconnected sequences (e.g., `[1, 2, 4, 5]` would count 2 twice).
    - Didn’t reset or track the longest sequence properly.

*Initial Code (Sorting):*
```csharp
public int LongestConsecutive(int[] nums)
{
    int count = 0;
    Array.Sort(nums);
    
    for (int i = 0; i < nums.Length; i++)
    {
        if (i + 1 == nums.Length)
            break;
        
        if (nums[i] + 1 == nums[i + 1])
            count++;
    }
    
    return count;
}
```
- **Issue**: For `[1, 2, 3]`, returns 2 (transitions) instead of 3 (length).

*Initial Code (HashSet):*
```csharp
public int LongestConsecutive(int[] nums)
{
    if (nums.Length == 0 || nums == null)
        return 0;
    
    int count = 1;
    var sorted = new HashSet<int>(nums);
    
    foreach (var num in sorted)
    {
        if (sorted.Contains(num + 1))
            count++;
    }
    
    return count;
}
```
- **Issue**: For `[100, 4, 200, 1, 3, 2]`, counts transitions (e.g., 3) instead of finding the longest sequence (4).

---
## Correct Solution

#### Corrected Sorting Solution
```csharp
public int LongestConsecutive(int[] nums)
{
    if (nums.Length == 0) return 0;
    
    Array.Sort(nums);
    int maxLength = 1;
    int currentLength = 1;
    
    for (int i = 1; i < nums.Length; i++)
    {
        if (nums[i] == nums[i - 1]) 
            continue; // Skip duplicates
        if (nums[i] == nums[i - 1] + 1)
        {
            currentLength++;
            maxLength = Math.Max(maxLength, currentLength);
        }
        else
        {
            currentLength = 1;
        }
    }
    
    return maxLength;
}
```
- **Time**: O(n log n) due to sorting
- **Space**: O(1) or O(n) depending on sorting implementation
- **Note**: Correctly handles duplicates and tracks sequence length, but still fails O(n) requirement.

#### Optimized HashSet Solution
Use a HashSet and only check sequences starting from numbers without a predecessor.

```csharp
public int LongestConsecutive(int[] nums)
{
    if (nums.Length == 0) 
        return 0;
    
    HashSet<int> set = new HashSet<int>(nums);
    int maxLength = 0;
    
    foreach (int num in set)
    {
        // Only start a sequence if num-1 doesn’t exist
        if (!set.Contains(num - 1))
        {
            int currentNum = num;
            int currentLength = 1;
            
            // Keep checking for consecutive numbers
            while (set.Contains(currentNum + 1))
            {
                currentNum++;
                currentLength++;
            }
            
            maxLength = Math.Max(maxLength, currentLength);
        }
    }
    
    return maxLength;
}
```
- **Steps**:
  1. Add all numbers to a HashSet (handles duplicates).
  2. For each `num`, check if it’s the start of a sequence (`num - 1` not in set).
  3. If it’s a start, count consecutive numbers (`num + 1`, `num + 2`, etc.) while they exist.
  4. Update `maxLength` with the longest sequence found.
- **Time**: O(n)
  - HashSet construction: O(n).
  - Each number is processed at most twice (once as a start, once in a sequence), amortized O(n).
- **Space**: O(n) for the HashSet.

##### Comparison

| Approach    | Time Complexity | Space Complexity | Pros                       | Cons                          |
|-------------|-----------------|------------------|----------------------------|-------------------------------|
| Sorting     | O(n log n)      | O(1) or O(n)     | Simple, intuitive          | Fails O(n) requirement        |
| HashSet     | O(n)            | O(n)             | Meets O(n), handles dups   | Slightly less intuitive       |

---

## Edge Cases

1. **Empty Array**:
   - Input: `[]` → Output: `0`
2. **Single Element**:
   - Input: `[5]` → Output: `1`
3. **All Duplicates**:
   - Input: `[1, 1, 1]` → Output: `1`
4. **No Sequence**:
   - Input: `[1, 3, 5, 7]` → Output: `1`
5. **Mixed with Gaps**:
   - Input: `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]` → Output: `9` (sequence `[0, 1, 2, 3, 4, 5, 6, 7, 8]`)

---

## Lessons Learned

- **Correct Sequence Counting**: Transition counts (e.g., `count++`) don’t equal sequence length; track the full length explicitly.
- **Optimization Insight**: Only checking sequence starts (when `num - 1` is absent) avoids redundant work.
- **Time Complexity**: Sorting is tempting but violates O(n)—HashSet is the key to linear time.
- **Problem Constraints**: Use the unsorted nature and consecutive property to guide the solution.

---

## Related Problems

- [LeetCode #3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [LeetCode #300: Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

---

## Progress Tracker

- **Status**: Not Solved
- **Confidence**: Medium (after corrections, still refining HashSet intuition)
- **Revisit**: Yes (to solidify HashSet-based sequence detection)
