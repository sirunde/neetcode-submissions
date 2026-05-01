class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        total = 0
        last = 0
        for idx,i in enumerate(s):

            if i not in temp:
                temp.add(i)

            else:
                total = max(total,idx-last)

                for jdx in range(last,idx):

                    if s[jdx] != i:
                        temp.remove(s[jdx])

                    else:
                        last = jdx+1
                        break
        return max(total,len(temp))