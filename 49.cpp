class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, int> m;
        vector<vector<string>> res;
        for(auto str: strs){
            string s = str;
            std::sort(s.begin(), s.end());
            if (!m.count(s)){
                m[s] = res.size();
                res.push_back({});
            }
            res[m[s]].push_back(str);
        }
        return res;
    }
};
