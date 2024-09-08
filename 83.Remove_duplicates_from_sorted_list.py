class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next is None:
            return head
        current_elem = head
        while current_elem.next:
            if current_elem.val == current_elem.next.val:
                current_elem.next = current_elem.next.next
            else:
                current_elem = current_elem.next
        return head
