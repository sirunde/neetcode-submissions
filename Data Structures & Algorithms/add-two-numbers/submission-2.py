# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = 0
        prevNode = None

        while(l1 and l2):
            value = l1.val+l2.val+prev
            temp = ListNode(value%10)

            if (value//10):
                prev = 1
            else:
                prev = 0
            if prevNode:
                prevNode.next = temp
                prevNode = temp
            else:
                prevNode = temp
                head = temp

            l1 = l1.next
            l2 = l2.next

        while(l1):            
            value = l1.val+prev
            temp = ListNode(value%10)
            if (value//10):
                prev = 1
            else:
                prev = 0
            prevNode.next = temp
            prevNode = temp
            l1 = l1.next

        while(l2):            
            value = l2.val+prev
            temp = ListNode(value%10)
            if (value//10):
                prev = 1
            else:
                prev = 0
            prevNode.next = temp
            prevNode = temp

            l2 = l2.next

        if prev:
            temp = ListNode(1)
            prevNode.next = temp
        
        return head