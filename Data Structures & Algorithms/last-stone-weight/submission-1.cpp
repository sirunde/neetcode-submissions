class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> max_heap;
        for(auto&i:stones){
            max_heap.push(i);
        }
        while(max_heap.size()>=2){
        int first = max_heap.top();
        max_heap.pop();
        int second = max_heap.top();
        max_heap.pop();
        if (first>second){
            max_heap.push(first-second);
        }
        else if(first == second){
            continue;
        }
        else if(first < second){
            max_heap.push(second-first);
        }
        }
        return max_heap.size() ? max_heap.top() : 0;
    }
};
