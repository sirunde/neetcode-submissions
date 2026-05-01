# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        cur = head.next # can be null
        prev = head
        prev.next = None

        while(cur): # while cur is a node

            temp = cur.next # save third node to the temp
            # now switch prev and cur
            # p <- c
            cur.next = prev
            prev = cur
            cur = temp
        return prev




        
            