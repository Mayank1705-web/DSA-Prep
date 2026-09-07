class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;
        int n = nums.size();
        vector<int> result;
        for (int i = 0; i < n; i++){
            if (nums[i] != 0){
                swap(nums[left], nums[i]);
                left += 1;
            }
        }
    }
};