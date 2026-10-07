class Solution {
public:
    struct Compare {
        bool operator()(const vector<int>& a, const vector<int>& b) const {
            return (a[0]*a[0]+a[1]*a[1]) < (b[0]*b[0]+b[1]*b[1]);
        }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue <vector<int>,vector<vector<int>>, Compare> temp;
        vector<vector<int>> output;
        for(auto& i:points){
            temp.push(i);
        }
        while(temp.size()>k){
            temp.pop();
        }
    while (!temp.empty()) {
        output.push_back(temp.top());
        temp.pop();
    }
        return output;
    }
};
