class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[0][0] = True
        if len(s1) + len(s2) != len(s3):
            return False
        for idx in range(len(s1)+1):
            for jdx in range(len(s2)+1):
                if idx > 0 and s1[idx-1] == s3[idx+jdx-1]:
                    dp[idx][jdx] |= dp[idx-1][jdx]

                if jdx > 0 and s2[jdx-1] == s3[idx+jdx-1]:
                    dp[idx][jdx] |= dp[idx][jdx-1]

                
        return dp[len(s1)][len(s2)]