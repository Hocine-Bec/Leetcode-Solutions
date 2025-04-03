---
Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
tags:
  - Arrays
  - Easy
---
### **1. Problem Statement**

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.
After doing so, return the array.

**Example 1:**
```csharp
Input: [17, 18, 5, 4, 6, 1]
Output: [18, 6, 6, 6, 1, -1]
```

---
### **2. Initial Thoughts**

1. Use **two nested loops**:
    - Outer loop: Iterate through each element.
    - Inner loop: Find the maximum element to the right of the current element.
2. Replace the current element with the maximum found.
3. Handle the last element separately by setting it to `-1`.

---
### **3. Mistakes**

- **Time Complexity**: O(n²) due to nested loops.
- **Space Complexity**: O(n) due to the creation of a new array (`result`).
- **Inefficiency**: The nested loop approach is not optimal for large arrays.

---
### **4. Correct Solution**

### First Attempt
A single-loop approach comparing elements with a new array (result).

*Code*:
```csharp
public int[] ReplaceElements(int[] nums)
{
    int[] result = new int[nums.Length];
    int index = nums.Length - 1;
    result[index] = -1;
    
    for (int i = index; i > 0; i--)
    {
        if (nums[i] > result[i])
            result[i - 1] = nums[i];  // Store new max
        else
            result[i - 1] = result[i];  // Keep existing max
    }
    
    return result;
}```

- **Time**: O(n)
- **Space**: O(n)

**More Optimized Solution**:
Instead of using nested loops, we can traverse the array **from the end to the start**. This allows us to keep track of the maximum element seen so far and update the array in place.

**Steps:**
1. Initialize `maxSoFar` to `-1` (since the last element should be replaced with `-1`).
2. Traverse the array from the last element to the first.
3. For each element:
    - Store the current element in a temporary variable.
    - Replace the current element with `maxSoFar`.
    - Update `maxSoFar` to be the maximum of `maxSoFar` and the current element.
4. Return the modified array.

*code*:
```csharp
 public int[] ReplaceElements(int[] nums)
    {
        int n = nums.Length;
        int maxSoFar = -1; // Initialize the maximum to -1 for the last element
		
        // Traverse the array from the end to the start
        for (int i = n - 1; i >= 0; i--)
        {
            int currentElement = nums[i]; // Store the current element
            
            nums[i] = maxSoFar; // Replace the curr element with the maximum so far
            
            maxSoFar = Math.Max(maxSoFar, currentElement); // Update the maximum
        }
		
        return nums;
    }
```

This is the most optimized solution.
- **Time**: O(n)
- **Space**: O(1) -> in-place modification

---
### **5. Edge Cases**

1. **Single Element**: [400] → [-1]
2. **Empty Array**: [] → []
3. **All Equal**: [10, 10, 10] → [10, 10, -1]
4. **Descending**: [5, 4, 3, 2, 1] → [4, 3, 2, 1, -1]
5. **Ascending**: [1, 2, 3, 4, 5] → [5, 5, 5, 5, -1]

---
### **7. What I learned**

6. **Creative Problem-Solving**:
	I learned a creative way to solve a problem. I always thing straight forward but some problems can't be solve efficiently like that. 

7. **Self-Reliance**:
	I always ask AI for optimized solution after I solve a problem (which is good), but I need to think for myself first before doing that.

---
### **8. Related Problems**

1. [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
 1. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
	

---
### **9. Progress Tracker**

- **Status**: Solved it
- **Confidence Level**: Medium
- **Revisit**: Yes (to solidify the in-place approach)

---

>[!Related Concepts]
>- [[001_Arrays]]