class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        if (candidates.size() == 0){
            return {};
        }
        std::sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(candidates, target, 0, res, tmp);
        return res;
    }
    void dfs(vector<int>& candidates, int target, int index, vector<vector<int>>& res, vector<int>& tmp){
        if (target < 0){
            return;
        }
        if (target == 0){
            res.push_back(tmp);
            return;
        }
        for (int i = index; i < candidates.size();i++){
            if (i != index and candidates[i] == candidates[i-1]){
                continue;
            }
            tmp.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i+1, res, tmp);
            tmp.pop_back();
        }
    }
};
