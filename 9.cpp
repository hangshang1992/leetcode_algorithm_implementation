#include<iostream>
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        if (x >= 0 && x < 10){
            return true;
        }
        long long temp = 0;
        long long xx = x;
        while (x != 0){
            int n = x % 10;
            temp = temp * 10 + n;
            x /= 10;
        }
        if (temp == xx){
            return true;
        }else{
            return false;
        }
    }
};
