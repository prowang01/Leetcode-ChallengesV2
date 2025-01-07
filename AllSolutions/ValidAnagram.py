# Approach : sort all the characters from the two lists then compare
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        return False
    
# Runtime : 18 ms / Memory : 18.11 MB


# Approach : Using Hashmap to count the frequency of characters and increment / decrement.

'''
# Count the frequency of characters in string s
# Decrement the frequency of characters in string t
# Check if any character has non-zero frequency

'''

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Count = defaultdict(int)
        for x in s:
            Count[x] += 1
        for x in t:
            Count[x] -= 1
        for val in Count.values():
            if val != 0:
                return False
        return True

# Runtime : 7 ms / Memory : 18.04 MB