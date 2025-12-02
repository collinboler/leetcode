class Solution {
    public int[] twoSum(int[] nums, int target) {
     // declare hashmap
    
    HashMap<Integer, Integer> map = new HashMap<>();
     // one pass through array

    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) return new int[] {i, map.get(complement)};
        else map.put(nums[i], i);
    }

    return new int[]{};
     // check for complement, if found return both indicies


     // return empty array if none found after pass 
    }
}