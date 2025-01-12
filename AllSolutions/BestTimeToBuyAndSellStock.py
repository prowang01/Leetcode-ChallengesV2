# Approach : Iterating through a loop and calculate profit and the minimum price and update.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float(inf) # Huge number for initialization
        max_profit = 0 # to calculate profit

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(price-min_price, max_profit)
        return max_profit

'''
Runtime : 87 ms / Memory : 26.89 MB
Complexity : O(n) Time / O(1) Space
The loop has O(n) complexity, the operations have constant time O(1)
And we don't have any elements that depends on the variables inside, only two constant variables so O(1).
'''
 

# Two pointers : one for the minimum price, another to find the correct profit.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        for right in range(1, len(prices)) :
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxProfit = max(currentProfit,maxProfit)
            else:
                left = right # if you do left += 1, if you find a value inferior to the current minimum, it won't update
            right += 1
        return maxProfit


'''
Runtime : 91 ms / Memory : 26.85 MB
Complexity : O(n) Time / O(1) space
The loop iterates through the list once, and the rest are constant-time operations / comparisons.
Since no additional data structures (like arrays or hash maps) are used, and all the variables are scalar -> O(1)
'''
