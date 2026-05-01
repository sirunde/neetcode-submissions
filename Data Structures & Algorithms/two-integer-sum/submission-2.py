class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for idx,i in enumerate(nums):
            if target-i in a:
                return [a[target-i],idx]
            a[i] = idx
        