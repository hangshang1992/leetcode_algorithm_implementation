class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        if (nums.size() == 0){
            return {};
        }
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(nums, res, tmp, 0);
        return res;
    }
    void dfs(vector<int>& nums, vector<vector<int>>& res, vector<int>& tmp, int index){
        res.push_back(tmp);
        for (int i = index; i < nums.size(); i++){
            if (i != index and nums[i] == nums[i-1]){
                continue;
            }
            tmp.push_back(nums[i]);
            dfs(nums, res, tmp, i+1);
            tmp.pop_back();
        }
        return;
    }
};
