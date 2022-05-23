class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<string> out;
        vector<vector<string>> res;
        dfs(s, 0, out, res);
        return res;
    }
    void dfs(string s, int start, vector<string>& out, vector<vector<string>>& res){
        if (start == s.size()){
            res.push_back(out);
            return;
        }
        for (int i = start; i < s.size(); ++i){
            if (!isPara(s, start, i)){
                continue;
            }
            out.push_back(s.substr(start, i - start + 1));
            dfs(s, i+1, out, res);
            out.pop_back();
        }
    }
    bool isPara(string s, int start, int end){
        while ( start < end){
            if (s[start] != s[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
