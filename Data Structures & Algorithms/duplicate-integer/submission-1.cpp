class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> temp;
        for(auto&i:nums){
            if(temp.contains(i)){
                return true;
            }
            temp.insert(i);
        }
        return false;
    }
};