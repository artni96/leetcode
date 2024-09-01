class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        result = 0
        if a > 0:
            list_1 = [1] * a
        elif a == 0:
            list_1 = list()
        else:
            list_1 = [0] * abs(a)
        if b > 0:
            list_2 = [1] * b
        elif b == 0:
            list_2 = list()
        else:
            list_2 = [0] * abs(b)
        if len(list_1) > 0 and len(list_2) > 0:
            if list_1[0] != 1 or list_2[0] != 1:
                if list_1[0] == 0 and list_2[0] == 0:
                    list_1.extend(list_2)
                    result = -len(list_1)
                elif list_1[0] == 0 or list_2[0] == 0:
                    if list_1[0] == 0:
                        if len(list_1) > len(list_2):
                            list_1 = list_1[:len(list_1) - len(list_2)]
                            result = -len(list_1)
                        else:
                            list_2 = list_2[:len(list_2) - len(list_1)]
                            result = len(list_2)
                    else:
                        if len(list_1) < len(list_2):
                            list_2 = list_2[:len(list_2) - len(list_1)]
                            result = -len(list_2)
                        else:
                            list_1 = list_1[:len(list_1) - len(list_2)]
                            result = len(list_1)
            else:
                list_1.extend(list_2)
                result = len(list_1)
        elif len(list_1) == 0 or len(list_2) == 0:
            if len(list_1) > 0:
                if list_1[0] == 1:
                    result = len(list_1)
                else:
                    result = -len(list_1)
            elif len(list_2) > 0:
                if list_2[0] == 1:
                    result = len(list_2)
                else:
                    result = -len(list_2)
        return result


assert -2 == Solution().getSum(-1, -1)
assert 0 == Solution().getSum(1, -1)
assert 0 == Solution().getSum(-1, 1)
assert 1 == Solution().getSum(1, 0)
assert 1 == Solution().getSum(0, 1)
assert 0 == Solution().getSum(0, 0)
assert 2 == Solution().getSum(1, 1)
assert 2 == Solution().getSum(-14, 16)
assert 2 == Solution().getSum(16, -14)
assert -30 == Solution().getSum(-16, -14)
assert -2 == Solution().getSum(-16, 14)
assert -2 == Solution().getSum(14, -16)
assert -1 == Solution().getSum(-1, 0)

