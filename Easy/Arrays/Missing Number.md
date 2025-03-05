---
Link: https://leetcode.com/problems/missing-number/description/
tags:
  - Arrays
  - Easy
  - BitManipulation
  - Math
---
# Missing Number

## Problem Statement

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Example:**
```csharp
Input: nums = [3, 0, 1]
Output: 2
Explanation: n = 3, range is [0, 3] (0, 1, 2, 3), missing number is 2.
```

---

## Initial Thoughts

- Use **XOR** to find the missing number:
  - XOR all numbers in the array and track the maximum value.
  - XOR all numbers from `0` to the maximum value.
  - The result will be the missing number due to XOR canceling paired values.
- Alternative: Calculate the expected sum of numbers from `0` to `n` and subtract the actual sum of the array.

---

## Mistakes

- **Initial XOR Approach**:
  - Used two loops: one to XOR array elements and find `maxNum`, another to XOR from `0` to `maxNum`.
  - **Time Complexity**: O(n + m) where `m` is `maxNum`, unnecessarily iterating beyond `n`.
  - **Inefficiency**: Didn’t leverage the problem’s guarantee that numbers are in `[0, n]`.
- **Overcomplication**: Didn’t initially consider a single-pass solution using array length.
- **Not efficient for all problems**: if `nums` is [0, 1], the final output will 0 which is false

---

## Correct Solution

#### First Attempt (Two-Pass XOR)
```csharp
public int MissingNumber(int[] nums)
{
    int result = 0;
    int maxNum = 0;
    
    for (int i = 0; i < nums.Length; i++)
    {
        result ^= nums[i];
        if (maxNum < nums[i])
            maxNum = nums[i];
    }
    
    for (int i = 0; i <= maxNum; i++)
    {
        result ^= i;
    }
    
    return result;
}
```
- **Time**: O(n + m)
- **Space**: O(1)

#### Optimized Solution 1: XOR (Single Pass)
Traverse the array once, XORing each element with its index and the array length.

```csharp
public int MissingNumber(int[] nums)
{
    int result = nums.Length; // Start with n
    
    for (int i = 0; i < nums.Length; i++)
    {
        result ^= i ^ nums[i]; // XOR index and element
    }
    
    return result;
}
```
- **Steps**:
  1. Initialize `result` with `n` (array length).
  2. For each index `i`, XOR `i` and `nums[i]` into `result`.
  3. The missing number remains due to XOR cancellation.
- **Time**: O(n)
- **Space**: O(1)

#### Optimized Solution 2: Arithmetic (Single Pass)
Use the sum of the first `n` numbers minus the array sum.

```csharp
public int MissingNumber(int[] nums)
{
    int n = nums.Length;
    int expectedSum = (n * (n + 1)) / 2; // Sum of 0 to n
    int actualSum = 0;
    
    for (int i = 0; i < nums.Length; i++)
    {
        actualSum += nums[i];
    }
    
    return expectedSum - actualSum;
}
```
- **Steps**:
  1. Compute expected sum: `(n * (n + 1)) / 2`.
  2. Compute actual sum of `nums`.
  3. Return the difference.
- **Time**: O(n)
- **Space**: O(1)
- **Note**: Preferred for readability, but watch for integer overflow with large `n`.

#### Even More Concise (LINQ)
we can also leverage LINQ to make it shorter (though not necessarily faster due to overhead):

```csharp
public class Solution {
    public int MissingNumber(int[] nums) {
        int n = nums.Length;
        return (n * (n + 1)) / 2 - nums.Sum();
    }
}
```
- **Trade-off**: Slightly less performant due to LINQ’s enumeration but more readable.
##### Comparison

| Approach        | Time Complexity | Space Complexity | Pros                       | Cons                                          |
| --------------- | --------------- | ---------------- | -------------------------- | --------------------------------------------- |
| Original (XOR)  | O(n + m)        | O(1)             | Uses XOR, no overflow risk | Two loops, maxNum needed, not for all problem |
| XOR (Optimized) | O(n)            | O(1)             | Single pass, no overflow   | Slightly less intuitive                       |
| Arithmetic      | O(n)            | O(1)             | Single pass, intuitive     | Risk of integer overflow                      |
| LINQ            | O(n)            | O(1)             | Concise, readable          | LINQ overhead                                 |

---
## Edge Cases

1. **Single Element**:
   - Input: `[0]` → Output: `1` (n = 1, range [0, 1])
   - Input: `[1]` → Output: `0`
2. **Empty Array**:
   - Input: `[]` → Output: `0` (n = 0, range [0])
3. **All Consecutive**:
   - Input: `[0, 1, 2, 3]` → Output: `4` (missing last number)
4. **Missing First**:
   - Input: `[1, 2, 3]` → Output: `0`
5. **Unordered**:
   - Input: `[9, 6, 4, 2, 3, 5, 7, 0, 1]` → Output: `8`

---

## Lessons Learned

- **Learned XOR**: I learned how to work with XOR in this particular problem.
- **Problem Constraints**: Leverage the given range `[0, n]` to simplify the solution—array length `n` eliminates the need for finding `maxNum`.
- **Optimization Techniques**: Both XOR and arithmetic approaches can solve this in one pass; choosing between them depends on readability vs. overflow concerns.
- **Critical Thinking**: Start with the simplest approach (e.g., arithmetic) before exploring bitwise operations.

---
## Related Problems

- [LeetCode #136: Single Number](https://leetcode.com/problems/single-number/)
- [LeetCode #287: Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

---
## Progress Tracker

- **Status**: Solved
- **Confidence**: High
- **Revisit**: Yes (to solidify the one loop and arithematic approach)
