class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int[] merged = new int[nums1.length + nums2.length];
        
        for (int i = 0; i < nums1.length; i++) {
            merged[i] = nums1[i];
        }
        
        for (int j = nums1.length; j < nums1.length + nums2.length; j++) {
            merged[j] = nums2[j - nums1.length];

        }
        Arrays.sort(merged);

     
    

        if (merged.length % 2 != 0) return merged[merged.length / 2]; // odd
        return ((merged[merged.length/2 - 1] + merged[merged.length/2]) / 2.0); // even
        
    }




}