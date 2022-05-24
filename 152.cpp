class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        vector<int> f(n, 0), g(n,0);
        f[0] = nums[0];
        g[0] = nums[0];
        int res = nums[0];
        for (int i = 1; i < nums.size();i++){
            f[i] = max({nums[i], f[i-1] * nums[i], g[i-1] * nums[i]});
            g[i] = min({nums[i], f[i-1] * nums[i], g[i-1] * nums[i]});
            res = max(f[i], res);
        }
        return res;
    }
};
