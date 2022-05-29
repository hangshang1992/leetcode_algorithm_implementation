class Solution {
public:
    string longestPalindrome(string s) {
        if ( s.size() < 2){
            return s;
        }
        int maxLen = 0;
        int start = 0;
        for(int i = 0; i < s.size() - 1; i++){
            isPalin(s, i, i+1, start, maxLen);
            isPalin(s, i, i, start, maxLen);
        }
        return s.substr(start, maxLen);
    }
    
    void isPalin(string s, int l, int r, int& start, int& maxLen){
        while(l >= 0 and r < s.size() and s[l] == s[r]){
            l--;
            r++;
        }
        if(maxLen < r - l -1){
            maxLen = r- l - 1;
            start = l + 1;
        }
    }
    
    
}; 
