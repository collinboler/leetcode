class Solution {
    public int minStartValue(int[] nums) {
        int[] prefixSum = new int[nums.length];
        prefixSum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            prefixSum[i] = nums[i] + prefixSum[i - 1];
        }
        int min = Integer.MAX_VALUE;
        for (int p : prefixSum) {
            if (p < min) min = p;
            System.out.println(p);
        }
        if (min < 0){
        return (-1 * min) + 1;
        }
        else return 1;
    }
}