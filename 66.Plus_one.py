class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        for i in range(len(digits)):
            if digits[::-1][i] == 9:
                if i == 0:
                    part_to_change = digits[i:]
                    digits = list()
                else:
                    part_to_change = digits[i-1:]
                    digits = digits[:i-1]
                break
        result = list(str(int(''.join([str(elem) for elem in part_to_change])) + 1))
        return digits + [int(elem) for elem in result]


test_data_1 = [1, 2, 3]
test_data_2 = [7, 8, 9, 9, 9]
test_data_3 = [9, 9]
test_data_4 = [4, 0, 9, 2, 6, 5, 9]
print(Solution().plusOne(test_data_1))
print(Solution().plusOne(test_data_2))
print(Solution().plusOne(test_data_3))
print(Solution().plusOne(test_data_4))
