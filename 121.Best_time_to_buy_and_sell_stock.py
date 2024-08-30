class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        to_buy = 0
        to_sell = 1
        while to_sell < len(prices):
            if prices[to_sell] > prices[to_buy]:
                result = max(result, prices[to_sell] - prices[to_buy])
            else:
                to_buy = to_sell
            to_sell += 1
        return result


test_1 = [7, 1, 5, 3, 6, 4]
test_2 = [7, 6, 4, 3, 1]
print(Solution().maxProfit(test_1))
print(Solution().maxProfit(test_2))
