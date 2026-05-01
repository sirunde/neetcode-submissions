class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        temp = []
        for i in strs:
            counter = Counter(i)
            if counter not in temp:
                output.append([i])
                temp.append(counter)
            else:
                idx = temp.index(counter)
                output[idx].append(i)
        return output