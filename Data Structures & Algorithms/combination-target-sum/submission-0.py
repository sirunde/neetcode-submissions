class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []

        def inner(lists,start,total):
            if total == target:
                output.append(lists[:])
                return

            if total > target or start >= len(nums):
                return

            lists.append(nums[start])
            inner(lists,start,total+nums[start])
            lists.pop()
            inner(lists,start+1,total)
            return output
        return inner([],0,0)

                    


