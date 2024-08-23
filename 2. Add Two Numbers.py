class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        extra_point = 0
        if len(l1) > len(l2):
            max_l = l1[::-1]
            min_l = l2[::-1]
        else:
            max_l = l2[::-1]
            min_l = l1[::-1]
        for elem in range(len(max_l)):
            if elem <= len(min_l) - 1:
                current_sum = max_l[elem] + min_l[elem] + extra_point
            else:
                current_sum = max_l[elem] + extra_point
            extra_point = 0
            if current_sum >= 10:
                extra_point += 1
            result.append(current_sum % 10)
        if extra_point != 0:
            result.append(extra_point)
        return result


l1 = [2, 4, 3]
l2 = [5, 6, 4]
# l1 = [0]
# l2 = [0]
# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
print(Solution().addTwoNumbers(l1, l2))
