class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        while len(num) >= 2:
            current_num = 0
            for elem in list(num):
                current_num += int(elem)
            num = str(current_num)
        return int(num)


test_data_1 = -38
print(Solution().addDigits(test_data_1))
