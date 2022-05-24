class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int majority1 = -1, majority2 = -1, count1 = 0, count2 = 0;
        for (int i = 0; i <nums.size(); i++){
            if (count1 > 0 and majority1 == nums[i]){
                count1++;
                continue;
            }
            if (count2 > 0 and majority2 == nums[i]){
                count2++;
                continue;
            }
            if (count1 == 0){
                majority1 = nums[i];
                count1++;
                continue;
            }
            if (count2 == 0){
                majority2 = nums[i];
                count2++;
                continue;
            }
            count1--;
            count2--;
        }
        vector<int> res;
        if (majority1 == majority2){
            return {majority1};
        }
        for(auto item:{majority1, majority2}){
            int count = 0;
            for (int i = 0; i < nums.size();i++){
                if (item == nums[i]){
                    count++;
                }
            }
            if (count > nums.size()/3){
                res.push_back(item);
            }
        }
        return res;
    }
};
