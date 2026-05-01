class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = [0]*(amount+1)
        n[0] = 1
        for i in coins:
            for j in range(i,amount+1):
                n[j] += n[j-i]

        return n[-1]
