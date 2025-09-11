class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int curr = 0;  
        for (int i = 0; i < k; i++) {
            curr += nums[i];
        }
        int best = curr;

        for (int i = k; i < nums.length; i++) {
            curr += (nums[i] - nums[i - k]);
            best = Math.max(curr, best);
        }
        double result = Double.valueOf(best) / Double.valueOf(k);
        return result;
    }
}