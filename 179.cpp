class Solution {
public:
    static bool cmp(int a, int b){
        string as = to_string(a),bs = to_string(b);
        return as + bs > bs + as;
    }
    
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), cmp);
        string res;
        for (auto x: nums){
            res += to_string(x);
        }
        if (res[0] == '0'){
            return "0";
        }
        return res;
    }
};
