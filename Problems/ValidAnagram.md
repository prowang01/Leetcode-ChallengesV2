# Valid Anagram

## Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

## Examples

### Example 1:
**Input:**
```
s = "anagram", t = "nagaram"
```
**Output:**
```
true
```

---

### Example 2:
**Input:**
```
s = "rat", t = "car"
```
**Output:**
```
false
```

---

## Constraints:
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Performance:
- **Runtime:** 7 ms
- **Memory Usage:** 18.04 MB

---

## Complexity:
- **Time Complexity:** `O(n)`
  - Iterate through both strings once.
- **Space Complexity:** `O(n)`
  - Store character frequencies in a hash map.

---

## Approach: Using Hash Map
We use a hash map to count the frequency of characters in `s` and decrement the count while iterating through `t`.

### Steps:
1. Count the frequency of each character in string `s`.
2. Decrement the frequency of each character in string `t`.
3. Verify if all frequencies in the hash map are zero.

---

## Code
```python
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Count = defaultdict(int)
        for x in s:
            Count[x] += 1
        for x in t:
            Count[x] -= 1
        
        for val in Count.values():
            if val != 0:
                return False

        return True
```
