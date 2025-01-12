# Three Sum

## Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
- \( i \) is not equal to \( j \), \( i \) is not equal to \( k \), and \( j \) is not equal to \( k \).
- The sum of \( nums[i] \), \( nums[j] \), and \( nums[k] \) is equal to zero.

The solution set must not contain duplicate triplets.

---

## Examples

### Example 1:
**Input:**  
`nums = [-1,0,1,2,-1,-4]`  
**Output:**  
`[[-1,-1,2],[-1,0,1]]`  

**Explanation:**  
The distinct triplets are:
1. The sum of `nums[0]`, `nums[1]`, and `nums[2]` is \(-1 + 0 + 1 = 0\).
2. The sum of `nums[1]`, `nums[2]`, and `nums[4]` is \(-1 + 0 + 1 = 0\).

Notice that the order of the output and the order of the triplets does not matter.

---

### Example 2:
**Input:**  
`nums = [0,1,1]`  
**Output:**  
`[]`  

**Explanation:**  
The only possible triplet does not sum up to zero.

---

### Example 3:
**Input:**  
`nums = [0,0,0]`  
**Output:**  
`[[0,0,0]]`  

**Explanation:**  
The only possible triplet sums up to zero.

---

## Constraints:
- The length of the array `nums` is between 3 and 3000.
- Each element in `nums` is between \(-100,000\) and \(100,000\).

---

## Performance:
- **Runtime:** 596 ms  
- **Memory Usage:** 20.68 MB  

---

## Complexity:
- **Time Complexity:**  
   - \( O(n^2) \): Sorting the array takes \( O(n log n) \), and iterating through each element with the two-pointers technique takes \( O(n) \) per element.
   - Overall, this results in \( O(n^2) \).

- **Space Complexity:**  
   - \( O(n) \): Sorting the array takes extra space.

---

## Approach: Two Pointers Technique

### Steps:
1. **Sort the array:**  
   - Sorting ensures that duplicates are grouped together, making it easier to skip them.

2. **Iterate through the array:**  
   - For each element `nums[i]`, fix it as the first element of the triplet.
   - Use two pointers, `left` (starting after `i`) and `right` (starting at the end of the array), to find the other two elements such that their sum equals the negative of `nums[i]`.

3. **Skip duplicates:**  
   - Skip duplicate values for `nums[i]`, `left`, and `right` to avoid repeated triplets.

4. **Adjust pointers:**  
   - If the sum of the triplet is less than zero, move `left` forward to increase the sum.
   - If the sum is greater than zero, move `right` backward to decrease the sum.

---

## Code:
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:       
                continue  
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
