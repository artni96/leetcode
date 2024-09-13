from string import ascii_uppercase


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        counter = 1
        abc = dict.fromkeys(ascii_uppercase)
        for elem in ascii_uppercase:
            abc[elem] = counter
            counter += 1
        reversed_input = columnTitle[::-1]
        result = 0
        for elem in range(len(reversed_input)):
            if elem == 0:
                result += abc[reversed_input[elem]]
            else:
                result += (len(abc) ** elem) * abc[reversed_input[elem]]
        return result


print(Solution().titleToNumber('A'))
print(Solution().titleToNumber('AB'))
print(Solution().titleToNumber('FXSHRXW'))
