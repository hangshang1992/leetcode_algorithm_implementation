class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> tmp;
        vector<int> visited(nums.size(), 0);
        dfs(nums, res, tmp, visited);
        return res;
    }
    void dfs(vector<int>& nums, vector<vector<int>>& res, vector<int>& tmp, vector<int>& visited){
        if(nums.size() == tmp.size()){
            res.push_back(tmp);
            return;
        }
        for(int i = 0; i < nums.size(); i++){
            if (visited[i] == 1){
                continue;
            }
            if (i > 0 and nums[i] == nums[i-1] and visited[i-1] == 0){
                continue;
            }
            visited[i] = 1;
            tmp.push_back(nums[i]);
            dfs(nums, res, tmp, visited);
            visited[i] = 0;
            tmp.pop_back();
        }
        return;
    }
    
   
   
};
