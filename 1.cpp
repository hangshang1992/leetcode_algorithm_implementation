#include <map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> my_map;
        vector<int> a1;
        for (int i = 0; i < nums.size(); i++){
            int a = nums[i];
            int b = target - a;
            if (my_map.find(a) == my_map.end()){ 
                my_map[b] = i;
            }else{
                
                map<int,int>::iterator it;
                it = my_map.find(a);
                a1.push_back(it->second);
                a1.push_back(i);
                return a1;
            }
        }
        
        return a1;
    }
};
