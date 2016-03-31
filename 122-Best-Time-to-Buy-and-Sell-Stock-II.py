"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock 
multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        list1 = [prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] - prices[i] > 0]
        return sum(list1)
s = Solution()
print s.maxProfit([1, 2, 3, 4, 5, 6, 4])