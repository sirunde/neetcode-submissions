class Solution {
   public:
    bool checkInclusion(string s1, string s2) {
        int windo = s1.size();
        unordered_map<char, int> temp;
        int tracking = 0;

        // edge case when s1 larger than s2
        if (s2.size() < windo) {
            return false;
        }

        for (auto& i : s1) {
            temp[i]++;
        }
        tracking = temp.size();
        // for (auto& i : temp) {
        //     std::cout << i.first << ' ' << i.second << ", ";
        // }
        // std::cout << std::endl;
        for (int i = 0; i < windo; i++) {
            if (temp.contains(s2[i])) {
                if (temp[s2[i]] == 0) {
                    tracking++;
                }
                temp[s2[i]]--;
                if (temp[s2[i]] == 0) {
                    tracking--;
                }
            }
        }
        // for (auto& i : temp) {
        //     std::cout << i.first << ' ' << i.second << ", ";
        // }
        // std::cout << std::endl;
        // check if 0 to windo is correct
        if (tracking == 0) return true;

        for (int i = windo; i < s2.size(); i++) {
            // for (auto& i : temp) {
            //     std::cout << i.first << ' ' << i.second << ", ";
            // }
            if (temp.contains(s2[i - windo])) {
                if (temp[s2[i - windo]] == 0) {
                    tracking++;
                }
                temp[s2[i - windo]]++;
                if (temp[s2[i - windo]] == 0) {
                    tracking--;
                }
            }
            if (temp.contains(s2[i])) {
                if (temp[s2[i]] == 0) {
                    tracking++;
                }
                temp[s2[i]]--;
                if (temp[s2[i]] == 0) {
                    tracking--;
                }
            }
            if (tracking == 0) return true;
        }
        return false;
    }
};
