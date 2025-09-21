class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] counts = new int[26];
        
        // Count characters in magazine
        for (char c : magazine.toCharArray()) {
            counts[c - 'a']++;
        }
        
        // Check ransom note
        for (char c : ransomNote.toCharArray()) {
            if (--counts[c - 'a'] < 0) return false;
        }
        return true;
    }
}