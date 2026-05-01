"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = {None:None}
        cur = head
        while(cur):
            new = Node(cur.val)
            temp[cur] = new
            cur = cur.next
        cur = head

        while(cur):
            copy = temp[cur]
            copy.next = temp[cur.next]
            copy.random = temp[cur.random]
            cur = cur.next
        return temp[head]