class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        vector<pair<int, int>> vpii;
        for (int i = 0; i<nums.size();i++){
            vpii.push_back({nums[i],i});
        }
        auto less = [](pair<int, int> a, pair<int, int> b) -> bool {return a.first == b.first ? a.second < b.second : a.first < b.first;};
        sort(vpii.begin(), vpii.end(), less);
        for (int i = 0; i < nums.size(); i++){
            for ( int j = i+1; j < nums.size(); j++){
                if ((long long)vpii[j].first - vpii[i].first <= t){
                    if (abs(vpii[i].second - vpii[j].second) <= k){
                        return true;
                    }
                }else{
                    break;
                }
            }
        }
        return false;
    }
};
