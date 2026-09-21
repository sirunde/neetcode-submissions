class Solution {
public:
    int characterReplacement(string s, int k) {
        // start from 0, and expand window
        // has k chance to replace.
        // what if abbbbb
        unordered_map<char,int> temp;
        int l = 0, r = 0;
        int output = 0;
        int maxi = 0;
        while(l<=r && r<s.size()){
            temp[s[r]]++;
            if(temp[s[r]] > maxi){
                maxi = temp[s[r]];
            }
            while((r-l+1)-maxi>k){
                temp[s[l++]]--;
            }
            if(output < r-l+1){
                output = r-l+1;
            }
            r++;
        }
        return output;
        // was thinking how to search max if l-- was max and check max again, but
        // dont need to do that



    }
};
