class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int high1 = -1001, high2 = -1001, high3 = -1001, low1 = 1001, low2 = 1001;
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] >= high1){
                high3=high2,high2=high1,high1=nums[i];
                // high3 = high2;
                // high2 = high1;
                // high1 = nums[i];
                
            }else if (nums[i] >= high2){
                high3=high2,high2=nums[i];
                // high3 = high2;
                // high2 = nums[i];
            }else if (nums[i] >= high3){
                high3 = nums[i];
            }
            if (nums[i] <= low1){
                low2=low1,low1=nums[i];
                // low2 = low1;
                // low1 = nums[i];
            }else if (nums[i] <= low2){
                low2 = nums[i];
            }
        }
        return max(low2*low1*high1,high1*high2*high3);
    }
};
