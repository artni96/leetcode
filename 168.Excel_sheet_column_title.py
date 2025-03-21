from string import ascii_uppercase

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # counter = 1
        # abc = dict.fromkeys(ascii_uppercase)
        # for elem in ascii_uppercase:
        #     abc[elem] = counter
        #     counter += 1
        # reversed_input = columnNumber[::-1]
        # result = 0
        # for elem in range(len(reversed_input)):
        #     if elem == 0:
        #         result += abc[reversed_input[elem]]
        #     else:
        #         result += (elem * len(abc)) * abc[reversed_input[elem]]
        # return result
        abc = dict()
        counter = 1
        for elem in ascii_uppercase:
            abc[counter] = elem
            counter += 1
        print(abc)
        counter = 0
        index_list = list()
        while columnNumber >= 26:
            columnNumber //= 26
            index_list.append(co)
            counter += 1
        print(columnNumber)
        print(counter)


print(Solution().convertToTitle(701))
