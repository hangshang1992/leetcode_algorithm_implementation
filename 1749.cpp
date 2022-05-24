class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int ans = abs(nums[0]);
        vector<int> per(nums);
        int n = nums.size();
        for (int i = 1; i< n; i++){
            per[i] += per[i-1];
        }
        int MAX = per[0];
        int MIN = per[0];
        for (int i = 1; i < n; i++){
            int sum = per[i];
            // ans = max(ans, max(abs(per[i]), max(abs(MAX + per[i]), abs(per[i] - MIN))));
            ans = max(ans, max(abs(sum), max(abs(sum-MIN), abs(sum-MAX))));
            MAX = max(MAX, per[i]);
            MIN = min(MIN, per[i]);
        }
        return ans;
    }
};
