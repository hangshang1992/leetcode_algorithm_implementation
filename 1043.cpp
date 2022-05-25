#include<iostream>
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(n+1,0);
        for ( int i = 0; i<= n; i++){
            int curMax = 0;
            for ( int j = i-1; (i-j) <= k and j >= 0; j--){
                curMax = max(arr[j], curMax);
                dp[i] = max(dp[i], dp[j] + (i-j) * curMax);
            }
        }
        return dp[n];
    }
};
