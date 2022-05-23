class Solution {
public:
    int countSubstrings(string s) {
        int res=0, left = 0, right = 0;
        for (int i = 0; i< s.size(); ++i){
            left = i, right = i;
            while(right < s.size() - 1 and s[right] == s[right + 1]){
                right++;
                res++;
            }
            while(right < s.size() and left >= 0 and s[left] == s[right]){
                res++;
                left--;
                right++;
                
            }
        }
        return res;
    }
};
