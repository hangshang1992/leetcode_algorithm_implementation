class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        while(true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if(slow == fast){
                break;
            }
        }
        int find = 0;
        while(true){
            slow = nums[slow];
            find = nums[find];
            if(slow == find){
                return slow;
            }
        }
    }
};
