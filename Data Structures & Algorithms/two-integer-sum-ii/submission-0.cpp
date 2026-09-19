class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // increasing order
        unordered_map<int,int> temp;
        for(int i = 0;i<numbers.size();i++){
            // std::cout << i << ' ' << numbers[i] << ' ';
            if(temp.contains(target-numbers[i])){
                return {temp[target-numbers[i]]+1,i+1};
            }

            temp[numbers[i]] = i;
        }
        return {-1,-1};
    }
};
