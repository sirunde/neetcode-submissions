class Solution {
   public:
    int numDistinct(string s, string t) {
        int lenS = s.length(), lenT = t.length();

        vector<vector<int>> dp(lenS + 1, vector<int>(lenT + 1, 0));

        for (int j = 0; j <= lenS; j++) {
            dp[j][0] = 1;
        }

        for (int i = 1; i <= lenS; i++) {
            for (int j = 1; j <= lenT; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];

                } 
                else {
                    dp[i][j] = dp[i - 1][j];
                }

                // for (int i = 0; i <= lenS; i++) {
                //     for (int j = 0; j <= lenT; j++) {
                //         std::cout << dp[i][j] << " ";
                //     }
                //     std::cout <<std::endl;
                // }
                // std::cout << std::endl;
            }
            // std::cout << std::endl << std::endl;
        }

        return dp[lenS][lenT];
    }
};
