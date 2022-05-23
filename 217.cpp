class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> q;
        for (int i = 0; i<nums.size();i++){
            if (q.find(nums[i]) != q.end()){
                return true;
            }
            q.insert(nums[i]);
        }
        return false;
    }
};
