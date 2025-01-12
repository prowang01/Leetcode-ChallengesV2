# Approach : Two Pointers at both edges of the list, and one fixed index that is the loop itself.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        result = []
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1] :       
                continue # skip the duplicate 'i'
            left = i+1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1          # continue finding all the combinations
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:  # the while loop inside because left and right
                        left += 1                                       # already moved once
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1 
        return result
        
'''
Runtime : 596 ms / Memory : 20.68 MB
Complexity : O(n^2) Time / O(k) Space with k being the number of unique triplets possible

Time : sorting the list takes O(nlogn)
the external loop takes O(n)
and the two pointers (while left < right) processes the rest of the list, so O(n)
so we have O(nlogn + n^2) = O(n^2)

Space : the sorting takes nothing because we sort in place,
all the variables are scalar, so constant-space
but for the result, it's possible to have every combination of i, left, and right valid and unique, so k unique triplets.
'''






# Approach: Divide and conquer using sets for efficient lookups
#
# 1. Split the input list into three separate lists:
#    - `n` for negative numbers
#    - `p` for positive numbers
#    - `z` for zeros
#    This categorization allows us to process each group efficiently.
#
# 2. Create two sets `N` and `P` for fast O(1) lookups:
#    - `N` contains all unique negative numbers
#    - `P` contains all unique positive numbers
#    This helps to quickly check for complements when forming triplets.
#
# 3. Handle cases with zeros:
#    - If there is at least one zero in the input, for each positive number in `P`,
#      check if its negative counterpart exists in `N`. If so, add the triplet `(-num, 0, num)`.
#    - If there are at least three zeros in `z`, include the triplet `(0, 0, 0)`.
#
# 4. Process pairs of negative numbers:
#    - For every pair of numbers in `n`, compute their complement (`-(n[i] + n[j])`).
#    - Check if this complement exists in `P`. If it does, add the triplet to the result.
#
# 5. Process pairs of positive numbers:
#    - Similarly, for every pair of numbers in `p`, compute their complement (`-(p[i] + p[j])`).
#    - Check if this complement exists in `N`. If it does, add the triplet to the result.
#
# 6. Return the result as a set to ensure unique triplets:
#    - The use of `tuple(sorted(...))` ensures that triplets are added in a consistent order.
#    - Convert the result set to a list of lists before returning, as required by the problem.
#
# Time Complexity:
# - Splitting the input into three lists: O(n)
# - Processing pairs of negative and positive numbers: O(n^2)
# - Overall: O(n^2), which is efficient for this problem.
#
# Space Complexity:
# - Storing the input in three separate lists and two sets: O(n)
# - Overall: O(n)

'''
It's supposed to work, but the solutions on Leetcode didn't.
'''