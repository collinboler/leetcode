class Solution {
    public int maximumWealth(int[][] accounts) {
        int count = 0;
        for (int[] arr : accounts) {
            int temp = 0;
            for (int i : arr) {
                temp += i;
            }
            if (temp > count) count = temp;
        }
        return count;
    }
    
}