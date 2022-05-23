class Solution {
public:
    int partition(vector<int>& nums, int l, int r){
        int n = rand()%(r-l+1) + l;
        swap(nums[n], nums[r]);
        int pivot = nums[r];
        int i = l;
        for (int j = l;j<r;j++){
            if (nums[j] < pivot){
                swap(nums[i++], nums[j]);
            }
        }
        swap(nums[i], nums[r]);
        return i;
    }
    void q_sort(vector<int>& nums, int l, int r){
        if (l >= r){
            return;
        }
        int q = partition(nums, l, r);
        q_sort(nums, l, q - 1);
        q_sort(nums, q+1, r);
    }
    
    int findKthLargest(vector<int>& nums, int k) {
        q_sort(nums, 0, nums.size() - 1);
        return nums[nums.size() - k];
    }
};
