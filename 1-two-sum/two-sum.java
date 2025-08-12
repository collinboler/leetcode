class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        // loop through nums 
        for (int i = 0; i < nums.length; i++) {
            int complement = target-nums[i];
            // adds up to target, return
            if (numMap.containsKey(complement)) {
                return new int[] { numMap.get(complement), i};
            }
            numMap.put(nums[i],i);    
        }
        // nothing that adds up to target
        return new int[0];
    }
}