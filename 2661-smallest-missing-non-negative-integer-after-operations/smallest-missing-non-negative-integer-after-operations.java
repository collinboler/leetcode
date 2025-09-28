class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        int[] freq = new int[value];

        for (int i : nums) {

            //negative value
            if (i% value < 0) {
                freq[ i % value + value]++;
            }

            else freq[Math.abs(i) % value]++;
        
        }

        // check every number from 0

        int res = 0;
        while (true) {
            if (freq[res % value] == 0) return res;
            freq[res % value]--;
            res++;
        }
}
}