# Palindrome Number

## Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

An integer is a palindrome when it reads the same backward as forward. For example, `121` is a palindrome while `123` is not.

---

## Examples

### Example 1:
**Input:**  
`x = 121`  
**Output:**  
`true`  

---

### Example 2:
**Input:**  
`x = -121`  
**Output:**  
`false`  
**Explanation:**  
From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

---

### Example 3:
**Input:**  
`x = 10`  
**Output:**  
`false`  
**Explanation:**  
Reads `01` from right to left. Therefore it is not a palindrome.

---

## Constraints:
- `-2^31 <= x <= 2^31 - 1`

---

## Performance:
- **Runtime:** 5 ms  
- **Memory Usage:** 17.85 MB  

---

## Complexity:
- **Time Complexity:**  
   - `O(n)` where `n` is the number of digits in `x`.  
   - Converting `x` to a string and reversing it both require `O(n)`.  

- **Space Complexity:**  
   - `O(n)` to store the string representation of `x` and its reverse.

---

## Approach 1: Convert Integer to String
We convert the integer `x` into a string and compare the original string with its reversed version.

### Steps:
1. Convert `x` to a string using `str(x)`.
2. Reverse the string using slicing (`[::-1]`).
3. Compare the original and reversed strings. If they are the same, return `true`. Otherwise, return `false`.

---

## Code:
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False
