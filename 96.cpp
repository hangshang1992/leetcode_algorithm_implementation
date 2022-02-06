class Solution {
public:
    int numTrees(int n) {
        vector<int> table(n+1,0);
        table[0] = 1;
        for (int size = 1; size <= n; ++size)
            for (int pivot = 1; pivot <= size; ++ pivot){
                int left = table[pivot-1];
                int right = table[size - pivot];
                table[size] += left * right;
            }
        return table[n];
    }
};
