import java.util.*;
class Solution {
    public int maxNumberOfBalloons(String text) {
        HashMap<Character, Integer> map = new HashMap<>();
        String balloon = "balloon";
        for (char c: balloon.toCharArray()) {
            map.put(c, 0);
        }
        for (char c : text.toCharArray()) {
            if (map.containsKey(c)) map.put(c, map.get(c) + 1);
        }
        
        
        int min = Integer.MAX_VALUE;
        for (char c : map.keySet()) {
            if (c != 'o' && c != 'l' )  min = Math.min(map.get(c), min);
        }
        
        return Math.min(min, Math.min(map.get('o') / 2, map.get('l') / 2));
    } 
}