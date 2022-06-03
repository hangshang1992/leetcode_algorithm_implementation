class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int index = nums.size() - 1, next = 0;
        for(int i = nums.size() - 2; i>= 0; i--){
            if (nums[i] < nums[i+1]){
                index = i;
                break;
            }
        }
        if (index == nums.size() - 1){
            std::sort(nums.begin(), nums.end());
        }else{
            next = index + 1;
            while((next + 1) < nums.size() and nums[index] < nums[next+1]){
                next++;
            }
            int tmp = nums[next];
            nums[next] = nums[index];
            nums[index] = tmp;
            std::sort(nums.begin() + index + 1, nums.end());
        }

    }
};
