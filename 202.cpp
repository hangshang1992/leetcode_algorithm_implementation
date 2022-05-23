class Solution {
public:
    bool isHappy(int n) {
        while (n != 1 and n != 4){
            int sum1 = 0;
            while (n){
                sum1 += (n%10)*(n%10);
                n /= 10;
            }
            n = sum1;
        }
        return n == 1;
    }
};
