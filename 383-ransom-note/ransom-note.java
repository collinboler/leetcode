class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        // populate
        for (char c : magazine.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
            // if (!map.containsKey(c)) map.put(c, 1);
            // else map.put(c, map.get(c) + 1);
        }
        for (char c: ransomNote.toCharArray()) {
            if (!map.containsKey(c)) return false;
            if(map.containsKey(c)) {
                if (map.get(c) == 0) return false;
                else map.put(c, map.get(c) - 1);
            }            
        }
        return true;
        
    
        
    }
}