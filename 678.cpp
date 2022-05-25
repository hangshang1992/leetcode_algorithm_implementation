class Solution {
public:
    bool checkValidString(string s) {
        int Lmin = 0, Lmax = 0, n = s.size();
        for (int i = 0; i < n; i++){
            if (s[i] == '('){
                Lmin++;
                Lmax++;
            }else if (s[i] == ')'){
                if (Lmin > 0){
                    Lmin--;
                }
                Lmax--;
                if (Lmax < 0){
                    return false;
                }
            }else{
                if (Lmin>0){
                    Lmin--;
                }
                Lmax++;
            }
        }
        return Lmin<=0 and Lmax >= 0;
    }
};
