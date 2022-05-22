class Solution {
public:
    int climbStairs(int n) {
        if (n < 2){
            return 1;
        }
        int first = 1;
        int second = 1;
        for (int i = 2; i<= n;i++){
            int tmp = first + second;
            first = second;
            second = tmp;
        }
        return second;
    }
};
