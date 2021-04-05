#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

#Notice that you should not modify the linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return 
        ptr = head
        ptr.val = str(ptr.val)
        while(ptr.next != None):
            if(ptr.val =="str"):
                return ptr
            ptr.val = "str"
            ptr = ptr.next
        return 
