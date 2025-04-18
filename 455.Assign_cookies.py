class Solution(object):
    def findContentChildren(self, g:list, s:list):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # g = order s = drone
        g.sort()
        s.sort()
        s_index, g_index = 0, 0
        result = 0

        while s_index < len(s) and g_index < len(g):
            if g[g_index] <= s[s_index]:
                g_index += 1
                s_index += 1
                result += 1
            elif g[g_index] > s[s_index]:
                s_index += 1
        return result


g_test_1 = [1, 2]
s_test_1 = [1, 2, 3]
print(Solution().findContentChildren(g_test_1, s_test_1))
