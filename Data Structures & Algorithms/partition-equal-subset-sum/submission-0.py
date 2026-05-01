class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total%2: # if sum is odd, subsets are not equal
            return False

        half = total//2

        # for faster calculation, after sorting, 
        # if last value is larger than half, 
        # return False, because it is impossible to have equal subset sum
        output = set()
        # print(output)
        for i in nums:
            # print(output)
            temp = set()
            for j in output:
                temp.add(i+j)
            # print(temp)
            output = output.union(temp)
            output.add(i)
            if half in output:
                return True

        return False
        



