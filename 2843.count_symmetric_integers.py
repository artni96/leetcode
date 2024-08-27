class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        result_list = []
        while len(str(low)) % 2 != 0:
            low += 1
        while len(str(high)) % 2 != 0:
            high -= 1
        for elem in range(low, high + 1):
            elem = str(elem)
            if len(elem) % 2 == 0:
                first_part = elem[:len(elem) // 2]
                first_part_sum = 0
                for i in first_part:
                    first_part_sum += int(i)
                second_part = elem[len(elem) // 2:]
                second_part_sum = 0
                for i in second_part:
                    second_part_sum += int(i)
                if first_part_sum == second_part_sum:
                    result_list.append(elem)
        return len(result_list)


print(Solution().countSymmetricIntegers(1, 100))
print(Solution().countSymmetricIntegers(1200, 1230))
print(Solution().countSymmetricIntegers(99, 1782))
# elem = '12'
# first_part = elem[:len(elem) // 2]
# second_part = elem[len(elem) // 2:]
# print(first_part, second_part)