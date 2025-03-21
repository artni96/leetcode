from itertools import permutations, product


class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        hours_list = [1, 2, 4, 8]
        minutes_list = [1, 2, 4, 8, 16, 32]
        result_hours_list = [
            sum(elem) for elem in permutations(hours_list, turnedOn)]
        result_minutes_list = [
            sum(elem) for elem in permutations(minutes_list, turnedOn)]
        result = [elem for elem in product(result_hours_list, result_minutes_list)]
        return result


print(Solution().readBinaryWatch(1))
