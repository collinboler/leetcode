import java.util.*;
class Solution {

    public int canBeTypedWords(String text, String brokenLetters) {
        HashSet<Character> set = new HashSet<>();

        for (char c : brokenLetters.toCharArray()) {
            set.add(c);
        }

        // int count = 0;
       
        // String[] words = text.split(" ");

        // // Print each word
        // for (String word : words) {
        //     int i = word.length();
        //     for (char c : word.toCharArray()) {
        //         i--;
        //         if (set.contains(c)) {
        //             System.out.println("hey" + word);
        //             break;
        //         }
        //         else if (i == 0) {
        //             count++;
        //         }
                
        //     }
        // }


        //  String[] words = text.split(" ");

        // Print each word
        int count = 0;
       
        for (int i = 0; i < text.length(); i++) {
            boolean bad = false;

            while (i < text.length() && text.charAt(i)!= ' ') {
                if (set.contains(text.charAt(i))) bad = true;
                i++;
            }
            // i++;
            if (!bad) count++;
        
        }
        return count;
    }
}