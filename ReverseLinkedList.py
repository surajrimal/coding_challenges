# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        ptr = head
        nptr = ptr.next
        head.next = None
        while nptr is not None:
            temp = nptr.next
            nptr.next = ptr
            ptr = nptr
            nptr = temp
        return ptr
            
