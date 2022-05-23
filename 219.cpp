class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> q;
        for (int i = 0; i < nums.size(); i++){
            if (q.find(nums[i]) != q.end() and abs(i - q.find(nums[i])->second) <= k){
                return true;
            }else{
                q[nums[i]] = i;
            }
        }
        return false;
    }
};
