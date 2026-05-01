class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        temp = [[] for _ in range(n+1)]
        counter = Counter(nums)
        print(counter)
        output = []
        for key,value in counter.items():
            temp[value].append(key)

        for i in temp[::-1]:
            output.extend(i)
            if len(output) == k:
                return output