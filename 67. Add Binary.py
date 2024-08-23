class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = self.binary_to_decimal(a)
        b = self.binary_to_decimal(b)
        result = a + b
        return self.decimail_to_binary(result)

    def binary_to_decimal(self, binary_elem):
        binary_elem = binary_elem
        index = len(binary_elem) - 1
        result = 0
        for elem in binary_elem:
            result += (int(elem) * (2**index))
            index -= 1
        return result

    def decimail_to_binary(self, elem):
        result = ''
        if elem == 0:
            return "0"
        while elem != 0:
            if elem % 2 == 0:
                result += '0'
                elem = elem // 2
            else:
                result += '1'
                elem = elem // 2
        return result[::-1]


print(Solution().binary_to_decimal('0'))
