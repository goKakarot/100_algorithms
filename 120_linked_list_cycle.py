"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if head is None:
            return False
        slow, fast = head, head.next
        result = False
        while fast is not None or fast.next is not None:
            if fast == slow:
                result = True
            slow = slow.next
            fast = fast.next.next
        return result

