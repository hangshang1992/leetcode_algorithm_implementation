class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(nums, res, 0, tmp);
        return res;
    }
    void dfs(vector<int>& nums, vector<vector<int>>& res, int index, vector<int>& tmp){
        res.push_back(tmp);
        for (int i = index; i < nums.size(); i++){
            tmp.push_back(nums[i]);
            dfs(nums, res, i+1, tmp);
            tmp.pop_back();
        }
    }
};
