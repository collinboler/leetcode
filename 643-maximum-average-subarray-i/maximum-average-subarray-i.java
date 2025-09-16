class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxSum = 0;
        double curr = 0;
        for (int i = 0; i < k; i++) {
            curr += nums[i];
        }
        maxSum = curr; 
        int left = 0;
        for (int right = k; right < nums.length; right++) {
            curr += nums[right] - nums[right - k];
            maxSum = Math.max(curr, maxSum);
        }
        return maxSum / (double) k;
    }
}