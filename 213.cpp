#include<iostream>
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0){
            return 0;
        }
        if (nums.size() == 1){
            return nums[0];
        }
        if (nums.size() == 2){
            return max({nums[0], nums[1]});
        }
        // cout << "hello1 " << nums[0];
        int m = nums.size();
        vector<int> dp(m, 0);
        dp[0] = nums[0];
        dp[1] = max({nums[0], nums[1]});
        for (int i = 2; i<m-1;i++){
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
            // cout << "mark1233 " << dp[i] << " " << i << endl;
        }
        vector<int> dp1(m, 0);
        dp1[1] = nums[1];
        dp1[2] = max({nums[1], nums[2]});
        for (int i = 3; i<m;i++){
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }
        // cout << "mar1 " << dp1[m-1] << " dd " << dp[m-2];
        return max({dp1[m-1], dp[m-2]});
        // return 0;
    }
};
