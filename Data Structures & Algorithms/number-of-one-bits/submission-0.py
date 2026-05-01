class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 1
        total = 0
        while(i<= n):

            if i & n:
                total += 1
            n>>=1

        return total