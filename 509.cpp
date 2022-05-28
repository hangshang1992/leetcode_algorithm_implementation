class Solution {
public:
    int fib(int n) {
        if (n <= 1){
            return n;
        }
        int first = 0, second = 1;
        for (int i = 2 ; i <= n; i++){
            int tmp = first;
            first = second;
            second = tmp + first;
        }
        return second;
    }
};
