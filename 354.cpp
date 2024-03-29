class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int res = 1;
        std::sort(envelopes.begin(), envelopes.end());
        int n = envelopes.size();
        vector<int> dp(n, 1);
        for(int i = 1; i < n; i++){
            for (int j = 0; j < i; j++){
                if (envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]){
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            res = max(res, dp[i]);
        }
        return res;
    }
};
