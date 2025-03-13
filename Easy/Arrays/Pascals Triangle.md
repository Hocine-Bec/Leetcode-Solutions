---
Link: https://leetcode.com/problems/pascals-triangle/description/
tags:
  - Easy
  - Arrays
  - DynamicProgramming
---
## Problem Statement

Given an integer `numRows`, generate the first `numRows` of Pascal's Triangle. In Pascal's Triangle, each number is the sum of the two numbers directly above it.

**Example:**
```csharp
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Explanation: 
    Row 0: [1]
    Row 1: [1,1]
    Row 2: [1,2,1]
    Row 3: [1,3,3,1]
    Row 4: [1,4,6,4,1]
```

---
## Initial Thoughts

- **Row-by-Row Building**:
  - Start with `[1]` and generate each subsequent row.
  - Each element is the sum of two elements from the previous row.
- **Pattern Recognition**:
  - First and last elements of each row are always 1.
  - Middle elements follow the binomial coefficient pattern.

---
## Mistakes

- *Initial Attempt*:
```csharp
public IList<IList<int>> Generate(int numRows)
{
    var mainList = new List<IList<int>>(numRows);
    var subList = new List<int>();

    if (numRows == 1) 
    {
        subList.Add(1);
        mainList.Add(subList);
        return mainList;   
    }
    
    for (int i = 0; i < numRows; i++)
    {
        subList = new List<int>();
        for (int j = 0; j < i + 1; j++)
        {
            if (j == 0 || j == i)
                subList.Add(1);
            else
                subList.Add(subList[j - 1] + subList[j]); 
        }
        mainList.Add(subList);
    }

    return mainList;
}
```

- **Issues**:
  1. **Reference Error in `subList`**:
     - Used the same `subList` instance to compute middle elements (`subList[j - 1] + subList[j]`), but these indices refer to the *current* row being built, not the previous row.
     - Result: Attempts to sum elements within the same row before it’s fully populated, leading to incorrect values or exceptions.
  2. **Special Case for `numRows == 1`**:
     - Handled `numRows == 1` separately, but this logic skips `numRows == 0` and overcomplicates the flow.
  3. **Incorrect Values**:
     - Middle elements were computed as sums of wrong data, producing wrong result.

---
## Correct Solution

```csharp
public IList<IList<int>> Generate(int numRows)
{
    var mainList = new List<IList<int>>();
    
    if (numRows == 0)
        return mainList;
        
    for (int i = 0; i < numRows; i++)
    {
        var subList = new List<int>();
        for (int j = 0; j < i + 1; j++)
        {
            if (j == 0 || j == i)
                subList.Add(1);
            else
                subList.Add(mainList[i-1][j-1] + mainList[i-1][j]);
        }
        mainList.Add(subList);
    }
    
    return mainList;
}
```

- **Steps**:
    1. Return an empty list if `numRows == 0`.
    2. For each row `i` (0 to `numRows - 1`):
        - Create a new `subList` with `i + 1` elements.
        - Set first `(j == 0)` and last `(j == i)` elements to 1.
        - Compute middle elements as the sum of two elements from the previous row (`mainList[i-1]`).
    3. Add each row to `mainList`.
- **Resolution**: After a hint about referencing, corrected the summation to use `mainList[i-1]` instead of `subList`, fixing the logic.
- **Time**: O(n²), where n is `numRows` (total elements ≈ n(n+1)/2).
- **Space**: O(n²) to store the triangle.
---
## Edge Cases

1. **Zero Rows**:
   - Input: `0` → Output: `[]`
2. **Single Row**:
   - Input: `1` → Output: `[[1]]`
3. **Two Rows**:
   - Input: `2` → Output: `[[1],[1,1]]`
4. **Large Input**:
   - Input: `5` → Output: `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`

---
## Lessons Learned

- **Correct Referencing**: Summing elements from the current row being built (`subList`) is invalid—always use the previous row’s data (`mainList[i-1]`).
- **Initialization Timing**: Don’t rely on partially built data; ensure dependencies (like previous rows) are complete before use.
- **Loop Bounds**: For row `i`, use `j <= i (or j < i + 1)` to get the correct number of elements `(i + 1)`.
- **Simplify Logic**: Avoid unnecessary special cases (e.g., `numRows == 1`) when a general loop can handle all cases with proper edge checks.
- **Debugging Tip**: Test small inputs (e.g., `numRows = 2`) to catch reference errors early.

---

## Related Problems

- [LeetCode #119: Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)
- [LeetCode #120: Triangle](https://leetcode.com/problems/triangle/)

---

## Progress Tracker

- **Status**: Solved (with reference hint)
- **Confidence**: High
- **Revisit**: Yes (to solidify dynamic row generation and indexing)


