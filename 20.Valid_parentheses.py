class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        round_brackets = 0
        figure_brackets = 0
        square_brackets = 0
        brackets_types = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        brackets_value = {
            '(': round_brackets,
            '[': square_brackets,
            '{': figure_brackets
        }
        count = 0
        unclosed_pair = []
        if len(s) >= 2 and s[0] in brackets_types.keys():
            while count < len(s):
                try:
                    current_obj = s[count]
                    brackets_value[current_obj] += 1
                    if s[count + 1] == brackets_types[current_obj]:
                        count += 2
                        brackets_value[current_obj] -= 1
                    else:
                        count += 1
                        unclosed_pair.append(current_obj)
                except Exception:
                    if brackets_types[unclosed_pair[-1]] == current_obj:
                        brackets_value[unclosed_pair[-1]] -= 1
                        del unclosed_pair[-1]
                        count += 1
                    count += 1

            for elem in brackets_value.values():
                if elem > 0:
                    return False
            return True
        return False





test_data_1 = '()'
test_data_2 = '()[]{}'
test_data_3 = '(]'
test_data_4 = '([])'
test_data_5 = '['
test_data_6 = '){'
print(Solution().isValid(test_data_1))
print(Solution().isValid(test_data_2))
print(Solution().isValid(test_data_3))
print(Solution().isValid(test_data_4))
print(Solution().isValid(test_data_5))
print(Solution().isValid(test_data_6))
