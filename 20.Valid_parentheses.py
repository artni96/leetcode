class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_types = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        count = 0
        unclosed_pair = []
        if len(s) >= 2 and len(s) % 2 == 0:
            while count < len(s):
                current_obj = s[count]
                if current_obj in brackets_types:
                    if count + 1 <= len(s) - 1:
                        if s[count + 1] == brackets_types[current_obj]:
                            count += 2
                        else:
                            count += 1
                            unclosed_pair.append(current_obj)
                    else:
                        if len(unclosed_pair) > 0:
                            return False
                elif len(unclosed_pair) >= 1:
                    if current_obj == brackets_types[unclosed_pair[-1]]:
                        del unclosed_pair[-1]
                        count += 1
                    elif current_obj != brackets_types[unclosed_pair[-1]]:
                        return False
                else:
                    return False
            if len(unclosed_pair) > 0 and count == len(s):
                return False
            return True
        return False


test_data_1 = '()'
test_data_2 = '()[]{}'
test_data_3 = '(]'
test_data_4 = '([])'
test_data_5 = '['
test_data_6 = '){'
test_data_7 = '(){}}{'
test_data_8 = '(('
test_data_9 = '[[[[[[[[[[[[[[[[[[['
print(Solution().isValid(test_data_1))
print(Solution().isValid(test_data_2))
print(Solution().isValid(test_data_3))
print(Solution().isValid(test_data_4))
print(Solution().isValid(test_data_5))
print(Solution().isValid(test_data_6))
print(Solution().isValid(test_data_7))
print(Solution().isValid(test_data_8))
print(Solution().isValid(test_data_9))
