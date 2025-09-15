import java.util.*;
class Solution {

    public int canBeTypedWords(String text, String brokenLetters) {
        HashSet<Character> set = new HashSet<>();

        for (char c : brokenLetters.toCharArray()) {
            set.add(c);
        }

        int count = 0;
       
        String[] words = text.split(" ");

        // Print each word
        for (String word : words) {
            int i = word.length();
            for (char c : word.toCharArray()) {
                i--;
                if (set.contains(c)) {
                    System.out.println("hey" + word);
                    break;
                }
                else if (i == 0) {
                    count++;
                }
                
            }
        }
        return count;
    }
}