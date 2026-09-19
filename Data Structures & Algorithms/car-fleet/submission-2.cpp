class Solution {
   public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> st(n);
        for (int i = 0; i < n; i++) {
            st[i] = {position[i], speed[i]};
        }
        sort(st.begin(), st.end());
        stack<pair<int, int>> temp;

        for (auto& i : st) {
            temp.push(i);
        }
        int output = 0;
        while (!temp.empty()) {
            double time = (double)(target - temp.top().first) / temp.top().second;
            temp.pop();
            while (!temp.empty() && temp.top().first+temp.top().second*time >= target) {
                temp.pop();
            }
            output++;
        }
        return output;
    }
};
