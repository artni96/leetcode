class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {elem: 0 for elem in nums if elem % 2 == 0}
        for elem in nums:
            if elem % 2 == 0:
                hm[elem] += 1
        result = [-1, 0]
        for elem, value in hm.items():
            if result[0] == -1:
                result[0] = elem
                result[1] = value
            elif result[1] == value:
                result[0] = min(result[0], elem)
            elif result[1] < value:
                result[0] = elem
                result[1] = value
        return result[0]


test_data_1 = [0, 1, 2, 2, 4, 4, 1]
test_data_2 = [4, 4, 4, 9, 2, 4]
test_data_3 = [29, 47, 21, 41, 13, 37, 25, 7]
test_data_4 = [1000]
test_data_5 = [8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]
print(Solution().mostFrequentEven(test_data_1))
print(Solution().mostFrequentEven(test_data_2))
print(Solution().mostFrequentEven(test_data_3))
print(Solution().mostFrequentEven(test_data_4))
print(Solution().mostFrequentEven(test_data_5))
