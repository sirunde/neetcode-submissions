class Solution {
   public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> boundary;
        // doesnt has to be consecutive in the original array
        int maxi = 0;
        for (auto& i : nums) {
            // when add+1, check left and right
            if (boundary[i] == 0) {
                boundary[i] = boundary[i - 1] + boundary[i + 1] + 1;
                boundary[i - boundary[i - 1]] = boundary[i];
                boundary[i + boundary[i + 1]] = boundary[i];
                if (maxi < boundary[i]) {
                    maxi = boundary[i];
                }
                // std::cout <<i << ' ' << boundary[i-1] << ' ' << boundary[i] << ' ' << boundary[i+1] <<std::endl;

            }
        }
        return maxi;
    }
};
