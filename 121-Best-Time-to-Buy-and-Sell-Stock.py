"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find 
the maximum profit.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        list1 = []
        for i in range(len(prices) - 1):
            list1.append(prices[i + 1] - prices[i])
        if len(list1) == 1:
            return [list1[0], 0][list1[0] < 0]
        for i in range(1, len(list1)):
            list1[i] = max(list1[i], list1[i] + list1[i - 1])
        return [max(list1), 0][max(list1) < 0]

s = Solution()
print s.maxProfit([1, 8, 9, 5])