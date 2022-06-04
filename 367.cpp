class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 2){
            return true;
        }
        int sub = 1;
        while(num > 0){
            num -= sub;
            sub += 2;
        }
        return num == 0;
    }
};
