class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = INT_MIN, curSum = 0;
        for (auto num : nums){
            curSum = max(curSum + num, num);
            res = max(curSum, res);
        }
        return res;
    }
};
