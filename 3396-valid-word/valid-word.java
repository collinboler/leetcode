class Solution {
    public boolean isValid(String word) {
        if (word.length() < 3) return false;
        word = word.toLowerCase();
        HashSet<Character> vowels = new HashSet<>();
        HashSet<Character> letters = new HashSet<>();
        HashSet<Character> consonants = new HashSet<>();
        HashSet<Character> numbers = new HashSet<>();
        Collections.addAll(vowels, 'a', 'e', 'i', 'o', 'u');
        Collections.addAll(letters, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
        Collections.addAll(consonants, 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z');
        Collections.addAll(numbers,'0','1', '2', '3', '4', '5', '6', '7', '8', '9');
        int vowelC = 0; 
        int consC = 0;

        for (char c :  word.toCharArray()) {
            System.out.println(c);
            if (vowels.contains(c)) {
                vowelC++;
            }
            else if (consonants.contains(c)) {
                consC++;     
            }
            else if (!letters.contains(c) && !numbers.contains(c)) {
                System.out.println("Early Exit");
                return false;
            } 
        }
        
        if (consC > 0 && vowelC > 0) return true;
        return false;
       

    }
}