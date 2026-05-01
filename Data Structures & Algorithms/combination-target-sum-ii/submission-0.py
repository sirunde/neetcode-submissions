class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def inner(lists,start,total):
            if total == target and lists not in output:
                output.append(lists[:])
                return

            if total > target or start >= len(nums):
                return

            lists.append(nums[start])
            inner(lists,start+1,total+nums[start])
            lists.pop()
            inner(lists,start+1,total)
            return output
        
        return inner([],0,0)