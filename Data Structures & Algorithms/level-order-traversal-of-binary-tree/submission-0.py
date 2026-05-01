# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        dq = [root]
        output = []
        while(dq):
            output.append([i.val for i in dq if i is not None])
            temp = []

            for i in dq:
                if i is None:
                    continue

                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            
            dq = temp

        return output