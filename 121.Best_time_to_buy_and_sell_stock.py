class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        result = 0
        while r < len(prices):
            cur_result = prices[r] - prices[l]
            if prices[l] < prices[r]:
                result = max(result, cur_result)
            else:
                l = r
            r += 1
        return result


test_1 = [7, 3, 5, 1, 6, 4]
test_2 = [7, 6, 4, 3, 1]
print(Solution().maxProfit(test_1))
print(Solution().maxProfit(test_2))
