import java.util.*;
class Solution {
    public int largestUniqueNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
     
            }
            else {
                map.put(num, map.get(num) + 1);
            }
        }
        
        int max = Integer.MIN_VALUE;
        int count = 0;
        for (int i : map.keySet()) {
            System.out.println(i + ", " + map.get(i));
            if (map.get(i) == 1) {
                max = Math.max(i, max); count++;
            }
        }
        
        if (count != 0) return max;
        return -1;
        
    
}
}