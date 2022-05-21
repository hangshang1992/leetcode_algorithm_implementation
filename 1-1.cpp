class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> umap;
        for (int i = 0; i < nums.size();i++){
            int tmp = target - nums[i];
            if (umap.find(tmp) != umap.end()){
                return {umap.find(tmp)->second, i};
            }
            umap.insert(pair<int, int>(nums[i], i));
        }
        return {};
    }
};
