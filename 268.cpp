class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int count = 0, count1 = 0;
        int length = nums.size() + 1;
        for (int i = 0; i < length; i++){
            count += i;
        }
        for (int i = 0; i < nums.size(); i++){
            count1 += nums[i];
        }
        return count - count1;
    }
};
