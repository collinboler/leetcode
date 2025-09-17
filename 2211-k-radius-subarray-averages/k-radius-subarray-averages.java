class Solution {
    public int[] getAverages(int[] nums, int k) {
        if (((k * 2) + 1) > nums.length) {
            int[] solution = new int[nums.length];
            for (int i = 0; i < nums.length; i++) {
                solution[i] = -1;
            }
            return solution;
        }


        int radius = (k * 2) + 1;

        int[] solution = new int[nums.length];
        long curr = 0;
        for (int i = 0; i < k; i++) {
            solution[i] = - 1;
            curr += nums[i];
        }
        for (int i = k; i < radius; i++) {
            curr += nums[i];
        }

        solution[k] = (int)(curr / radius);
        int left = 0;
   
        int right = radius;
        System.out.println(curr);

        for (int middle = k + 1; middle <= nums.length - k; middle++) {
            if (right > nums.length - 1) break;
            curr += (nums[right] - nums[left]);
            solution[middle] = (int)(curr / radius);
            left++;
            right++;
        }
        for (int i = nums.length - k; i < nums.length; i++) {
            solution[i] = - 1;
        }
        return solution;
    }
}