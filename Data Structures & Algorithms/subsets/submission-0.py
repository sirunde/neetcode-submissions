import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        # call output again and append i at the end
        for i in nums:

            temp = copy.deepcopy(output)

            for j in temp:

                j.append(i)


            output.extend(temp)

        return output