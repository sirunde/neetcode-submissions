class KthLargest {
public:
    int kth;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    KthLargest(int k, vector<int>& nums) {
        this->kth = k;
        for(int num:nums){
            minHeap.push(num);
            if(minHeap.size()>kth){
                minHeap.pop();
            }
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        if(minHeap.size()>kth){
                minHeap.pop();
            }
        return minHeap.top();
    }
};
