class Solution {
    public int findFinalValue(int[] nums, int original) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (!set.contains(num)) set.add(num);
            if (num == original) {
                original *= 2;
            }
        }
        while (set.contains(original)) {
            original *= 2;
        }
        return original;
    }
}