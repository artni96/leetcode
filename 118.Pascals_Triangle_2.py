class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        if rowIndex >= 0:
            result.append(1)
        if rowIndex >= 1:
            result.append(1)
        if rowIndex >= 2:
            for elem in range(2, rowIndex + 1):
                current_result = [(result[i - 1] + result[i]) for i in range(1, len(result))]
                result = [1] + current_result + [1]
        return result


print(Solution().getRow(33))