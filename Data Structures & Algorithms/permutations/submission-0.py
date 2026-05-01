class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def inner(left,temp):
            if not left:
                output.append(temp)
                return

            for i in range(len(left)):
                new = temp[:]
                new.append(left[i])
                inner(left[:i]+left[i+1:],new)

        for i in range(len(nums)):
            new = []
            new.append(nums[i])
            inner(nums[:i]+nums[i+1:],new)
        return output