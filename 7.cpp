class Solution {
public:
    int reverse(int x) {
        

        if (x<10 and x>= 0){
            return x;
        }
        long long temp = 0 ;
        while(x!= 0){
            if (abs(temp) > INT_MAX / 10) return 0;
            int tmp = x%10;
            temp = temp * 10 + tmp;
            x /= 10;
        }
        return temp;
    }
};
