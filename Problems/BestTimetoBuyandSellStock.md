# Best Time to Buy and Sell Stock

## Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a **single day to buy one stock** and choosing a **different day in the future to sell that stock**.

Return the **maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

---

## Examples

### Example 1:
**Input:**  
`prices = [7,1,5,3,6,4]`  
**Output:**  
`5`

**Explanation:**  
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.  
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

---

### Example 2:
**Input:**  
`prices = [7,6,4,3,1]`  
**Output:**  
`0`

**Explanation:**  
In this case, no transactions are done and the max profit = 0.

---

## Constraints:
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Performance:
- **Runtime:** 87 ms  
- **Memory Usage:** 26.89 MB  

---

## Complexity:
- **Time Complexity:**  
   - `O(n)` where `n` is the length of the `prices` array. The loop iterates through the array once.
- **Space Complexity:**  
   - `O(1)` since only a constant amount of extra space is used.

---

## Approach: Iterating through a loop and calculating profit and the minimum price

### Steps:
1. Initialize `min_price` to a very large number (`float('inf')`) to track the lowest price seen so far.
2. Initialize `max_profit` to 0 to store the maximum profit calculated.
3. Iterate through the `prices` array:
   - If the current price is less than `min_price`, update `min_price`.
   - Otherwise, calculate the potential profit (`price - min_price`) and update `max_profit` if this profit is higher.
4. Return `max_profit` at the end of the loop.

---

## Code:
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  
        max_profit = 0  

        for price in prices:
            if price < min_price:
                min_price = price  
            else:
                max_profit = max(max_profit, price - min_price)  

        return max_profit
```
