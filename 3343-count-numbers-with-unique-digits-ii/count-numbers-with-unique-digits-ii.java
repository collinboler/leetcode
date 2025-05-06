import java.util.*;
class Solution {

    public int numberCount(int a, int b)  {
        int count = 0;
        for (int i = a; i <= b; i++) {
            if (isUnique(i)) count++;
        }
        return count;
    }
    public Boolean isUnique(int number) {
        HashSet<Integer> set = new HashSet<>();
        while (number > 0) {
            int digit = number % 10;  // Gets the last digit
            if (set.contains(digit)) return false; 
            set.add(digit);
            number /= 10;  // Removes the last digit   
            }
        return true;
    }
}