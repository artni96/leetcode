class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node_list = ListNode()
        head = node_list
        while list1 and list2:
            if list1.val < list2.val:
                node_list.next = list1
                list1 = list1.next
            else:
                node_list.next = list2
                list2 = list2.next
            node_list = node_list.next
        if list1:
            node_list.next = list1
        elif list2:
            node_list.next = list2
        return head.next
