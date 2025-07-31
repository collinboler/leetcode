
import java.util.*;
import java.util.Arrays;
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        int i = 0;
        for (int num : nums) { 
            result[i] = num * num;
            i++;
        }
        Arrays.sort(result);
        return result;
    }
}