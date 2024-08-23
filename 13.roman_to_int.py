class Solution(object):

    roman_symbals_value = {
        'I': {
            'value': 1,
            'previous': None
        },
        'V': {
            'value': 5,
            'previous': 'I'
        },
        'X': {
            'value': 10,
            'previous': 'V'
        },
        'L': {
            'value': 50,
            'previous': 'X'
        },
        'C': {
            'value': 100,
            'previous': 'L'
        },
        'D': {
            'value': 500,
            'previous': 'C'
        },
        'M': {
            'value': 1000,
            'previous': 'M'
        },
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        index = 0
        while index <= len(s) - 1:
            current_value = self.roman_symbals_value[s[index]]['value']
            if index != (len(s)-1):
                if self.roman_symbals_value[s[index + 1]]['value'] > current_value:
                    current_value = (
                        self.roman_symbals_value[s[index + 1]]['value'] -
                        self.roman_symbals_value[s[index]]['value']
                    )
                    index += 2
                    result += current_value
                else:
                    index += 1
                    result += current_value
            else:
                result += current_value
                index += 1
        return result


print(Solution().romanToInt('III'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))
