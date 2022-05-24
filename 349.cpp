class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> mp;
        for(auto item: nums1){
            mp[item];
        }
        vector<int> res;
        for (auto item : nums2){
            if (mp.find(item) != mp.end()){
                res.push_back(item);
                mp.erase(item);
            }
        }
        return res;
    }
};
