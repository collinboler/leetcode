import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // declare hashmap
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        // pass through nums
        for (int i = 0; i < nums.length; i++) {
            // see if target - nums[i] is in db, if yes return both, if no add nums[i], i to db
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                result[0] = map.get(complement);
                result[1] = i;
                return result;
            }
            map.put(nums[i], i );
        }
         return result;
        }
      

        // return empty int[] if not
        
        
    }
    

