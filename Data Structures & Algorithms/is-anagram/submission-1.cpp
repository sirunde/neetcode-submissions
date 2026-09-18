class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int,int> tp1;
        unordered_map<int,int> tp2;
        for(auto& i:s){
            tp1[i-'a']++;
        }
        for(auto& i:t){
            tp2[i-'a']++;
        }
        if(tp1.size()!=tp2.size()){
            return false;
        }
        for(auto&i:tp1){
            if(tp2[i.first] != i.second){
                return false;
            }
        }
        return true;
    }
};
