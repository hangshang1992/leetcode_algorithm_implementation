class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> q;
        unordered_map<int, int> m;
        vector<int> res;
        for (auto x:nums){
            ++m[x];
        }
        for (auto it:m){
            q.push({it.second, it.first});
        }
        for (int i = 0; i<k;i++){
            res.push_back(q.top().second);
            q.pop();
        }
        return res;
    }
};
