class Solution {
    public int longestOnes(int[] nums, int k) {
        // if (k == 0) {
        //     int best = 0;
        //     int count = 0;
        //     int i = 0;
        //         while(i < nums.length) {
                
        //         while (nums[i] == 1 && i < nums.length - 1) {
        //             count++;
        //             i++;
        //         }
        //         best = Math.max(count, best);
        //         i++;
        //         }
        //     return best;        
        // }
        
        int zeros = 0;
        int left = 0;
        int best = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
        
            while (zeros > k) {
                if (nums[left] == 0) zeros--;
                left++;
            }
          
            best = Math.max(best, right - left + 1);
           
        }
        return best;
    }
}