class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> nums;
        for (int i = 1; i <= n; i++){
            nums.push_back(i);
        }
        vector<vector<int>> res;
        vector<int> out;
        dfs(nums, res, out, k, 0);
        return res;
    }
    void dfs(vector<int>& nums, vector<vector<int>>& res, vector<int>& out, int k, int index){
        if (out.size() == k){
            res.push_back(out);
            return;
        }
        for (int i = index; i < nums.size(); i++){
            out.push_back(nums[i]);
            dfs(nums, res, out, k, i+1);
            out.pop_back();
        }
        return ;
    }
};
