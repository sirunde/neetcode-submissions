class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n+2) for _ in range(n+2)]

        new = [1]+ nums + [1] # to easily iterate

        for l in range(n,0,-1): # choosing start range. We iterate from backward because that way we can make l to 0 at the end
            for r in range(l,n+1): # choosing end range
                for i in range(l,r+1): # choose last pop
                    coins = new[l-1]*new[i]*new[r+1] # since in range all popped except i, new[l-1]*new[i]*new[r+1]
                    coins += dp[l][i-1]+dp[i+1][r] # remember l-r is all popped execpt i, that means l to i-1 and i+1 to r should be added
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]
                    
