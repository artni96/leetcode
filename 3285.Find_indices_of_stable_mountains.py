class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        result = list()
        for elem in range(1, len(height)):
            if height[elem - 1] > threshold:
                result.append(elem)
        return result


test_data_1_height = [1, 2, 3, 4, 5]
test_data_1_treshhold = 2
print(Solution().stableMountains(test_data_1_height, test_data_1_treshhold))
test_data_2_height = [10, 1, 10, 1, 10]
test_data_2_treshhold = 3
print(Solution().stableMountains(test_data_2_height, test_data_2_treshhold))
