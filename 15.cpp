class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (nums.size() < 3 ){
            return {};
        }
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size() - 2; i++){
            if (i > 0 and nums[i] == nums[i-1]){
                continue;
            }
            int left = i+1;
            int right = nums.size() - 1;
            while (left < right){
                int total = nums[i] + nums[left] + nums[right];
                if (total > 0){
                    right--;
                }else if (total < 0) {
                    left++;
                }else{
                    res.push_back(vector<int>{nums[left], nums[i], nums[right]});
                    while (left < right and nums[left] == nums[left+1]){
                        left++;
                    }
                    while(left < right and nums[right] == nums[right-1]){
                        right--;
                    }
                    left++;
                    right--;
                }
            }
        }
        return res;
        
    }
};
