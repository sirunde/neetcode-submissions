class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        output = [0]
        for i in nums:
            temp = []
            for j in output:
                temp.append(j+i)
                temp.append(j-i)
            output = temp
        
        # print(output)
        output = Counter(output)
        return output[target]
