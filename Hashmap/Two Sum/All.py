# Brute Force Method
'''
Generate all the possible pairs and check if any of them add up to the target value. 
To generate all pairs, we simply run two nested loops.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [] # store the indexes
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    # b = [i, j]
                    # result.extend(b) complicating the code for nothing
        return result # no solution found

'''
O(n^2) time and O(1) space
Runtime : 1973 ms
Memory : 18.3 MB
'''



# Approach : hash table
'''
Use a hash table. Iterate through the array once, and for each element, check if the target minus the current element exists in the hash table. 
If it does, we have found a valid pair of numbers. If not, we add the current element to the hash table.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range (len(nums)):
            current = target - nums[i]
            if current in dict:
                return [i, dict[current]]
            else:
                dict[nums[i]] = i
        return [] # If no solution found

# O(n) Time and Space
# Runtime : 3 ms / Memory : 18.84 MB