#include <iostream>
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if (nums.size() < 3){
            return 0;
        }
        int res1 = nums[0] + nums[1] + nums[2];
        // cout << res1 << " dr ";
        
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for(int i = 0; i< nums.size() - 2;i++){
            if (i>0 and nums[i-1] == nums[i]){
                continue;
            }
            int left = i+1;
            int right = nums.size() - 1;
            while(left < right){
                int total = nums[i] + nums[left] + nums[right];
                if (abs(target - res1) > abs(total - target)){
                    cout << res1 << " po " << target << " dr ";
                    res1 = total;
                }
                if (total > target){
                    
                    right--;
                }
                else if (total<target){
                    
                    left++;
                }
                else{
                    // res1 = 0;
                    res.push_back(vector<int>{nums[i], nums[left], nums[right]});
                    while (left < right and nums[left] == nums[left + 1]){
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
        // cout << res1 << " mark1 ";
        return res1;
    }
};
