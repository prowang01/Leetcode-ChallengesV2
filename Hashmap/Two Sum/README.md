# Two Sum

## Description
Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

---

## Examples

### Example 1:
**Input:**  
`nums = [2,7,11,15], target = 9`  
**Output:**  
`[0,1]`

**Explanation:**  
Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

### Example 2:
**Input:**  
`nums = [3,2,4], target = 6`  
**Output:**  
`[1,2]`

---

### Example 3:
**Input:**  
`nums = [3,3], target = 6`  
**Output:**  
`[0,1]`

---

## Constraints:
- `2 <= nums.length <= 10,000`
- `-1,000,000,000 <= nums[i] <= 1,000,000,000`
- `-1,000,000,000 <= target <= 1,000,000,000`
- **Only one valid answer exists.**

---

- **Runtime:** 3 ms
- **Memory Usage:** 18.84 MB

## Performance :

- **Runtime:** 3 ms

- **Memory Usage:** 18.84 MB

- **Time Complexity:**  
   - `O(n)`: Single iteration over the array.
- **Space Complexity:**  
   - `O(n)`: To store elements in the hash table.

---

## Approach: Hash Table
We use a hash table to efficiently store and look up elements of the array.

### Steps:
1. Iterate through the array.
2. For each element:
   - Calculate the complement: `current = target - nums[i]`.
   - Check if the complement exists in the hash table.
     - If yes, return the indices of the current element and the complement.
     - If no, add the current element and its index to the hash table.
3. This approach ensures `O(n)` time complexity since we process each element only once.

---

## Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [i, hash_table[complement]]
            hash_table[nums[i]] = i
        return []  # If no solution is found
```



