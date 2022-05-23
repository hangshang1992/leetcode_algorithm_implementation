class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int majority = nums[0];
        for (int i = 1; i < nums.size(); i++){
            if (majority == nums[i]){
                count++;
            }else{
                if (count == 0){
                    count = 1;
                    majority = nums[i];
                }else{
                    count--;
                }
            }
        }
        return majority;
    }
};
