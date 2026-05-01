class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = set()
        for i in nums:
            if i in table:
                return True
            table.add(i)
        return False
