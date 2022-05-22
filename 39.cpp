#include<iostream>
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        if (candidates.size() == 0){
            return {};
        }
        vector<vector<int>> res;
        vector<int> tmp;
        // cout << " hello4 " << candidates[0] << " ds ";
        dfs(candidates, target, res, 0, tmp);
        return res;
    }
    void dfs(vector<int>& candidates, int target, vector<vector<int>>& res, int index, vector<int>& tmp){
        // cout << " hello3 " << index << " ds ";
        if (target < 0){
            return;
        }
        if (target == 0){
            res.push_back(tmp);
            // cout << res.size() << " mark1 ";
            return;
        }
        // cout << " hello2 " << index << " ds ";
        for (int i = index; i < candidates.size(); i++){
            tmp.push_back(candidates[i]);
            // cout << " hello1 " << candidates[i] << " df " << target;
            dfs(candidates, target - candidates[i], res, i, tmp);
            tmp.pop_back();
        }
        return;
    }
};
